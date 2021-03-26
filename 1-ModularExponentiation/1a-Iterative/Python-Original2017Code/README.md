For this task, an iterative algorithm was used to find the outcome of the phrase “a^b mod c” using the following method:

f	a	d	c	e
1	13	1	53	13
2	13	13	53	10
3	13	10	53	24
4	13	24	53	47
0	13	47	53	28
6	13	28	53	46
7	13	46	53	15
8	13	15	53	36
9	13	36	53	44
10	13	44	53	42
11	13	42	53	46

When: 		
```
f= current loop number
b= number of loops 
e = a * d % c 		
		d=e
		f=f+1	
```

As you can see above “d” starts off as 1 on the first loop and then is rewritten as e at the end of the first loop by implementing “d=e” at the end of the for loop. This method can be used for larger numbers than the following algorithm:

Solution =1
NextPow=1
Loop from NextPow= 1 to b 
Increment Next Pow
Solution = (a* Solution) Mod c        
End loop

The program was created in Python 3.5.2. To create the program, I first set all variables to zero other than “d” and f as d needs to be zero for the first loop and will then be replaced with “e”- the output. “f” will be set to 1 as “f” will be used in showing the outcome as it will be the NextPower variable.  

There are then three input prompts for “a”, “b” and “c”. There is a checker to check that the inputs are integers using a while loop. The syntax is shown before and would be repeated three times for the three inputs. 

To begin the recursive loop “for x in range 1,b+1” is used, input b which is to the power of “a” is being used to set the number of times the program will run. If “b” is eleven then in the first loop “f” will be 1, in the second loop “f” will be 2, all the way to the last loop when “f” will be eleven. Within the loop is the function explained above whereby the outcome of each loop becomes the d for the next loop, in the example above it starts as 1 as it is set to 1, and ends up at 42 at the end of the eleven loops. 