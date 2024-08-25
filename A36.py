# DSML Advanced: Probability and Statistics - 2
###################################################
######### Reference links #########
####################################################

## Bayes' Theorem
# As you know, Covid-19 tests are common nowadays,but some results of tests are not true. Given that the probability of getting covid is 60%, People who tested positive and have covid is 90% but people who 
# tested positive and don't have covid is 10%. Given, positive covid test, What is the probability that they actually have covid? Write a program that calculates the required probability using 
# the P(covid), P(positive|covid) and P(positive|~covid) as the input parameters. Take care that the inputs are taken as strings therefore if you are using those variables ensure to typecast them into floats.
def solve(prior,positive_covid,positive_not_covid):
  p_covid = float(prior)
  p_given_covid = float(positive_covid)
  p_given_not_covid = float(positive_not_covid)
  p_positive_and_covid = (p_given_covid * p_covid)
  p_positive = (p_given_covid * p_covid)+(p_given_not_covid*(1-p_covid)) # probability of getting a positive result is P(Covid)*P(Positive|Covid)+P(Not covid)*P(Positive|Not covid)
  ans = (p_positive_and_covid/p_positive)
  ans = round(ans,3)
  return ans
# print(solve(0.6,0.9,0.1))

## HHT of HTT?
# You flip a coin until either Head Heads Tails or Heads Tail Tails shows up. What's more likely to appear 1st?
# # Detailed Analysis of the Coin Toss Problem

# Definitions:
# P_E: Probability of getting HHT before HTT.
# P_E_H: Probability of getting HHT before HTT given that the first toss is H.
# P_E_T: Probability of getting HHT before HTT given that the first toss is T.
# P_E_HH: Probability of getting HHT before HTT given that the first two tosses are HH.
# P_E_HT: Probability of getting HHT before HTT given that the first two tosses are HT.

# Step-by-Step Breakdown:

# 1. Initial Probability Analysis
# P_E = 1/2 * P_E_H + 1/2 * P_E_T
# P_E_T does not directly influence whether HHT or HTT will appear first,
# so P_E_T can be treated as the probability from the starting point.

# 2. Probability from HH
# P_E_HH = 1
# If you are at HH, any subsequent head still keeps you in the HH state,
# and any tail completes HHT. Hence, P_E_HH = 1.

# 3. Probability from HT
# P_E_HT = 1/2 * P_E_HTT + 1/2 * P_E_HTH
# - P_E_HTT = 0, because HTT has already occurred.
# - P_E_HTH = P_E, because if you are at HT and get another H, you are effectively
# back to H (from which the probability P_E needs to be calculated).
# Thus:
# P_E_HT = 1/2 * 0 + 1/2 * P_E = 1/2 * P_E

# 4. Combining the Probabilities
# Combining all probabilities from initial conditions:
# P_E = 1/2 * P_E_H + 1/2 * P_E_T
# We assume P_E_T = P_E as it represents the base condition not directly affected
# by the first toss being T:
# P_E_H = 1/2 * P_E_HH + 1/2 * P_E_HT
# P_E_H = 1/2 * 1 + 1/2 * 1/2 * P_E = 1/2 + 1/4 * P_E
# Then:
# P_E = 1/2 * (1/2 + 1/4 * P_E) + 1/2 * P_E
# Simplifying:
# P_E = 1/4 + 1/8 * P_E + 1/2 * P_E
# P_E = 1/4 + 5/8 * P_E
# 3/8 * P_E = 1/4
# P_E = 2/3

# Conclusion:
# The final probability P_E of getting HHT before HTT is indeed 2/3,
# indicating that HHT is more likely to appear before HTT. This result
# aligns with the correct mathematical analysis of the problem.
