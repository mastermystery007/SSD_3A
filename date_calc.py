import re


class Date:
    
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y



"""
def get_Year_Diff(y1,y2):
    if(y1>y2):
        return ((int(y1)-int(y2))*365)
    else:
        return ((int(y2)-int(y1))*365)    
"""

def get_Total_Days(date):
    year = int(date.y)
    month = int(date.m)
    day = int(date.d)

    year2=year-1

    total_days = 0 
    leap_years = int(year2/4) - int(year2/100) + int(year2/400)
    
    total_days = (leap_years*366) + ((year-leap_years-1)*365)+this_Years_Days(date)
    #print ("total days are: "+str(total_days))
    return total_days


def this_Years_Days(date):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if(check_Leap_Year(date.y)):
        monthDays[1]=29
    monthitr= int(date.m)
    monthitr = monthitr-1
    for i in range (0,monthitr):
        days = days + monthDays[i]
    days = days + int(date.d)
    #print (" days"+str(days))
    return days    

def total_Diff(date1,date2):
    days_1 = get_Total_Days(date1)
    days_2 = get_Total_Days(date2)
    
   # print("days 1 is"+str(days_1))
    #print("days 2 is"+str(days_2))

    print ("The differnce is "+str(int(days_1)-int(days_2)))

def check_Leap_Year(year):
    if ((int(year) % 4 == 0 ) and ((int(year) % 100) != 0 or (int(year) % 400) == 0)):
        return True
    else:
        return False



lines=[]
f1 = open("date_input.txt", "r")
for line in f1.readlines():
    lines.append(line)
#date1 = input("Enter First Date : ")
x = re.search("^Date1: ([1-9]|0[0-9]|1[0-9]|2[0-9]|3[0-1])(.|-|/|th|rd|st|nd)([1-9]|0[0-9]|1[0-2]|January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(.|-|,|/|)([0-9][0-9][0-9][0-9])$", lines[0])
#date2=input("Enter Second Date : ")
y = re.search("^Date2: ([1-9]|0[0-9]|1[0-9]|2[0-9]|3[0-1])(.|-|/|th|rd|st|nd)([1-9]|0[0-9]|1[0-2]|January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(.|-|,|/|)([0-9][0-9][0-9][0-9])$", lines[1])
day1 = (x.group(1))
month1 = (x.group(3))

if(month1=="January" or month1=="Jan"):
    month1="01"
if(month1=="February" or month1=="Feb"):
    month1="02"
if(month1=="March" or month1=="Mar"):
    month1="03"
if(month1=="April" or month1=="Apr"):
    month1="04"
if(month1=="May" ):   
    month1="05"     
if(month1=="June" or month1=="Jun"): 
    month1="06"   
if(month1=="July" or month1=="Jul"):
    month1="07"
if(month1=="August" or month1=="Aug"):
    month1="08"
if(month1=="September" or month1=="Sep"):  
    month1="09"          
if(month1=="October" or month1=="Oct"):
    month1="10"
if(month1=="November" or month1=="Nov"):
    month1="11"
if(month1=="December" or month1=="Dec"):     
    month1="12" 
      
year1 = (x.group(5))
dt1 = Date(day1, month1, year1)

day2 = (y.group(1))
month2 = (y.group(3))

if(month2=="January" or month2=="Jan"):
    month2="01"
if(month2=="February" or month2=="Feb"):
    month2="02"
if(month2=="March" or month2=="Mar"):
    month2="03"
if(month2=="April" or month2=="Apr"):
    month2="04"
if(month2=="May" ):   
    month2="05"     
if(month2=="June" or month2=="Jun"): 
    month2="06"   
if(month2=="July" or month2=="Jul"):
    month2="07"
if(month2=="August" or month2=="Aug"):
    month2="08"
if(month2=="September" or month2=="Sep"):  
    month2="09"          
if(month2=="October" or month2=="Oct"):
    month2="10"
if(month2=="November" or month2=="Nov"):
    month2="11"
if(month2=="December" or month2=="Dec"):     
    month2="12"

year2 =(y.group(5))
dt2 = Date(day2,month2,year2) 


total_Diff(dt1,dt2)
