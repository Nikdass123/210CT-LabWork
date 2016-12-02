import random 

def randomshuff(list):
	list = []
	for i in range(9):
		x = random.randint(0,20)# this randomly generates shuffled list
		list.append(x)
	return list
	

print randomshuff(list)    
