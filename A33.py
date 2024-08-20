# DSML Advanced: Pandas 3
###################################################
######### Reference links #########
####################################################

## Max registrations they asked
# You're given a record of students with their registration dates and registration ids. You're also given the marks scored by each of the students in Physics, Chemistry, and Mathematics.
# You need to find out the month that observed the maximum registrations. Then return the average marks scored in each subject. In case of a tie, select the month that comes first (lexicographically).
import pandas as pd
import numpy as np
def max_reg():
  df = pd.DataFrame({'Date':["2015-12-06", "2011-12-27", "2015-09-07", "2012-12-21", "2020-02-13", "2015-06-09"], 
                    'R_id':[498, 721, 375, 464, 813, 853], 
                    'Phy':[22, 45, 1, 65, 22, 17], 
                    'Chem':[52, 56, 32, 50, 24, 61], 
                    'Math':[63, 37, 68, 62, 43, 42]})
  df["Date"] = pd.to_datetime(df["Date"])
  df["Month"] = df["Date"].dt.month_name()
  high_freq= df["Month"].value_counts().max()
  month=df["Month"].value_counts().sort_index()
  freq_month= month[month.values==high_freq].index[0]
  c = np.round(df[df['Month'] == freq_month]['Chem'].mean(),2)
  p = np.round(df[df['Month'] == freq_month]['Phy'].mean(),2)
  m = np.round(df[df['Month'] == freq_month]['Math'].mean(),2) 
  print(freq_month)
  return(pd.Series([freq_month[:3].upper(), high_freq, c, p, m,]))
# print(max_reg())

## Get the Month
# As an educational institute, you need to keep a track of all the registered students. Here you're given the registration IDs and the corresponding dates of a batch of students.
# You need to return a DataFrame containing the columns as follows:
#  - RID: Id of the student
#  - RDate: Date of joining of the student
#  - RMonth: Month of joining of the student
#  - RYear: Year of joining of the student
#  - RDay: Day of joining of the student
import pandas as pd
def solve(reg_id, reg_dates):
  res_df = pd.DataFrame(zip(reg_id, reg_dates), columns=["RID", "RDate"])
  """
  input:
  reg_id -> id of the input dataframe
  reg_dates -> dates of the input dataframe
  res_df -> the input dataframe 
  
  output:
  return the resultant dataframe after performing the required operation
  """
  res_df["RDate"] = pd.to_datetime(res_df["RDate"])
  res_df["RMonth"] = res_df["Rdate"].dt.month
  res_df["RYear"] = res_df["RDate"].dt.year
  res_df["RDay"] = res_df["RDate"].dt.day
  return res_df