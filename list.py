print("************ methods ***************")

list=[12, "hey", 98, 11]
#index
print(list[1])
print(list[2:3])

#change
list[1]="hello"
print(list)

#insert
list.insert(3,"hey")
print(list)

#append
list.append("employee")
print(list)

# extend =To append elements from another list to the current list, use the extend() metho
tuple=("id",)
list.extend(tuple)
print(list)

#remove specific iteam
list.remove("employee")
print(list)

#pop() method removes the specified index
list.pop()
print(list)

#del keyword also removes the specified index and  also delete the list completely
del list[0]
print(list)
del list
print(list)

#clear() method empties the list
list=[12, "k", "saisri", 7]
list.clear()
print(list)

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


#sort() method that will sort the list alphanumerically, ascending
list=[20,99,88,36,73,22,12]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#capital letters being sorted before lower case letters
list=["true","Yes", "FOR", "apple"]
list.sort()
print(list)

#case-insensitive sort function
list.sort(key=str.lower)
print(list)

#reverse
list.reverse()
print(list)

#copy
mylist=list.copy()
print(list)

#list method
"""b=["3","s",3]
s=list(b)
print(s)"""


#join :to join, or concatenate, two or more lists
l1=["2",3, 7,9]
l2=["4",8,3]
l3=l1+l2
print(l3)

#length
print(len(l1))


