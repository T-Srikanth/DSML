# DSML Advanced: Pandas 1
###################################################
######### Reference links #########
####################################################

## Return the Slice
# You're given a record of students with their registration dates and registration IDs. You're also given the marks scored by each student in Physics, Chemistry, and Mathematics.
# You need to find out the average marks by the students who registered on or after 01/05/2014 i.e. May 1st, 2014.
# Return a list with the corresponding register IDs of the students sorted by their average marks in all three subjects in increasing order.
import pandas as pd  
df = pd.DataFrame({'dates':["2015-12-06", "2011-12-27", "2015-09-07", "2012-12-21", "2020-02-13"], 
                   'RID':[498, 721, 375, 464, 813], 
                   'Phy':[22, 45, 1, 65, 22], 
                   'Chem':[52, 56, 32, 50, 24], 
                   'Math':[63, 37, 68, 62, 43]})
def solve(df):
  sliced_df = df[df["dates"]>="2014-05-01"] 
  sliced_df["Avg"] = (sliced_df["Phy"]+sliced_df["Chem"]+sliced_df["Math"])/3
  sliced_df.sort_values("Avg", inplace=True)
  return [x for x in sliced_df["RID"]]
# print(solve(df))