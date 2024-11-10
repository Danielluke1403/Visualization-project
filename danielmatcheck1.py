import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#reading the csv file
df=pd.read_csv(r'C:\Users\danie\Documents\python\StudentPerformanceFactors.csv')
#cleaning and normalising the data
df.head()
df.info()
df=df.dropna()
df.isnull().sum()
df.describe().T
for col in df:
    print(df[col].value_counts())
    print("-----------------------")
#visualisation 

#Countplots are useful for comparing and counting the number of observations in different groups within a categorical feature.

for col in df:
    if df[col].dtype == 'O':
        sns.countplot(x=col,data=df)
        plt.show()

#histogram
for col in df:
    if df[col].dtype != 'O':
        sns.histplot(df[col],kde=True)
        plt.show()


#this the code for showing the relationship between distance from home and attendance
sns.boxplot(x='Distance_from_Home',y='Attendance',data=df)


#this shows the relationship between hours studied and exam score
plt.figure(figsize=(8,8))
sns.lmplot(x='Hours_Studied', y='Exam_Score', data=df)
plt.show()


#here is a boxplot for parental involvement and how the student performs through their exam score

sns.boxplot(x='Parental_Involvement', y='Exam_Score', data=df)
plt.title('Parental Involvement vs Exam Score')
plt.show()

#here is the gender vs exam score barplot graph

sns.barplot(x='Gender', y='Exam_Score', data=df)
plt.title('Gender vs Exam Score')
plt.show()

#here we can find out the parents education level and how it can be a boon or gain for the student
sns.boxplot(x='Parental_Education_Level', y='Exam_Score', data=df)
plt.title('Parental Education Level vs Exam Score')
plt.show()


#this is the scatterplot for study hours and scores 
sns.scatterplot(x='study_hours', y='Exam_Score', data=df)
plt.title('Study Hours vs. Scores')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.show()