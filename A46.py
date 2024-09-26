# CC Fundamentals: Feature Engineering 1
###################################################
######### Reference links #########
####################################################

import pandas as pd 
from scipy.stats import ttest_ind 
from scipy.stats import chi2_contingency

## Difference in income group
# We believe that the loan.csv data shows that unmarried men are in a different income group than both married and unmarried women.To prove this, would a t-test be more appropriate or a chi-square test?
# Carry out the test on the 'ApplicantIncome' column for the two groups and report the p-value. Also, report your interpretation. Note: Assume a confidence level of 95% and round off the p-value to 2 decimal places.
def income_group():
  # Since the incomes are a continuous variable, we will use the t-test here.
# Nulll hypothesis (H0) : The incomes of both groups are similar.
# Alternate hypothesis (Ha) : The incomes of both groups are different.
  # Load the data
  data = pd.read_csv('loan.csv')
  # Load the Income data for unmarried men
  unmarried_men = data[(data["Gender"] == "Male") & (data["Married"] == "No")]["ApplicantIncome"]
  unmarried_men.dropna(inplace=True)
  print("Number of unmarried men datapoints: ", len(unmarried_men))
  # Load the data for both married and unmarried women
  women = data[(data["Gender"] == "Female")]["ApplicantIncome"]
  women.dropna(inplace=True)
  print("Number of women datapoints: ", len(women))
  # Perform a t-test since the incomes are a continuous variable.
  p_value = ttest_ind(unmarried_men, women)[1]
  print("p_value :" ,round(p_value,2))
  if p_value > 0.05:
    print('Since p_value > 0.05 we fail to reject the null hypothesis.')
  else:
    print('Since p_value < 0.05 we reject the null hypothesis.')

## Graduate unmarried men
# We believe that the loan.csv data shows that graduate unmarried men are in a different income group than both married and unmarried graduate women.# To prove this, would a t-test be more appropriate or a chi-square test?
# Carry out the test on the 'ApplicantIncome' column for the two groups and report the p-value. Also report your interpretation.
# Note: Assume a confidence level of 95% and round off the p-value to 2 decimal places.

def graduate_unmarried_men():
# Nulll hypothesis (H0) : The incomes of both groups are similar.
# Alternate hypothesis (Ha) : The incomes of both groups are different.
  # Load the data
  data = pd.read_csv('loan.csv')
  # Load the Income data for graduate unmarried men
  unmarried_graduate_men = data[(data["Gender"] == "Male") & (data["Married"] == "No") & (data["Education"] == "Graduate")]["ApplicantIncome"]
  unmarried_graduate_men.dropna(inplace=True)
  print("Number of unmarried graduate men datapoints: ", len(unmarried_graduate_men))
  # Load the data for graduate women
  graduate_women = data[(data["Gender"] == "Female") & (data["Education"] == "Graduate")]["ApplicantIncome"]
  graduate_women.dropna(inplace=True)
  print("Number of graduate women datapoints: ", len(graduate_women))
  # Perform a t-test since the incomes are a continuous variable.
  p_value = ttest_ind(unmarried_graduate_men, graduate_women)[1]
  print("p_value :" ,round(p_value,2))
  if p_value > 0.05:
    print('Since p_value > 0.05 we fail to reject the null hypothesis.')
  else:
    print('Since p_value < 0.05 we reject the null hypothesis.')

## Get a loan
# We believe that the loan.csv data shows that graduate unmarried men are more likely to get a loan than graduate women. To prove this, would a t-test be more appropriate or a chi-square test?
# Perform the appropriate statistical test on the 'Loan_Status' column for the two groups, report the p-value, and provide an interpretation of the results, considering a confidence level of 95%.
# Note: Round the p-value to two decimal places.
def get_a_loan():
# We will perform a chi-square test since the Loan_Status is a categorical variable. Since chi-squared test can only be used to check the independence between two variables, we define our hypothesis as:
#   Null hypothesis (H0) : The likelihood of getting a loan is equal for both groups.
#   Alternate hypothesis (Ha) : The likelihood of getting a loan is not equal for both groups.
# Further, we need to filter our dataframe such that it contains 2 new columns:
#   GraduateUnmarriedMen: That holds True/1 value when the individual is a Graduate Unmarried man, and False/0 otherwise.
#   GraduateWomen: That holds True/1 value when the individual is a Graduate woman, and False/0 otherwise.
# Since we are only concerned with individuals who fall in either of these categories, we drop all rows having False/0 in both these columns (Ungraduate men and women, Gaduate married men, etc).
  # Load the data
  data = pd.read_csv('loan.csv')
  # Add a column indicating that the entry contains graduate and unmarried men
  data['GraduateUnmarriedMen'] = (data["Gender"] == "Male") & (data["Married"] == "No") & (data["Education"] == "Graduate")
  graduate_unmarried_men = data[(data['GraduateUnmarriedMen'] == True)]
  print('Number of graduate married men datapoints:',len(graduate_unmarried_men))
  # Load the data for graduate women
  data['GraduateWomen'] = (data["Gender"] == "Female") & (data["Education"] == "Graduate")
  graduate_women = data[(data["GraduateWomen"] == True)]
  print('Number of graduate women datapoints:',len(graduate_women))
  data = data[(data['GraduateUnmarriedMen'] == True) | (data['GraduateWomen'] == True)]
  # Perform a chi-square test since the loan_Status is a categorical variable.
  contingency = pd.crosstab(data['GraduateUnmarriedMen'], data['Loan_Status'])
  print('\n',contingency,'\n')
  p_value = chi2_contingency(contingency)[1]
  print('p-value:',round(p_value,2))
  if p_value > 0.05:
    print('Since p_value > 0.05 we fail to reject the null hypothesis.')
  else:
    print('Since p_value < 0.05 we reject the null hypothesis.')

## Create a new feature
# We have been given a dataset containing the details of the people applied for loan. dataset: loan.csv
# We wish to create a new feature called 'NewFeature' using a linear combination of the features ApplicantIncome, LoanAmount and Credit_History, with weights 1, 3 and 7000,
# i.e., data['NewFeature'] = (data["ApplicantIncome"]) + (3 * data["LoanAmount"]) + (7000 * data["Credit_History"]).
# Since 'NewFeature' is a numerical feature, convert it to a categorical feature by checking whether 'NewFeature' is greater than 0.25 times the mean of 'NewFeature'. Call this feature 'Separator'.
# Perform a chi-square test on the contingency table formed by the features 'Loan_Status' and 'Separator' and report the p-value. Also report your interpretation.
# Note: Drop all the rows having 'na' values before performing any operation on the data and assume the significance level to be 5%. Also, round off the p-value to four decimal places.
def create_a_new_feature():
  # H0: The features Separator and Loan_Status are independent.
  # Ha: The features Separator and Loan_Status are dependent on each other.
  # Read data
  data = pd.read_csv('loan.csv')
  # Add a column indicating that the entry contains graduate and married men
  data.dropna(inplace=True)
  data['NewFeature'] = (data["ApplicantIncome"]) + (3 * data["LoanAmount"]) + (7000 * data["Credit_History"])
  data['Separator'] = data['NewFeature'] > (data['NewFeature'].mean()*0.25)
  # Perform a chi-square test since the incomes are a continuous variable.
  contingency = pd.crosstab(data['Separator'], data['Loan_Status'])
  print(contingency)
  # p-value calculation
  p_value = chi2_contingency(contingency)[1]
  print('p-value:',round(p_value,4))
  if(p_value < 0.05):
    print("Since p-value < 0.05, the two features 'Separator' and 'Loan_Status' are dependent.")
  else:
    print("Since p-value > 0.05, the two features 'Separator' and 'Loan_Status' are independent.")