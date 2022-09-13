import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

students = pd.read_csv("data/Student_Marks.csv")
print(students["Marks"].mean())
print(students[["number_courses", "Marks"]].median())
print(students[["number_courses", "Marks"]].describe())
print(students["Marks"].describe(percentiles=[0.05, 0.25, 0.5, 0.75]))
print(students.agg(
{
"number_courses": ["max", "min", "median"],
"Marks": ["max", "min", "mean", "median"],
})
)
sns.histplot(data=students["Marks"], bins=10)
plt.show()
sns.boxplot(x=students["Marks"])
plt.show()
print(students[["number_courses", "Marks"]].groupby("number_courses").mean())
print(students.groupby("Marks").mean())
print(students.groupby(["number_courses", "Marks"])["time_study"].mean())
print(students["Marks"].value_counts())