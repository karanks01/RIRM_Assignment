N = int(input("Enter a Number : "))

if N > 1:
   for i in range(2, N):
       if (N % i) == 0:
           print("false")
           break
   else:
       print("true")
else:
   print("false") 
