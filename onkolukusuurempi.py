def onkolukusuurempi(x, y):
  if not type(x) is int:
     raise TypeError("Only integers are allowed")
  elif not type(y) is int:
     raise TypeError("Only integers are allowed")
  elif x > y:
     returnvalue = "on"
  elif x < y:
     returnvalue = "ei ole"
  elif x == y:
     returnvalue  = "yhtä suuret"
  return returnvalue
  
  
