import pandas

student_scores = {
    "student": ["Angela", "Martins"],
    "score": [99, 92],
}

student_scores_df = pandas.DataFrame(student_scores)
print(student_scores_df)

# iterate using dictionary methods.
# iterate based on columns
for (key, value) in student_scores_df.items():
    print(key)
    print(value)

# iterate using pandas methods
# iterate based on rows
for (index, row) in student_scores_df.iterrows():
    print(f'Record number ({index}): Student {row.student}, has score - {row.score}')
