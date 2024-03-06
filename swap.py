def swap(list,pos1,pos2):
    new1=list.pop(pos1)
    new2=list.pop(pos2-1)

    list.insert(pos2,new1)
    list.insert(pos1,new2)
    return list

list=[2,33,41,67,83]
pos1,pos2=2,3
lislen=len(list)
print(lislen)

swap(list,pos1-1,pos2-1)

print("list after swapping is:")
print(list)
