# Appending to an item in a tuple
a_tuple = (1, 2, [1, 2, 3])
a_tuple[2].append(4)
print(a_tuple)
#change
t=("saisri", 8, "5", 7)
l=list(t)
l[2]="0"
t=tuple(l)
print(t)
#