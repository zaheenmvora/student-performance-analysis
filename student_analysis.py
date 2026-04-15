import numpy as np

def analyze_data(marks):

    student_avg = np.mean(marks, axis=1)

    subject_avg = np.mean(marks, axis=0)

    subject_std = np.std(marks, axis=0)

    rank_indices = np.argsort(student_avg)[::-1]

    z_scores = (marks - np.mean(marks, axis=0)) / np.std(marks, axis=0)

    correlation_matrix = np.corrcoef(marks.T)

    return (
        student_avg,
        subject_avg,
        subject_std,
        rank_indices,
        z_scores,
        correlation_matrix
    )