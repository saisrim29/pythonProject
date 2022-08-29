x=" hello world "
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("h","j"))
print(x.split(' '))
print("****************************** concatenation *****************************")
c="hey"
s=x+" "+x
print(s)
print("******************** format=combine strings and numbers by using the format() method! ****************")
name=" employed id is {} and contact number is {}"
id=457
contnum=123456789
print(name.format(id,contnum))
print("****************** escape character is a backslash \ followed by the character you want to insert ***********")
txt="hey this is \"saisri\" from telangana"
print(txt)
print("that\'s it")
print("avg=sum\\num")
print("first_name=saisri\nlast name=M")
print("first\rlast")
print("first\tlast")
print("back \bspace")
print("\123\123\131\132")
print("\x48\x65\x6c\x6c\x6f")

#capitalize()	Converts the first character to upper case
x=txt.capitalize()
print(x)

#casefold()	Converts string into lower case
print(x)

#center()	Returns a centered string
print(x)

#count()	Returns the number of times a specified value occurs in a string
x="saisri"
y=x.count(x)
print(y)

#encode()	Returns an encoded version of the string

#endswith()	Returns true if the string ends with the specified value
x="hello this is saisri."
y=x.endswith(".")

#expandtabs()	Sets the tab size of the string
x="s\ta\ti\ts\tr\ti"
z=x.expandtabs(3)
print(z)

#find()	Searches the string for a specified value and returns the position of where it was found
x= "welocome to python class"
p=x.find("to")
print(p)

#format()	Formats specified values in a string
x="the price of icecream is {}"
l=x.format("100")
print(l)
#format_map()	Formats specified values in a string

#index()	Searches the string for a specified value and returns the position of where it was found
x= "my phone is out of battery"
print(x.index("out"))

#isalnum()	Returns True if all characters in the string are alphanumeric
x="saisri 15"
print(x.isalpha())

#isalpha()	Returns True if all characters in the string are in the alphabet
x="saisri 15"
print(x.isalpha())

#isdecimal()	Returns True if all characters in the string are decimals
x="pi value is 3.14"
print(x.isdecimal())

#isdigit()	Returns True if all characters in the string are digits
x="56"
print(x.isdigit())

#isidentifier()	Returns True if the string is an identifier
x="demo"
print(x.isidentifier())

#islower()	Returns True if all characters in the string are lower case
x=" iam at office"
print(x.islower())

#isnumeric()	Returns True if all characters in the string are numeric
x="26788"
print(x.isnumeric())

#isprintable()	Returns True if all characters in the string are printable
x=" hey \n you"
print(x.isprintable())

#isspace()	Returns True if all characters in the string are whitespaces
x="hi everyone"
print(x.isspace())

#istitle()	Returns True if the string follows the rules of a title
x="Hi Everyone"
print(x.istitle())

#isupper()	Returns True if all characters in the string are upper case
x="SAISRI"
print(x.isupper())

#join()	Joins the elements of an iterable to the end of the string
t=("hey", "would", "you", "like", "have", "some","tea")
x="@".join(t)
print(x)

#ljust()	Returns a left justified version of the string
t="hey"
x=t.ljust(12)
print(x)

#lower()	Converts a string into lower case
x="welcome to home"
print(x.lower())

#lstrip()	Returns a left trim version of the string
x="   vn2  "
print(x.lstrip())

#maketrans()	Returns a translation table to be used in translations
x="hi leo"
r=x.maketrans("l", "r")
print(r)

#partition()	Returns a tuple where the string is parted into three parts
x="i would like eat dark chocolates and icecream , especially  chocolate icecream is my favourite "
w=x.partition("icecream")
print(w)

#replace()	Returns a string where a specified value is replaced with a specified value
x="i am saisri"
d=x.replace("saisri","leo")
print(d)

#rfind()	Searches the string for a specified value and returns the last position of where it was found
x= "welocome to python class"
z=x.find("to")
print(z)

#rindex()	Searches the string for a specified value and returns the last position of where it was found
x= "my phone is out of battery"
print(x.index("out"))

#rjust()	Returns a right justified version of the string
t="hey"
x=t.ljust(12)
print(x)

#rpartition()	Returns a tuple where the string is parted into three parts
x="i would like eat dark chocolates and icecream , especially  chocolate icecream is my favourite "
h=x.partition("icecream")
print(h)

#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
x="   vn2  "
print(x.lstrip())

#split()	Splits the string at the specified separator, and returns a list
x=" welcome to python"
print(x.split())

#splitlines()	Splits the string at line breaks and returns a list
x="i am saisri \n iam from hyderabad"
o=x.splitlines()
print(o)

#startswith()	Returns true if the string starts with the specified value
x="@ welcome to python"
print(x.startswith("@"))

#strip()	Returns a trimmed version of the string
x = "   vn2  "
print(x.lstrip())

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
x="i am SAISRI"
print(x.swapcase())

#title()	Converts the first character of each word to upper case
x="i am SAISRI"
print(x.title())

#translate()	Returns a translated string
dic={65:86}
txt=" apple is good for health"
print(txt.translate(dic))
#upper()	Converts a string into upper case
x="apple"
print(x.upper())

#zfill()	Fills the string with a specified number of 0 values at the beginning  "
txt = "50"

x = txt.zfill(10)

print(x)

