while True:												#while loop used to repeat program

  a= int(0)												#Set values to zero to be re-writted
  b= int(0)
  c= int(0)
  d= int(1)												#Set d to one for first loop
  e= int(0)							
  f= int(1)												#Set f to one for first loop
  
  while True:												#input a, while loop checks the input is an integer
      try:
          a= input ("Enter a:")
          a= int(a)
          break
      except ValueError:
          print ("Not valid, input integers only")
  while True:
      try:
          b= input ("Enter b:")
          b= int(b)
          break
      except ValueError:
          print ("Not valid, input integers only")
  while True:
      try:
          c= input ("Enter c:")
          c= int(c)
          break
      except ValueError:
          print ("Not valid, input integers only")
  
  for x in range(1,b+1):										#input b dictates how many times the program will loop
    e = a * d % c											#equation e = a * d mod c
    
    print ("NextPower=" , f , "Solution=" ,a, "*" ,d, "mod" ,c, "=" ,e)					#result is printed
    
    d=e													#for any loops post loop one, e from the predecessing loop will become d
    f=f+1												#this is used in the result to number the loops 
    
  print ()  												#Blank line
  v=input("Would you like to repeat the modular exponentiation calculator? Enter y or n.")		#While loop for possible repeat
  print ()		
  if v == "y":												#if y is inputted then the calculator will repeat 
    continue
  elif v == "n":											#if n is inputted the while loop will end
    break