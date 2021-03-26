while True: 									#While loop to make the program repeatable
  
  while True:									#integer check for input a
      try:
          a= input ("Enter a:")
          a= int(a)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  while True:									#integer check for input b
      try:
          b= input ("Enter b:")
          b= int(b)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  
  def gcd(a,b):									#define function
    c= abs(a-b)									#c = the absolute value of a minus b
    if (a-b)==0:								#if a-b=0 
      return b									#function returns value for b
    else:									
      return gcd(c,min(a,b))							#else, function returns the smallest value out of: a, b and c is returned
  
  d=gcd(a,b)									#function becomes d
  print ("The greatest common denominator of", a, "and", b, "is", d,".")	#output function as the gcd
  
  print ()									#insert space for tidiness  
  v=input("Would you like to repeat the GCD calculator? Enter y or n.")		#While loop to repeat program
  print ()
  if v == "y":									#y repeats program
    continue
  elif v == "n":								#n ends program
    break