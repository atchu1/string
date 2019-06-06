def isProductEven(arr, n)
for i in range(0, n):
 if ((arr[i] & 1) == 0):  
 return True
 return False
arr = [12,3] 
n = len(arr) 
if (isProductEven(arr, n)): 
    print("Even")  
else: 
    print("Odd")  
