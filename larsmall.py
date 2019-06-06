List = []
Number = int(input("Enter  the Total Number of List Elements:"))
for i in range(1, Number + 1):
 value = int(input("Please enter the Value of %d Element :"%i))
List.append(value)
print("The Smallest Element in  List is :", min(List))
print("The Largest Element in List is : ", max(List))
