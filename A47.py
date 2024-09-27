# CC Fundamentals: Feature Engineering 2
###################################################
######### Reference links #########
####################################################
import numpy as np
import pandas as pd
from scipy.stats import levene, ttest_ind, kruskal, chi2_contingency
## Loan amount payable
# In the loan.csv dataset, we wish to test the hypothesis that the loan amount payable per year is different for women and unmarried men.To do so, first define a new feature called 'Loan_Amount_per_year' using the formula 'LoanAmount' / 'Loan_Amount_Term'.
# Next, define group1 as the women loan applicants, and group2 as the unmarried male applicants. Print out their variances.Perform a Levene test using the median as the center to check whether the variances of the two groups are significantly different.
# Next, apply the t-test to check whether the average loan amount payable is significantly different for the two groups. What interpretations can be drawn from the tests conducted?
# Note: Assume the significance level to be 5%.
def loan_amount_payable():
# The Null hypothesis for the Levene test: The variances in the applicant income for the two groups are identical.
# The alternate hypothesis for the Levene test: The variances in the applicant income for the two groups are significantly different.
# The Null hypothesis for the Krushkal test: The medians in the applicant income for the two groups are identical.
# The alternate hypothesis for the Krushkal test: The medians in the applicant income for the two groups are significantly different.
# The Levene test and the t-test have been implemented using the code below.
  # Load the data
  data = pd.read_csv('loan.csv')
  # Compute the Loan_Amount_per_year feature, which is an approximate version of the loan amount payable per year.
  data['Loan_Amount_per_year'] = data['LoanAmount'] / data['Loan_Amount_Term']
  # Unmarried men data
  group1 = data[(data["Gender"] == "Male") & (data["Married"] == "No")]['Loan_Amount_per_year']
  # women data
  group2 = data[(data["Gender"] == "Female")]['Loan_Amount_per_year']
  # dropping the missing values of both the groups
  group1 = group1.dropna()
  group2 = group2.dropna()
  print("Number of group1 datapoints", len(group1))
  print("Variance of group1:",round(np.var(group1),2))
  print("Number of group2 datapoints", len(group2))
  print("Variance of group2:",round(np.var(group2),2))
  #levene test
  levene_p_value = levene(group1, group2, center='median')[1]
  print("levene test p-value", round(levene_p_value,2))
  t_test_p_value = ttest_ind(group1, group2)[1]
  print("t-test p-value:", round(t_test_p_value,2))

## Rejected for a loan
# In the loan.csv dataset, we wish to test the hypothesis that among all loan applicants with a Credit_History of 1 who were rejected for a loan, the married group of people applied for a loan amount that is significantly different from the unmarried applicants.To do so, first, define group1 as the married group and group2 as the unmarried group, and retrieve their "LoanAmount" details. Drop the columns containing 'nan'.
# Print out their variances, and perform a Levene test to check whether the variance in the loan amount for the two groups is significantly different.Next, apply the Krushkal test to check if the median loan amount is significantly different for the two groups. What interpretations can you draw from the tests performed?
# Note: Assume a significance level of 5%.
def rejected_for_a_loan():
  # Load the data
  data = pd.read_csv('loan.csv')
  #loan applicants with a Credit_History of 1 who were rejected for a loan
  chn = data[ (data["Credit_History"] == 1) & (data["Loan_Status"] == "N") ]
  # group1 and group2
  group1 = chn[chn["Married"] == "Yes"]["LoanAmount"]
  group2 = chn[chn["Married"] == "No"]["LoanAmount"]
  #dropping na values
  group1 = group1.dropna()
  group2 = group2.dropna()
  print("Number of group1 datapoints", len(group1))
  print("Variance of group1:",round(np.var(group1),2))
  print("Number of group2 datapoints", len(group2))
  print("Variance of group2:",round(np.var(group2),2))
  #levene test
  levene_p_value = levene(group1, group2, center='median')[1]
  print("levene test p-value", round(levene_p_value,2))
  # Test whether the mean and median are significantly different for the populations
  kruskal_p_value = kruskal(group1, group2)[1]
  print("kruskal test p-value: ", round(kruskal_p_value,2))

## Compare the applicant incomes
# In the loan.csv dataset, we wish to test the hypothesis that among all loan applicants who were rejected for a loan, the applicant income of the people with a credit history of 1 is significantly different from the applicant income of the people with a credit history of 0.To do so, first, define group1 as the people with a credit history of 0, and group2 as the people with a credit history of 1.
# Retrieve their Applicant Income information and drop the columns containing 'nan'. Next, apply the Krushkal test to check whether the mean applicant income of the two groups is significantly different, and the Levene test to check if the variance in the applicant income for the two groups is significantly different. What are the results of these tests, and what interpretations can you draw?
# Note: Assume a significance level of 5%.

def compare_the_applicant_incomes():
  # Load the data
  data = pd.read_csv('loan.csv')
  # group1 and group2
  group1 = data[ (data["Credit_History"] == 1) & (data["Loan_Status"] == "N") ]["ApplicantIncome"]
  group2 = data[ (data["Credit_History"] == 0) & (data["Loan_Status"] == "N") ]["ApplicantIncome"]
  #drop the na values
  group1 = group1.dropna()
  group2 = group2.dropna()
  print("Number of group1 datapoints", len(group1))
  print("Variance of group1:",round(np.var(group1),2))
  print("Number of group2 datapoints", len(group2))
  print("Variance of group2:",round(np.var(group2),2))
  #levene test
  levene_p_value = levene(group1, group2, center='trimmed')[1]
  print("levene test p-value", round(levene_p_value,3))
  krushkal_p_value = kruskal(group1, group2)[1]
  print("kruskal: ", round(krushkal_p_value, 3))

## Female applicant
# In the loan.csv dataset, we wish to test the hypothesis that among all loan applicants who were rejected for a loan, applicants with a credit history of 1 are more likely to be female.
# Use a chi-square test to verify this claim (Ensure that you drop all nan rows), and report your interpretation. Note: Use a significance level of 5%.
def female_applicant():
#   Null hypothesis (H0): the features are independent.
#   Alternate hypothesis (Ha) : the features are dependent.
# The below given code performs the chi2 test and the p-value comes out to be 0.961.
  # Load the data
  data = pd.read_csv('loan.csv')
  # data of all the rejected applicants
  chn = data[(data["Loan_Status"] == "N")]
  #dropping na values
  chn = chn.dropna()
  #contingency table
  contingency = pd.crosstab(chn['Gender'], chn['Credit_History'])
  print(contingency)
  #p-value
  p_value = round(chi2_contingency(contingency)[1],3)
  print('p-value:', p_value)
  if p_value > 0.05:
    print('Since p_value > 0.05, we fail to reject the null hypothesis.')
  else:
    print('Since p_value < 0.05, we reject the null hypothesis.')

## Gender bias
# In the loan.csv dataset, we observed that among all applicants with a credit history of 1, 272 males and 53 females were granted loans, while 66 males and 19 females were not granted loans.
# We suspect a gender bias towards males here, and wish to test if there is any statistical significance to our claim. Perform a chi-square test to do so, and report your interpretations.
# Note: Assume a significance level of 5%.
def gender_bias():
  # Load the data
  data = pd.read_csv('loan.csv')
  # data of all the applicants with a credit history of 1
  chn = data[(data["Credit_History"] == 1)]
  #dropping na values
  chn = chn.dropna()
  #contingency table
  contingency = pd.crosstab(chn['Gender'], chn['Loan_Status'])
  print('Contingency table',contingency)
  # Test whether the mean and median are significantly different for the populations
  p_value=chi2_contingency(contingency)[1]
  #p-value
  print('p-value:', round(p_value,2))
  if p_value > 0.05:
    print('Since p_value > 0.05, we fail to reject the null hypothesis.')
  else:
    print('Since p_value < 0.05, we reject the null hypothesis.')