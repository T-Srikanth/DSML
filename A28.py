# DSML Advanced: Exception Handling
###################################################
######### Reference links #########
####################################################

## Salary in range
# Design a function check_salary() that takes salary as an argument and raises a custom exception named SalaryNotInRangeError if the salary is not in range (10000, 100000). Both the boundaries are exclusive
# Handle the raised exception with the message "Salary is not in range" else print "Congratulations!!".
class SalaryNotInRangeError(Exception):
  """
  Exception raised for errors in the input salary.
  Attributes:
      message -- explanation of the error
  """
  def __init__(self, message="Salary is not in range"):
    self.message = message
    super().__init__(self.message)
def check_salary(salary):
  try:
    # Check if salary is within the exclusive range (10000, 100000)
    if not (10000 < salary < 100000):
      # Raise the custom exception if the salary is out of range
      raise SalaryNotInRangeError()
    else:
      # If within range, print a success message
      print("Congratulations!!")  
  except SalaryNotInRangeError as e:
    # Handle the exception and print the error message
    print(e)
# Test the function with different salary values
# check_salary(9500)   # Should raise the exception
# check_salary(15000)  # Should print "Congratulations!!"
# check_salary(100000) # Should raise the exception
