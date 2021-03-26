while True: 										#while loop for possibility of repeating program
  
  while True:										#integer check for input a
      try:
          a= input ("Enter a:")
          a= int(a)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  while True:										#integer check for input b
      try:
          b= input ("Enter b:")
          b= int(b)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  
  def gcd(a,b):										#define function
    c=abs(a-b)										#c = the absolute value of a minus b
    if (a-b)==0:									# if a-b=0 
      return b										#function outputs b
    else:										
      return gcd(c,min(a,b))								#function outputs smallest value out of a,b and c
  
  d=gcd(a,b)										#function assigned to value d									
  
  if d==1:
      print ("-They are relative primes")						#if the gcd is one they are relative primes
  else:
      print ("-They are not relative primes")						#else/ if the gcd is not one they are not relative primes
      
  print ()  
  v=input("Would you like to repeat the relative prime identifier? Enter y or n.")	#while loop for repeating program
  print ()
  if v == "y":										#y repeats program
    continue
  elif v == "n":									#n ends program
    break