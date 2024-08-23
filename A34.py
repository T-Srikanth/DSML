# DSML Advanced: Python Regular Expressions
###################################################
######### Reference links #########
####################################################

## Valid or not?
# Write a python program to check whether a password is valid or not. A valid password must satisfy the following conditions:
# 1. should be at least eight characters long
# 2. contains atleast one uppercase character
# 3. contains atleast one lowercase character
# 4. has at least one digit
# 5. has at least one special character, special characters are '$','#', and '@'
# 6. shouldn't have any space
import re
def valid_or_not(password):
  while True:  
    if len(password)<8:
      break
    elif not re.search("[a-z]",password):
      break
    elif not re.search("[0-9]",password):
      break
    elif not re.search("[A-Z]",password):
      break
    elif not re.search("[$#@]",password):
      break
    elif re.search("\s",password):
      break
    else:
      return 'Valid Password'
  return 'Invalid Password'
# print(valid_or_not("Nikhil2709$"))

## Valid postal code
# Write a program to check if a postal code is a valid postal code or not. A valid code has to fulfill the below requirements:
# 1. must be a six-digit number.
# 2. must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits that repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
def valid_postal_code(code):
  return bool(re.match(r'^[1-9][\d]{5}$',code) and len(re.findall(r'(\d)(?=\d\1)',code))<2 )

## Valid debit card
# You opened your bank account in an XYZ bank. You received your debit card recently but you want to check whether its a valid debit card or not.
# A valid debit card has the following characteristics:
# It must start with a 4,5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits
# It must NOT use any separator like ' ', '_', etc.
def valid_debit_card(num):
  match_output = re.match(r'^[456][\d]{15}',num)
  if match_output is not None and num == match_output.group():
    return True  
  return False