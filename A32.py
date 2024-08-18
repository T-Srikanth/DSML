# DSML Advanced: Pandas 2
###################################################
######### Reference links #########
####################################################

## Her discipline
# Which of the following discipline(s) observed more female participants as compared to male participants in Olympics-2021? Use the EntriesGender dataset
import pandas as pd
def one():
  df1 = pd.read_excel('/Users/srikanth/Downloads/EntriesGender.xlsx',engine='openpyxl')
  return df1.loc[df1["Female"]>df1["Male"]]

## Hey Coach
# Given the data set containing data of Olympics 2021. Who among the following has served as the coach of both his/her national men and women team (here teams should necessarily be different for men and women, not duet) in Olympics 2021?
def two():
  df2 = pd.read_excel('/Users/srikanth/Downloads/Olympics21/Coaches.xlsx',engine='openpyxl')
  df2 = df2[df2["Event"]!="Duet"]
  df2a = df2["Name"].value_counts().to_frame()  # check number of times the coach name appeared
  df2a = df2a.reset_index()
  ans = df2a[df2a["count"]>1]
  return ans

## Medals
# Which of these countries got more gold medals than silver and bronze combined, yet are ranked at positions greater than 70 by total medals obtained in Olympics 2021?
def three():
  df3 = pd.read_excel('/Users/srikanth/Downloads/Olympics21/Medals.xlsx',engine='openpyxl')
  df3["s_and_b"] = df3["Silver"]+df3["Bronze"]
  ans = df3[(df3["Gold"]>df3["s_and_b"]) & (df3["Rank by Total"]>70)]["Team/NOC"]
  return ans

## 10 teams
# How many countries sent less than 10 teams to Olympics 2021?
def four():
  df4 = pd.read_excel('/Users/srikanth/Downloads/Olympics21/Teams.xlsx',engine='openpyxl')
  df4a = df4["Name"].value_counts().to_frame().reset_index()
  return df4a[df4a["count"]<10]

##  Haven't followed the instructions?
# In the above-given dataframe, usernames are the display names of the learner's accounts shown on a video-conferencing app when taking classes.
# The instructor clearly said to the learners that usernames must contain the real name (name) of the learners. Return userid of learner who failed to do so.
data = {
    'name': ['Jim', 'Clarke', 'Kent', 'Mark'],
    'username': ['itsjimhere', 'clark002', 'itskentment', 'markyoumustknow'],
    'userid': [20, 10, 86, 21]
}
df5 = pd.DataFrame(data)
def check(name,username):
  return name.lower() in username
# print(df5) 
# print(df5[~(df5.apply(lambda x:check(x['name'],x['username']), axis=1))]['userid'])

## preprocess the dataframe
# Given a dataframe df as input, perform the following steps for preprocessing:
#   - Remove the row if all the columns have missing values.
#   - Replace the missing values of Roll_ID column with 0 and Name column with "Anonymous".
#   - Replace the missing values in Marks column with the median value of the column.
#   - Change the numerical columns (Roll_ID and Marks) to int datatype in the output.
#   - Reset the index of the dataframe returned as shown in the sample output.
# Note: Every column of the input dataframe df is currently of object type.
import numpy as np
data = {
  'Roll_ID': ['412', np.nan, '456', np.nan, '434', '429', '418'],
  'Name': ['John', 'Mitra', 'Ritz', np.nan, 'Anny', 'Hema', np.nan],
  'Marks': [np.nan, '32', '25', np.nan, '35', '28', '38']
}
df6 = pd.DataFrame(data)
def preprocess(df6):
  print(df6)
  df6a = df6[~(np.all(df6.isna(),axis=1))] #remove rows with all missing values
  values = {"Roll_ID": 0,"Name": "Anonymous","Marks": 0} 
  df6a.fillna(value= values,inplace=True) #replace missing roll_id, name and marks
  median = df6a["Marks"].median() #find median
  df6a.replace(to_replace= 0, value= median,inplace=True) #replace 0 marks with median value
  df6a["Roll_ID"] = df6a["Roll_ID"].astype(int) #change type to int
  df6a["Marks"] = df6a["Marks"].astype(int) #change type to int
  df6a.reset_index(drop=True) #reset index to have continuous numbers and drop the previous index
  return df6a
#OR
def perprocess_2():    
  df = pd.DataFrame(data)
  # 1. Remove rows where all columns have missing values
  df = df.dropna(how='all')
  # 2. Replace missing values in Roll_ID column with 0
  df['Roll_ID'].fillna('0', inplace=True)
  # 3. Replace missing values in Name column with "Anonymous"
  df['Name'].fillna('Anonymous', inplace=True)
  # 4. Replace missing values in Marks column with the median value
  df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
  median_marks = df['Marks'].median()
  df['Marks'].fillna(median_marks, inplace=True)
  # 5. Convert Roll_ID and Marks to int datatype
  df['Roll_ID'] = df['Roll_ID'].astype(int)
  df['Marks'] = df['Marks'].astype(int)
  # 6. Reset the index of the DataFrame
  df.reset_index(drop=True, inplace=True)
  return df

## Data Treatment
# Your task will be to:
#  - Replace all null/nan values with 0
#  - Replace all negative infinite values with -1 and positive infinities with 1 (usually these will be of type np.inf)
#  - The non-null and non-inf values, basically integers, range from the range 50-100. Replace each such value with the square root of the same, and round them off up to 2 decimal places.
def data_treatment():
  df7 = pd.read_csv('/Users/srikanth/Downloads/input_data.csv')
  df7.fillna(0, inplace=True) #replace all null.nan values to 0
  # print(df7.isna().sum())
  df7.replace(-np.inf,-1,inplace=True)
  df7.replace(np.inf,1,inplace=True)
  df7['dataPoints'] = df7['dataPoints'].apply(lambda x: round(np.sqrt(x), 2) if 50 <= x <= 100 else x)
  df7.set_index("id",inplace=True)
  df7.to_csv('/Users/srikanth/Downloads/output.csv')
  return

## Concatenation-average
# Tests were taken in two sets 1 and 2. Names of the students who participated in the respective tests are given. Marks are recorded according to the subjects, names, and tests.
# df1 and df2 contain test1 and test2 respectively. You are required to return the following:
#  - The average Chemistry score of students from both the dataframes.
#  - The average score across all the subjects for students who participated in both sets of exams (here all subjects of both the exams have to be considered together).
def concat_avg():
  res = []
  df8a = pd.DataFrame({"name": ['tobey', 'peter', 'chris', 'pratt'],'chem_score':[10, 9, 8, 7], 'phy_score':[7, 8, 9, 10], 'Hindi_score':[9, 9, 9, 9]})  
  df8b = pd.DataFrame({"name": ['chris', 'pratt', 'andrew', 'tom'],'chem_score':[10, 10, 10, 9], 'maths_score':[6, 6, 7, 9], 'eng_score':[9, 10, 10, 9]})
  chem = pd.concat((df8a,df8b)).reset_index(drop=True)
  a1 = float(chem["chem_score"].mean())
  res.append(a1)
  test = pd.merge(df8a,df8b,how="inner",on="name")
  a2 = test.mean(axis=1).to_list()
  res.append(a2)
  return res
# concat_avg()

## As a series
# You're working on collecting the text data for a Natural Language Processing(NLP) project. You come up with the idea of storing the unique words (case-sensitive) with their frequency in a Pandas Series object.
# You are given the raw data in form of a string, Write a function which can take a string as an input and return the unique words and the corresponding frequency in form of a Pandas Series object.
# The indices of the series should be the unique words and the values should be the frequency of those unique words.
# Note that:
#  - String contains no special character.
#  - Always a Non-empty string.
#  - Case sensitive i.e. He and he should be treated as two different word tokens.
#  - Series returned is expected to be sorted by sort_index()for sorting all the words.
def series(string):
  s = pd.Series(string.split(" "))
  return s.value_counts().sort_index()
# string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# series(string)
