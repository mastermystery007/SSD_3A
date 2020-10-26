import json




class Node:
    id = 0
    nodes = []
    parent = None
    def __init__(self,empid):
        self.id = empid
        self.nodes = []
    def set_id(self,id):
        self.id=id
    
    def set_parent(self,parent):
        self.parent=parent

        


leaders1 = []
leaders2 = []
def find_leader(id,root):
    
    if(root==None):
        return False

    if(root.id == id):
        return True
    addMe = False
    for node in root.nodes:
        addMe = addMe or find_leader(id,node)
        if(addMe):
            leaders1.append(root.id)  
            return True
    
    return False  


def get_Level(root,id,level):
    
    if(root==None):
        return level
    
    if(root.id == id):
        return level+1

    return get_Level(root)





def find_leader_2(id,root):
    
    if(root==None):
        return False

    if(root.id == id):
        return True
    addMe = False
    for node in root.nodes:
        addMe = addMe or find_leader_2(id,node)
        if(addMe):
            leaders2.append(root.id)  
            return True
    
    return False  



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


input_file=open('boss.json', 'r')

json_decode=json.load(input_file)
levels=[]
root = Node(1) 
for item in json_decode:
    levels.append(item)
    print (item)
    temp =Node()
    for keys in json_decode[item][0]:
        print(keys,end=" ")
        if(keys == "name"):
            temp.set_id(json_decode[item][0][keys])
        if(keys == "parent"):
            add_child(root,json_decode[item][0][keys],temp)
            pass
        print(json_decode[item][0][keys])


"""
root = Node(1) 
node0 = get_node(1,root)

add_child(root,Node(2),1)
add_child(root,Node(11),1)
add_child(root,Node(12),1)
add_child(root,Node(22),1)
add_child(root,Node(3),2)
add_child(root,Node(4),3)
add_child(root,Node(7),4)
add_child(root,Node(9),7)
add_child(root,Node(11),7)

find_leader_2(11,root)
print(leaders2)"""
"""
node1 = get_node(2,root)
node1.nodes.append(Node(6))
node1.nodes.append(Node(5))
node2 = get_node(5,root)
add_child(node2,Node(10))
add_child(node2,Node(9))
find_leader(4,root)
find_leader_2(9,root)
print(leaders1)
print(leaders2)"""

"""root.left.nodes.append(Node(4)) 
root.left.nodes.append(Node(5)) 
root.right.nodes.append(Node(6)) 
root.right.nodes.append(Node(7))"""
#get_Leaders_1(5,root)
#get_Leaders_1(2,root)

"""
leaders1=[]
def get_Leaders_1(id1,root):
    if root is None: 
        return False

    if(root.id == id1):
        return True
    if(get_Leaders_1(id1,root.left) or get_Leaders_1(id1,root.right)):
        leaders1.append(root.id)
        return True

leaders2=[]
def get_Leaders_2(id2,root):
    if root is None: 
        return False

    if(root.id == id2):
        return True
    if(get_Leaders_2(id2,root.left) or get_Leaders_2(id2,root.right)):
        leaders2.append(root.id)
        return True



nodeX.left = Node(9)
nodeX.right = Node(10)
nodeY = find_node(10,root)
print(nodeX.id)







	def dfs(self,key,root):
		if len(root.child)==0:
			return 
		for nde in root.child:
			if nde.val==key:
				return ([])
			else:
				fnd=self.dfs(key,nde)
				if isinstance(fnd,list):
					fnd.append(nde.val)
					return fnd
			
		return fnd
"""
#get_Leaders_1(10,root)


#print (leaders1)
