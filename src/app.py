import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv("../data/student_marks_10_students.csv")

# Assign grades
def assign_grade(marks):
    if marks >= 90: return 'A+'
    elif marks >= 80: return 'A'
    elif marks >= 70: return 'B'
    elif marks >= 60: return 'C'
    elif marks >= 50: return 'D'
    else: return 'F'

df['Grade'] = df['Marks'].apply(assign_grade)

# Title
st.title("📊 Student Result Visualization")

# Sidebar filters
st.sidebar.header("📌 Filters")

class_filter = st.sidebar.selectbox("Select Class", sorted(df['Class'].unique()))
term_filter = st.sidebar.selectbox("Select Exam Term", sorted(df['ExamTerm'].unique()))
subject_filter = st.sidebar.selectbox("Select Subject", ["All"] + sorted(df['Subject'].unique()))

# Apply filters
filtered_df = df[(df['Class'] == class_filter) & (df['ExamTerm'] == term_filter)]
if subject_filter != "All":
    filtered_df = filtered_df[filtered_df['Subject'] == subject_filter]

# Summary metrics
st.subheader("📈 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("📊 Overall Average", round(filtered_df['Marks'].mean(), 2))
col2.metric("🏅 Highest Score", filtered_df['Marks'].max())
col3.metric("📉 Lowest Score", filtered_df['Marks'].min())

# Subject-wise average bar chart
if subject_filter == "All":
    st.subheader("📚 Subject-wise Average Marks")
    subject_avg = filtered_df.groupby('Subject')['Marks'].mean().reset_index()
    st.bar_chart(subject_avg.set_index('Subject'))

# Grade distribution pie chart
st.subheader("🍩 Grade Distribution")
grade_counts = filtered_df['Grade'].value_counts().reset_index()
grade_counts.columns = ['Grade', 'Count']
fig = px.pie(grade_counts, names='Grade', values='Count', title='Grade Distribution')
st.plotly_chart(fig)

# Top performers table
st.subheader("🏆 Top Performers")
n = st.slider("Number of Top Performers", 1, 10, 3)
top_df = filtered_df.groupby(['StudentID', 'Name'])['Marks'].mean().reset_index()
top_df = top_df.sort_values(by='Marks', ascending=False).head(n)
st.dataframe(top_df.style.highlight_max(axis=0))
