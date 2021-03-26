while True:					  #while loop used to repeat program
  
  C=int(0)                                        #set C to zero for first loop
  f= 1
  p=int(0)                                        #set p to zero                
  q=int(4)                                        #set q to four
  
  k= input ("Key:")                               #input hex key
  K=int((k), 16)                                  #covert hex to decimal
  B="{0:04b}".format(K)
  print ("The key is:", B)
  
  a= input ("Hex string:")                        #input hex string
  b=int((a), 16)                                  #convert hex to decimal
  c="{0:020b}".format(b)                          #convert decimal to binary
  print ("input in binary:", c)
  print ()
  
  
  
  for j in [1,2,3,4,5]:                           #There are five blocks to be looped
  
      m =list(str(c))                                 #string to list
      print (m)
      o=m[p:q]                                        #'cut' perameter [p:q] from string
      print (o)
      
      
      d = "".join(map(str, o))                        #list to string
      M=int((d), 2)      
  
      BinC="{0:04b}".format(C)
      print ("C for loop",f, "is:", BinC)
      print ("M for loop",f, "is:", M)
      XORC = (int(M)^int(C))                      # working out XOR between the 4 bits in decimal and the key in decimal
      BinXORC ="{0:04b}".format(XORC)  
      print ("XOR for C is:", BinXORC)
      XORK = (int(XORC)^int(K))                    # working out XOR between the 4 bits in decimal and the key in decimal
      BinXORK="{0:04b}".format(XORK)                    #XOR in decimal to binary at augmentation zero, with four digits
      Rotate=list(str(BinXORK))                         #string to list
      print ("XOR for K is:", BinXORK)
              
      def rotate(lst,x):                          #left rotation 
              copy = list(lst)
              for i in range(len(lst)):
                  if x<0:
                      lst[i+x] = copy[i]
                  else:
                      lst[i] = copy[i-x]
      rotate(Rotate, -1)                          #rotate once to the left is -1
      Rotation = "".join(map(str, Rotate))        #list to string
      print ("After rotation:",Rotation)
      C=int((Rotation), 2)                        #binary to decimal
      print ("Outcome of loop",f,":", C)                                   #C to be used for XOR in next loop
      BinC="{0:004b}".format(C)  
      print ("Binary of C:", BinC)
      print ()
      p=p+4                                       #change perameters to next block
      q=q+4
      f=f+1
      
      print (p)
      print (q)
      print ()

  v=input("Would you like to repeat the cipher block chain encryption? Enter y or n.")
  print ()
  if v == "y":					#if y the program will repeat
    continue
  elif v == "n":				#if n the program will end
    break  