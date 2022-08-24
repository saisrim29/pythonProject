"""4. Get employee details(in dict format, empid,name,sal, exp) and update hike for employee with below
		If exp is 0 to 2 years - 10% Hike
				  2 to 5 years - 20% Hike
				  5 to 8 years - 30% Hike
				  8+           - No hike  """

emp = {
    "emp_id" : 431,
    "name": "Navneeta Sinha",
    "sal" : 45000,
    "exp" : 1
}
if emp["exp"] >= 0 and emp["exp"] <= 2:
    emp["sal"] += emp["sal"] * 0.1
elif emp["exp"] > 2 and emp["exp"] <= 5:
    emp["sal"] += emp["sal"] * 0.2
elif emp["exp"] > 5 and emp["exp"] <= 8:
    emp["sal"] += emp["sal"] * 0.3
else :
    print("No Hike")
print(emp["sal"])

""" 3. Prepare Programs for below questions
	1. Prepare state and assign North South West East 
	    north = []
		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
		west = []
		east = []
	2. Prepare dictionary with key as state name and value as "list of districts """

north=['Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Uttarakhand']
south=['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
west=['RAJASTHAN', 'MADHYA PRADESH', 'KARNATAKA' ]
east=['Bihar', 'Jharkhand', 'Orissa', 'West Bengal']
print("north:", north, "south:", south, "west:" ,west, "east:", east)

thisd={'AP':['a','b','c'],'Kerala':['d','e','f'],'karnataka':['g','h','i']}
print(thisd)

