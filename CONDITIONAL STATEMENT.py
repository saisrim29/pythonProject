# IF
n=10
a=10
if n==a:
    print(a)

#IF ELSE
year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print("is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("is a leap year".format(year))
else:
    print("is not a leap year".format(year))

# IF ELIF ELSE
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print("fuzzy buzzy")
    elif i%3==0:
        print("fuzzy")
    elif i%5==0:
        print("buzzy")
    else:
        print(i)


# Nested IF
mark = int(input("mark is:"))

if 0 <= mark <= 100:
    print("valid mark")
    if mark >= 50:
        print("Result is Pass")
        if 90 < mark < 100:
            print("Grade is : S")
        if 80 < mark < 90:
            print("Grade is : A")
        if 70 < mark < 80:
            print("Grade is : B")
        if 60 < mark < 70:
            print("Grade is : C")
        if 50 < mark < 60:
            print("Grade is : D")
        if mark == 50:
            print("Grade is : E")

    else:
        print("result is Fail")
        print("Grade is : F")
else:
    print("enter valid marks")