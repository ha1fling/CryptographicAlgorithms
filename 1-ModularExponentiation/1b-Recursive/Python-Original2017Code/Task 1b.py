while True:							#Wile loop to possibly repeat program

  while True:							#While loop used to check an integer is entered for a
      try:
          a= input ("Enter a:")
          a= int(a)
          break
      except ValueError:
          print ("Not valid, input integers only")
  while True:							#While loop used to check an integer is entered for b
      try:
          b= input ("Enter b:")
          b= int(b)
          break
      except ValueError:
          print ("Not valid, input integers only")
  while True:							#While loop used to check an integer is entered for c
      try:
          c= input ("Enter c:")
          c= int(c)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  def modularExponentiation(a,b,c):				#define the function
  
    if b==1:							#if b is equal to one
        return (a%c)						#the function will out put a mod c 
    elif b==0:							#if b is equal to zero
        return 1						#the function will output one
    else:							#if b equals anything else
        return (a**b) % c					#the function will output a^b mod c
  
  
  d= modularExponentiation(a,b,c)				#name function d
  
  print (a,"^", b, "mod", c, "=",d)				#output a ^ b mod c = d with figures to replace the variables.
  
  print ()  											#while loop to repeat the program if the user wants
  v=input("Would you like to repeat modular exponentiation calculator? Enter y or n.")		
  print ()
  if v == "y":							#if y is input the progam will repeat
    continue
  elif v == "n":						#if n is input the program will end
    break