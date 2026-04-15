import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from student_analysis import analyze_data

# Page Setup
st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

st.title(" Student Performance Dashboard")

subjects = ["Math", "Physics", "Chemistry", "CS"]

# Number of Students Input
num_students = st.slider(
    "Select number of students",
    min_value=1,
    max_value=50,
    value=5
)

students = []
marks = []

st.subheader("Enter Student Details")

# Dynamic Input UI
for i in range(num_students):

    name = st.text_input(
        f"Student {i+1} Name",
        key=f"name{i}"
    )

    students.append(name if name else f"Student{i+1}")

    cols = st.columns(4)

    student_marks = []

    for j in range(len(subjects)):

        mark = cols[j].number_input(
            subjects[j],
            min_value=0,
            max_value=100,
            key=f"{i}{j}"
        )

        student_marks.append(mark)

    marks.append(student_marks)


marks = np.array(marks)

# Analysis Button
if st.button("Analyze Performance "):

    (
        student_avg,
        subject_avg,
        subject_std,
        rank_indices,
        z_scores,
        correlation_matrix
    ) = analyze_data(marks)


    df = pd.DataFrame(
        marks,
        index=students,
        columns=subjects
    )

    st.subheader(" Marks Table")
    st.dataframe(df)

    # Rankings
    st.subheader(" Rankings")

    ranking_df = pd.DataFrame({
        "Student": np.array(students)[rank_indices],
        "Average Marks": student_avg[rank_indices]
    })

    st.dataframe(ranking_df)

    # Subject Average Chart
    st.subheader(" Subject Average")

    avg_df = pd.DataFrame({
        "Subjects": subjects,
        "Average Marks": subject_avg
    })

    st.bar_chart(avg_df.set_index("Subjects"))


    # Difficulty Chart
    st.subheader(" Subject Difficulty")

    std_df = pd.DataFrame({
        "Subjects": subjects,
        "Std Dev": subject_std
    })

    st.bar_chart(std_df.set_index("Subjects"))


    # Correlation Heatmap
    st.subheader(" Correlation Matrix")

    fig, ax = plt.subplots()

    cax = ax.matshow(correlation_matrix)

    fig.colorbar(cax)

    ax.set_xticks(range(len(subjects)))
    ax.set_yticks(range(len(subjects)))

    ax.set_xticklabels(subjects)
    ax.set_yticklabels(subjects)

    st.pyplot(fig)


    # Z-score Table
    st.subheader("Z-score Table")

    z_df = pd.DataFrame(
        z_scores,
        index=students,
        columns=subjects
    )

    st.dataframe(z_df)