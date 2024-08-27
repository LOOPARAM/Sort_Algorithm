import random
import time

def random_data(len,start,end):
    data = []
    for i in range(0,len):
        data.append(random.randint(start,end))
    return data

def insertion_sort(data):
    for i in range(1,len(data)):
        print(data,i)
        for j in range(i-1,0-1,-1):
            if(data[j+1] < data[j]):
                data[j+1], data[j] = data[j], data[j+1]
    return data

# data = [15,11,1,3,8]
# data = random_data(10,1,30)
data = [37,2,8,16,11,25,19,45,33,22]
print(data)
print(insertion_sort(data))