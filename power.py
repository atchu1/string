def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
    return True
test_no = 8
if(isPowerOfTwo(8)): 
    print( 'Yes') 
else: 
    print('No') 
  
