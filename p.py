l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print("odd:", l1[1:7:2])
print("even:", l2[0:7:2])
l3=l1[1:7:2]
l4=l2[0:7:2]
l5=l3+l4
print(l5)

list1 = [54, 44, 27, 79, 91, 41]
list1.pop(4)
print("removing the element at index 4:", list1 )
list1.insert(2, 11)
print("inserting the element at index 2:", list1 )
list1.append(11)
print("adding the element :", list1 )

""" Get the length of a list using a len() function
Divide the length by 3 to get the chunk size
Run loop three times
In each iteration, get a chunk using a slice(start, end, step) function and reverse it using the reversed() function
In each iteration, start and end value will change """





sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l1=sample_list[::-1]
print(l1)
print(l1[0:3])
print(l1[3:6])
print(l1[6:9])

