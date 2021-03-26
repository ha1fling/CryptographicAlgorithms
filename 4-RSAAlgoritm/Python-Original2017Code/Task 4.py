while True:
  print("This is an RSA Cipher")
  print ()
  print ("The following are prime numbers above 255, the higher the prime number the longer the program will take to progress.")
  print ()
  print ("257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359...")
  print ()
  
  while True:
    a=int(input("Enter a prime number 255 or larger."))					#while loop prime number checker
    if a > 1:
     for i in range(2,a):
         if (a % i) == 0:
             print(a,"is not a prime number- enter y to try again")			#if a prime number is not entered the user should enter y to try again
             print ()
             break
     else:
         print(a,"is a prime number to make",a,": P enter 'n'.")			#if a prime number is entered the user should enter y to continue
         print ()
    v=input("Enter y or n")
    print ()
    if v == "y":
      continue
    elif v == "n":
      break
  
  
  while True:
    b=int(input("Enter any prime number that is different to the previous."))
    if b > 1:
     for i in range(2,b):
         if (b % i) == 0:
             print(b,"is not a prime number- enter y to try again")
             print ()
             break
     else:
         print(b,"is a prime number to make",b,": Q enter 'n'.")
         print ()
    v=input("Enter y or n")
    print ()
    if v == "y":
      continue
    elif v == "n":
      break
    
  P = a  							#input from first prime number checker: a becomes P
  Q = b								#input from first prime number checker: b becomes Q
  N = (P*Q)							
  Z = (P-1)*(Q-1)
  m = input("Enter your message here:")				#input enters message here
  d = int(0)							#d is set to zero for first loop
  M= ([ord(ASCII) for ASCII in m])				#the message is turned into ASCII (this is just for show)
  
  
  
  import random
  while True:
  	x = random.randint(2, 100)				#random number generated between 2 and 100
  	K = x*Z + (1)						#random number multiplied by Z and one is added
  
  	list = []
  	for i in range(2,K):					#a list of factors of K is created
  		if K % i == 0:					
  			list.append(i)
  	E = (random.choice(list))				#random number from list assigned to variable "E"
  	D = K // E						#floor division used to divide K by E to get variable "D"
  	break							#While loop ends
  
  e= [int((ord(ASCII)**E)%N)for ASCII in m]			#The message is encrypted using E and N
  d = [int((x**D)%N)for x in e]					#The message is decrypted using D and N
  a= [chr(ASCII)for ASCII in d]					#The message is changed from ASCII to plaintest
  s = "".join(map(str, a))					#The message is converted from a list to a string
  
  print ()
  print ("The encrypted message is:", e)			#This shows the encrypted message
  print ()
  print ("The decrypted message is:", s)			#This shows the decrypted message which is the same as the input
  
  v=input("Would you like to repeat the RSA cipher? Enter y or n.")		
  print ()	
  if v == "y":							#if y is input the program will repeat
    continue
  elif v == "n":						#if n is input the program will end
    break