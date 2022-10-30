import random
from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


#Sex
sexs=["Female", "Male"]
sex=random.randint(0,len(sexs)-1)

#First name
if sex==0:
    FirstNameFile = open("name-female.txt", "r", encoding='utf-8')
elif sex==1:
    FirstNameFile = open("name-male.txt", "r")
FirstNameList=FirstNameFile.readlines()
FirstNamesLen=len(FirstNameList)
FirstName=FirstNameList[random.randint(0, FirstNamesLen)].rstrip()

#Last name
LastNameFile = open("lastNames.txt", "r", encoding='utf-8')
LastNameList=LastNameFile.readlines()
LastNamesLen=len(LastNameList)
LastName=LastNameList[random.randint(0, LastNamesLen)].lower().capitalize().rstrip()

#Birthday
MonthList={'January':[31, 1], 'February':[28, 2], 'March':[31, 3], 'April':[30, 4], 'May':[31, 5], 'June':[30, 6], 'July':[31, 7],
        'August':[31, 8], 'September':[30, 9], 'October':[31, 10], 'November':[30, 11], 'December':[31, 12]}
Month=random.choice(list(MonthList))
Day=random.randint(1, MonthList[Month][0])
CurrentYear=date.today().year
Year=CurrentYear-random.randint(21, 63)

#Age
Age=age(date(Year, MonthList[Month][1], Day))

#Mail
Voyelles=["a","e","i","o","u","y"]

PrefixChoice=random.randint(1,2)
if PrefixChoice==1:
    Prefix=FirstName[:3]
    for c in range(3,len(FirstName)):
        if Prefix[-1] not in Voyelles:
            Prefix+=FirstName[c]
        else:
            break
else:
    Prefix=FirstName
    
SuffixChoice=random.randint(1,2)
if SuffixChoice==1:
    SuffixNumbersLen=random.randint(2,3)
    Suffix=LastName.lower()
    for x in range(SuffixNumbersLen):
        Suffix+=str(random.randint(0,9))
else:
    Suffix=LastName.lower()
    
Prefix=Prefix.lower()
Mail=Prefix+"."+Suffix+"@gmail.com"


print("Sex: "+sexs[sex])
print("Birthday: "+str(Day), str(Month), str(Year))
print("Age: "+str(Age))
print("First name: "+FirstName)
print("Last name: "+LastName)
print("Mail: "+Mail)