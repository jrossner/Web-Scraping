def getDateSuffix(x):
  suffix = ''
  x = int(x)
  
  if x == 1 or x == 21 or x == 31:
    suffix = 'st'
  elif x == 3 or x == 23:
    suffix = 'rd'
  elif x == 22:
    suffix = 'nd'
  else:
    suffix = 'th'
   
  return suffix
