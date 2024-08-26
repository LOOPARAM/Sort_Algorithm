import random
import time

def random_data(len,start,end):
    data = []
    for i in range(0,len):
        data.append(random.randint(start,end))
    return data

def bubble_sort(data):
    count = 1
    while count >= 1:
        count = 0
        print(data)
        for i in range(1,len(data)):
            if(data[i-1]>data[i]):
                data[i],data[i-1] = data[i-1],data[i]
                count += 1

# data = random_data(10,1,30)
data = [15,11,1,3,8]
print(data)
print(bubble_sort(data))