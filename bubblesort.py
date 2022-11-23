import random
list=[]
for i in range(10):
    list.append(random.randrange(0,50))

print(list)

def bubblesort(list):
    for i in range(len(list)):
        for a in range(len(list)-1):
            if list[a]>list[a+1]:
                list[a], list[a+1]=list[a+1], list[a]
    return list
print(bubblesort(list))