a=input()
k1=k2=0
for i in a:
 if i.isalpha():
 k2+=1
elif i.isnumeric():
 k1+=1
if k1>=1 and k2>=1:
 print('Yes')
else:
    print('No')
