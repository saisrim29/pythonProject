number=int(input())
num=number
rev=0
while num>0:
    last=num%10
    rev=rev*10+last
    num=int(num/10)

if rev==number:
    print("palindorm:")
else:
    print("not a palindrom")


