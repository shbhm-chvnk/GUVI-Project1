# Student Result Visualization App
This is Project 1 for GUVI, built using Streamlit and Plotly to visualize student marks. The application reads student data from a CSV file and provides an interactive dashboard with filters, charts, and performance metrics.

## 📁 Repository Structure
guvi-project1/

├── data/

│   └── student_marks_10_students.csv

├── src/

│   └── app.py

└── README.md

## 🚀 Features
🎯 Filter by Class, Exam Term, and Subject

📈 Summary metrics (Average, Highest, and Lowest Marks)

📚 Subject-wise Average Marks (Bar Chart)

🍩 Grade Distribution (Pie Chart)

🏆 Top Performers Table

💡 Dynamic grade assignment based on marks

## 🧪 Tech Stack
Python (Pandas – Data manipulation, Streamlit – Web app framework, Plotly Express – For interactive pie chart)

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/yourusername/guvi-project1.git
cd guvi-project1
```

2. Install dependencies
(Make sure Python is installed)
```bash
pip install streamlit pandas plotly
```

3. Run the app
Navigate to the src/ folder and run:
```bash
cd src
streamlit run app.py
```

4. Ensure CSV Path is Correct
The app expects the CSV at:
```bash
../data/student_marks_10_students.csv
```
So do not move the CSV from the data/ folder.

## 📌 Author
Shubham Chavanke (Project submitted as part of HCL GUVI Internship)

