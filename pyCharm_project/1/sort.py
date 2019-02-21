list = [34,564,2,35,35,62,67]
def mysort(list):
    newList = []
    for number in range(0,len(list)):
        newList.append(min(list))
        list.remove(min(list))
    return newList
print(mysort(list))
list.pop()