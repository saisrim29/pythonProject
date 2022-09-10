print("--------------Program 1-------------------")
print(" ------palandrome-----")
print(" ---(---- 1 using for loop ---)--- ")
def palin():
    palindromes=[]
    for count in range(100):
        n = str(count)
        if n == n[::-1]:
            palindromes.append(n)
    return palindromes
p=palin()
print(p)




print("--------------Program 2-------------------")
print(" ------sum 2-digit -----")
def sum(n1, n2):
    sumVal = 0
    print(n1, n2)
    while (n1 != 0 and n2 != 0):
        i = n1 % 10
        j = n2 % 10
        n1 = int(n1 / 10)
        n2 = int(n2 / 10)
        sumVal = sumVal + i + j
    return sumVal

n1 = int(input("Enter number1 :"))  # 1234
n2 = int(input("Enter number2 :"))  # 9999
print(sum(n1, n2))


print("--------------Program 3-------------------")
print(" ------reverse string -----")
string = "ab@cd!ef"
string1 = string[::-1]
string1 = list(string1)
reverse = ''
list = []
for idy, val in enumerate(string1):
    if val.isalpha():
        list.append(val)
    else:
        list.insert(idy, string[idy])
rev_string = reverse.join(list)
print(rev_string)

print("--------------Program 4------------------")
print(" ------dict format-----")
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
sCount={x:some_list.count(x) for x in some_list}
t=dict()
for key, value in sCount.items():
    if value>1:
        t[key]=value

print(t)


print("--------------Program 5------------------")
print(" ------adding or concantetion-----")
def combineList(t1,t2):
    t3 = []
    for i in t1:
        for j in range(len(t2)):
            if(type(i) is type(t2[j])):
                t3.append(i+t2[j])
                t2.remove(t2[j])
                break
    return t3


t1 = [1, 2, 3, "a", "c"]
t2 = ["b", "d", 9, 8, 7]
print(combineList(t1,t2))



print("--------program 6-----------")
print("--- remove leading zeros from an IP address-----")
def ipString(str1):
    str2 = ""
    for i in str1:
        if i != "0":
            str2 = str2+i
    return str2

print(ipString(input("Enter the IP address: ")))
it

print("--------program 7-----------")
print("--- remove leading zeros from an IP address-----")

def singleList(l1):
    l2 = []
    for i in l1:
        if type(i) is list:
            l2.extend(singleList(i))
        else:
            l2.append(i)
    return l2


l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(singleList(l))