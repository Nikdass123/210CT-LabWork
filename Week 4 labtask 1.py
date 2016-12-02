def binsearch(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if target<list[midpoint]:
               return binsearch(list[:midpoint],target)# checks the target in left side of list
            else:
                return binsearch(list[midpoint+1:],target)#checks the target in right side of list

list = [2,3,4,8,10,19,23,25,30]
print binsearch(list,10)
