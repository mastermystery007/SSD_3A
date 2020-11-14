import json




class Node:
    id = 0
    nodes = []
    parent = None

    def __init__(self):
        self.id = 0
        self.nodes = []

    def __init__(self,empid):
        self.id = empid
        self.nodes = []
    
    def set_id(self,idp):
        self.id=idp
    
    def set_parent(self,parent):
        self.parent=parent

        


leaders = []

def find_leader(id,root):
    
    if(root==None):
        return False

    if(root.id == id):
        return True
    addMe = False
    for node in root.nodes:
        addMe = addMe or find_leader(id,node)
        if(addMe):
            leaders.append(root.id)  
            return True
    
    return False  
     


def get_Level(root,id,level):
    
    if(root==None):
        return level
    
    if(root.id == id):
        return level+1
    v=0
    for node in root.nodes:
        v=max(v,get_Level(node,id,int(level)+1))
    return v    


def add_child(root,node1,val):
    temp = get_node(val,root)
    temp.nodes.append(node1)    



def get_node(id,root):
    if(root == None):
        return None
    
    if(root.id == id):
        return root

    
    for nodeT in root.nodes:
        temp  =get_node(id,nodeT)
        if(temp!=None):
            return temp
    return None    


input_file=open('org.json', 'r')

json_decode=json.load(input_file)
levels=[]

for item in json_decode:
    levels.append(item)
    if(item == "L0"):
        root = Node(json_decode[item][0]["name"])
       
        continue
        
    
    
    for i in range (0,len(json_decode[item])):
        temp =Node(0)
        for keys in json_decode[item][i]:
            
            if(keys == "name"):
                temp.set_id(json_decode[item][i][keys])
            if(keys == "parent"):
                add_child(root,temp,json_decode[item][i][keys])
                pass
            





number = int(input("No of employees: "))
led = []
allemployees = []

for j in range (0,number):
    ledtemp=[]
    employee=input("Employee name: ")
    allemployees.append(employee)
    find_leader(employee,root)
    #print(leaders)
    appendlist = []
    for leader in leaders:
        #print(leader)
        appendlist.append(leader)
    
    led.append(appendlist)
    leaders.clear()
    
        
    
 
firstlist = led[0]
#print(firstlist)


finallist = led[0]
for i in range (0,len(led)):
    finallist = set(finallist).intersection(led[i])
    #print(finallist)


#print (finallist)

if(len(finallist)==0):
    print("No common  boss")
else:
    leaderfound = False
    
    for leader in firstlist:
        for il in finallist:
            if(leader == il):
                leaderfound = True
                finalleader = leader
                break
        if(leaderfound == True):
            break    
    print ("common leader is: ",end=" ")
    print (finalleader)    
    boss_level = get_Level(root,finalleader,0)
    #print(boss_level)

    allemployeelevels = []
    for employee in allemployees:
        emplevel = get_Level(root,employee,0)
        allemployeelevels.append(emplevel)    
    for i in range (0,len(allemployeelevels)):
        print(str(finalleader)+" is "+str(allemployeelevels[i]-boss_level)+" levels above "+allemployees[i])



"""
for leader in firstlist:
        for interleader in finallist:
            if(interleaders == leader):
 return set(lst1).intersection(lst2)
common_boss_val = 0
flag=1
for i in range (0,len(leaders1)):
    for j in range (0,len(leaders2)):
        if(leaders2[j]==leaders1[i] and flag==1):
            common_boss_val=leaders1[i]
            flag=0
            print("The common boss is "+common_boss_val)   
if(flag==1):
    print("No common boss")                   
#print(leaders1)
#print(leaders2)
intrsctn=(set(leaders1)).intersection(set(leaders2))
#print(intrsctn)
boss_level = get_Level(root,common_boss_val,0)
emp1_level = get_Level(root,employee1,0)
emp2_level = get_Level(root,employee2,0)
if(len(intrsctn)!=0):
    print (str(common_boss_val)+" is "+str(emp1_level-boss_level)+" levels above "+employee1)
    print (str(common_boss_val)+" is "+str(emp2_level-boss_level)+" levels above "+employee2)
"""
