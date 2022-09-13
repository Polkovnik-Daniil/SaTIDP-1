#import pandas as pd
#titanic = pd.read_csv('data/titanic.csv')
#titanic["Age"].mean()
#titanic[["Age","Fare"]].median()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

students = pd.read_csv("data/student_data.csv")
print(students["school"].mean())
print(students[["school", "sex"]].median())
print(students[["school", "sex"]].describe())
print(students["avg_rating"].describe(percentiles=[0.05, 0.25, 0.5, 0.75]))
print(students.agg(
{
"school": ["max", "min", "median"],
"sex": ["max", "min", "mean", "median"],
})
)
sns.histplot(data=students["avg_rating"], bins=10)
plt.show()
sns.boxplot(x=students["avg_rating"])
plt.show()
print(students[["year", "avg_rating"]].groupby("year").mean())
print(students.groupby("year").mean())
print(students.groupby(["year", "likes"])["avg_rating"].mean())
print(students["year"].value_counts())