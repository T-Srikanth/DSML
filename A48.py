# DSML Adv: Linear Algebra 3 - Halfspaces and distance
###################################################
######### Reference links #########
####################################################

## Straight line or not
# You are given a list of (X,Y) coordinates, check whether the coordinates lie on a straight line or not. If they lie on a straight line return the slope and intercept else return −1.
def straight_line_or_not(coordinates):
  """
      Input is the list of tuples containg the coordiantes.
      Fucntion computes the slope and intercept if the points lies in a straight line.
      If lie straight line return the tuple (slope,intercept) having float values till one deciaml point.
      else, return -1
  """
  slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
  intercept = coordinates[0][1] - slope*coordinates[0][0]
  for i in range(1,len(coordinates)-1):
    if(coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0]) != slope:
      return -1
  return (slope,intercept)

co = [(5.0, 5.0), (-2.0, -3.0), (0.0, 0.0), (14.0, 6.7), (-3.0, -6.3)]
# print(straight_line_or_not(co))