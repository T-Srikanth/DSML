# Probability distributions - 4
###################################################
######### Reference links #########
####################################################

## Analyze the time
# You are hired as a data scientist for the company SellMart. Your first task is to analyze the durations of customer support call.
# On an average, a customer care executive takes about 5 minutes to solve the issue of any customer. It is known that the time taken follows an exponential distribution.
# Find the probability that an executive spends 4 to 5 minutes with any randomly selected customer.
from scipy.stats import expon
mu = 5
x1 = 4
x2 = 5
e1 = expon.cdf(x = x1, scale = mu) # The probability of spending 4 mins
e2 = expon.cdf(x = x2, scale = mu) # The probability of spending 5 mins
e3 = e2 - e1 #The probability of spending 4 to 5 mins
print("The probability that an executive spends 4 to 5 minutes with any randomly selected customer is", round(e3*100,2),"%.")
# Given,
# μ = 5
# So, λ = 1/5
# Now, the probability of spending 4 to 5 mins with any randomly selected customer is P(4 < X < 5)

# We know CDF of Exponential distribution = 1 - e(-x/μ)
# So,
# P(X < 5) = 1 - e(-5/5) = 1 - 0.3678 = 0.6321
# P(X < 4) = 1 - e(-4/5) = 1 - 0.4493 = 0.5506
# Now,
# P(4 < X < 5) = P(X < 5) - P(X < 4) = 0.6321 - 0.5506 = 0.08142 which is 8.14%.

## Sales Day
# Sales delay is the elapsed time between the manufacture of a product and it’s sale. It is quite common for investigators to model sales delay using a lognormal distribution.
# For a particular product, the distribution with the following parameter values is proposed : μ = 2.05 and variance = 0.08 (here the unit for delay is months).
# i) What is the standard deviation of delay time ?
# ii) What is the probability that delay time exceeds 10 months?
## Answer - delay time(T) follows lognormal distrbution with μ = 2.05 and variance = 0.08 of X, where X = log(T)
# i) Calculation of standard deviation of delay time (standard deviation of T):
# We know that for a lognormal distribution, Var(X) = (e^(2μ+σ^2) (e(σ^2)-1)
# Given, μ = 2.05 and variance = 0.08 = σ^2
#  Substitute those values to get variance 
# Variance = 5.44266
# Therefore, Standard deviation (sqrt(Variance))= *****2.332 months*****
# ii) The probability that delay time exceeds 10 months
# P(X > 10) = P(ln(X) > ln(10))  # Applying ln on both sides
# Now, since X follows a log normal distribution, therefore ln(X) will follow the normal distribution with μ = 2.05 and variance = 0.08.
# P(ln(X) > ln(10)) = P((ln(X)−μ)/σ  >  (ln(10)−2.05)/sqrt(0.08))
# P(Z >  (2.302−2.05)/0.28280) = *****0.18589*****

## Customers Spend
# The amount of money customers spend in one trip to the supermarket follows an exponential distribution with a mean amount of Rs 1000.
# If a customer has Rs 600 in the wallet, what is the probability that the customer will need more money? Note: Round the output up to 2 decimal places.
from scipy.stats import expon
mu = 1000
x = 600
# The probability that the customer will need more money.
e = 1 - (expon.cdf(x=x,scale=mu))
print(round(e,2),"is the probability that the customer will need more money.")
# The question is indirectly asking about the probability that the customer will spend more than Rs 600 in the supermarket.
# Given,The average spend = 1000
# Therefore, λ =  1/1000
# P(the customer will spend more than Rs 600 in the supermarket) = P(X > 600)
# P(X > 600) = 1 – P(X ≤ 600) = 1 - cdf(x = 600)
# The cumulative distribution function for the exponential distribution is given as: P(X<x) = (1 −e^(−λx))
# P(X > 600) = 1 −(1 − e^(−600/1000)) = e^(-3/5)
# P(X > 600) = *****0.55*****

## Running Shoes
# A new pair of running shoes of Brank X are known to last 6 months, on an average, assuming that they are used every day.
# It is known that the duration of their lifespan follows exponential distributed.
# If a pair has already lasted 5 months, find the probability that it will last a total of over 9 months.
from scipy.stats import expon
mu = 6
x1 = 5
x2 = 9
x3 = x2 - x1
# Probability that it will last a total of over 9 months
e = 1 - (expon.cdf(x=x3,scale=mu))
print("The probability that it will last a total of over 9 months:", round(e,2))
# Let,
# T= the lifetime of the pair of shoes.
# Given, the average lifetime = 6 months
# Therefore, λ =  1/6
# The cumulative distribution function is : P(T<t) = 1−e^(−t/6)
# We need to find P(T>9| T>5)
# Using memoryless property,i.e. P(X>x+a | X>a) = P(X>x)
# P(T>9| T>5) = P(T>4)
# P(T>4) = 1 - P(T<4)
# P(T>4) = 1-(1 - e^(−4/6))
# P(T>4) = 0.5134 ≈ *****0.51******