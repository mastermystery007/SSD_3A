import json
import re
import datetime  
from datetime import timedelta
from datetime import time

class Time:
    def __init__(self, hrs, mins,phase):
        self.hrs = hrs
        self.mins = mins
        self.phase = phase


def sanitize_time(time):
    total_mins=0
    if(time.phase == "AM"):
        total_mins=total_mins+(int(time.hrs) - 9)*60
        total_mins=total_mins+(int(time.mins))
    elif(time.phase == "PM"):
        total_mins=total_mins+(int(time.hrs) + 3)*60
        total_mins=total_mins+(int(time.mins))
    return total_mins    


def fill_empty(filled_slots):
    empty_slots = [] 
    if(filled_slots[0][0].hrs=="9" and filled_slots[0][0].mins=="00"):
        pass
    else:
        temp = Time("9","00","AM")
        empty_slots.append([temp,filled_slots[0][0]])   

    for i in range (0,len(filled_slots)-1):
        
        if(not((filled_slots[i][1].hrs == filled_slots[i+1][0].hrs) and(filled_slots[i][1].mins == filled_slots[i+1][0].mins))):
            if(filled_slots[i][1].hrs=="12"):
                temp1 = Time(filled_slots[i][1].hrs ,filled_slots[i][1].mins ,"PM")
            else:
                temp1 = Time(filled_slots[i][1].hrs ,filled_slots[i][1].mins ,filled_slots[i][1].phase)

            if(filled_slots[i+1][0].hrs=="12"):
                temp2 = Time(filled_slots[i+1][0].hrs ,filled_slots[i+1][0].mins ,"PM")
            else:
                temp2 = Time(filled_slots[i+1][0].hrs ,filled_slots[i+1][0].mins ,filled_slots[i+1][0].phase)    

            empty_slots.append([temp1,temp2]) 
               

    if(filled_slots[len(filled_slots)-1][1].hrs=="5" and filled_slots[len(filled_slots)-1][1].mins=="00"):
        pass
    else:
        temp = Time("5","00","PM")
        empty_slots.append([filled_slots[len(filled_slots)-1][1],temp])  

    return empty_slots

def fill_time_1(t1,t2):
    t1o = sanitize_time(t1)
    t2o = sanitize_time(t2)
    for i in range (t1o,t2o):
        buckets1[i]=1

def fill_time_2(t1,t2):
    t1o = sanitize_time(t1)
    t2o = sanitize_time(t2)
    for i in range (t1o,t2o):
        buckets2[i]=1    

def rev_sanitize(mins):
    h = mins/60
    rm = mins%60
    if (rm == 0):
        rm="00"
    
    
    if(h>=3):
        tt = Time(int(9+h),rm,"PM")
    else:
        tt = Time(int(9+h),rm,"AM")    
    
    
    return tt



def get_common(duration,a1,a2):
    cntr=0
    index=0
    for i in range (0,480):
        if(a1[i]==0 and a2[i]==0):
            cntr=cntr+1
            if(cntr==duration):
                index = i-cntr
                break
        else:
            cntr=0
    
    if(cntr < duration ):
        print ("No slot available")
        return None
    else:
        t = rev_sanitize(index+1)
        p = rev_sanitize(index+duration+1)
        strp=""
        strp+=str(t.hrs)+":"+str(t.mins)+str(t.phase)+" "+"-"+" "+str(p.hrs)+":"+str(p.mins)+str(p.phase)
        
        return strp

    


f1 = open("e1.txt", "r")
line1 = f1.readline()
f2 = open("e2.txt", "r")
line2 = f2.readline()


obj1 = eval ("(" + line1 + ")");
obj2 = eval ("(" + line2 + ")");

a = (obj1['Employee1'].keys())
b = (obj2['Employee2'].keys())

for key1 in a :
    date1 = key1
for key2 in b :
    date2 = key2    

access1 = obj1['Employee1'][date1]
access2 = obj2['Employee2'][date2] 

time1=[]
buckets1 = [0] * 480  # 480 mins  = 8 hrs 
time2=[]
buckets2 = [0] * 480
for item in access1:
    item = item.replace(" ", "")
    x = re.search("^(1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])(-)(1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])$", item)
    
    t1 = Time(x.group(1),x.group(2),x.group(3))
    if(t1.hrs=="12"):
        t1.phase="AM"
        
    t2 = Time(x.group(5),x.group(6),x.group(7))
    if(t2.hrs=="12"):
        t2.phase="AM"
    
    time1.append([t1,t2])
    
    fill_time_1(t1,t2)


for item in access2:
    item = item.replace(" ", "")
    x = re.search("^(1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])(-)(1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])$", item)
    
    t1 = Time(x.group(1),x.group(2),x.group(3))
    if(t1.hrs=="12"):
        t1.phase="AM"
        
    t2 = Time(x.group(5),x.group(6),x.group(7))
    if(t2.hrs=="12"):
        t2.phase="AM"
    
    time2.append([t1,t2])
    
    fill_time_2(t1,t2)    

cnt2=0
cnt1=0
for i in range (0,480):
    if(buckets2[i]==1):
        cnt2=cnt2+1
    if(buckets1[i]==1):
        cnt1=cnt1+1

empty1 = fill_empty(time1)

empty2 = fill_empty(time2)
str1 = ""
str2 = ""
for i in range (0,len(empty1)):
    str1+="'"+empty1[i][0].hrs+":"+empty1[i][0].mins+" "+empty1[i][0].phase+" - "+empty1[i][1].hrs+":"+empty1[i][1].mins+" "+empty1[i][1].phase+"'"+","

for i in range (0,len(empty2)):
    str2+="'"+empty2[i][0].hrs+":"+empty2[i][0].mins+" "+empty2[i][0].phase+" - "+empty2[i][1].hrs+":"+empty2[i][1].mins+" "+empty2[i][1].phase+"'"+","
     

print (str1)
print (str2)    
time = input("Enter slot duration in hours : ")
strh = get_common(int(float(time)*60),buckets1,buckets2)
print (strh)   
file1write = open("MyFile.txt","a")

file1write.write("Available slot \n")
file1write.write("Employee1: [")
file1write.write(str1)
file1write.write("]")
file1write.write("\n") 
file1write.write("Employee2: [")
file1write.write(str2)
file1write.write("]")
file1write.write("\n") 

file1write.write("\n") 
file1write.write("Slot duration "+time+" hour")
file1write.write("{'"+date1+"':["+strh+"']}")

#file1write.write(strh)
file1write.close() 

#"""
#t1 = Time(9,30,"AM") 
#t2 = Time(10,30,"AM") 
#t1f = sanitize_time(t1)
#t2f = sanitize_time(t2)

#if(t1f>t2f):
#    arr = fill_time(t2f,t1f)
#else:
#    arr= fill_time(t1f,t2f)


#print(arr)
