inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A', 'Headset'], ['B', 'Headset']]
# print(inp)
lst = []
lst1=[]
lst2 = []
out1 = []
out2 = []
for i in inp:
    if (i[0] not in lst):
        lst.append(i[0])
        out1.append([i[0], 1])
    else:
        ind = lst.index(i[0])
        out1[ind][1] = out1[ind][1] + 1

    if (i[1] not in lst2):
        lst2.append(i[1])


    if i not in lst1:
        lst1.append(i)
        out2.append([i[0],i[1], 1])
    else:
        ind = lst1.index(i)
        out2[ind][2] = out2[ind][2] + 1
print(out2)
lst.append(lst2)

print(out1)
print(lst)  # out3




A = [1, 2, 3, 'ae']
B = [1, 1, 'b', 6]
C=[]
count=0
for i in range (len(A)):
    if A[i]=='ae':
        A[i]=0
    if B[i]=='b':
        B[i]=0
    x=A[i]+B[i]
    if x%2!=0:
        x=0
    C.append(x)
print(C)
A = [1, 2, 3, 'ae']
B = [1, 1, 'b', 6]
p=A+B
count=0
num=0
ele=0
for i in range (len(p)):
    num=p.count(p[i])
    if (num>count):
        count=num
        ele=i
print(p[ele])


#3


l = [-10, 2, 3, -2, 0, 5, -15]


def calMaxSum(l):
    currsum = 0
    maxsum = 0
    for i in l:
        maxsum = maxsum + i
        maxsum = max(maxsum, 0)
        currsum = max(currsum, maxsum)

    return currsum


print(calMaxSum(l))


from binarytree import build
nodes = [4,7,2,9,6,]

