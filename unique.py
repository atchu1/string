def sublist_duplicates(lst):
sublists= []
 for item in set(lst):
 if (lst.count(item)>=2):
 return item
 return "unique"
dummy = input()
lst_of_duplicates = [int(x) for x in input().split()]
print(sublist_duplicates(lst_of_duplicates))
