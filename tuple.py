# Appending to an item in a tuple
a_tuple = (1, 2, [1, 2, 3])
a_tuple[2].append(4)
print(a_tuple)


#change


#append()
t=("saisri", 8, "5", 7)
l=list(t)
l[2]="0"
t=tuple(l)
print(t)

#tuple+tuple
tuple2=("3", 3,7,9,73)
tuple1=("f",7,4,9,9)
tuple2+=tuple1
print(tuple2)

#remove
tuple2=("3", 3,7,9,73)
t=list(tuple2)
t.remove(3)
tuple2=tuple(t)
print(tuple2)

#del
tuple3=("3", 3,7,9,73)
del tuple3
print(tuple3)

#we are also allowed to extract the values back into variables. This is called "unpacking
t=("9", 2,4,8)
("s",5,8,9)=t
print("s")




