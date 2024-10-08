import random
import time
import sys

recursion_limit = sys.getrecursionlimit()
sys.setrecursionlimit(100000)

def random_data(len,start,end):
    data = []
    for i in range(0,len):
        data.append(random.randint(start,end))
    return data

def quick_sort(data):
    pivot = 0
    large = 0
    small = len(data)-1
    result = []

    if(len(data)<=1):
        return data
    
    while True:   
        while data[pivot] < data[small]:
            small -= 1
        while data[pivot] >= data[large]:
            large += 1
            if(large == len(data)-1):
                data[pivot],data[small] = data[small],data[pivot]
                print("나누기!",data[0:small],data[small],data[small+1:len(data)])
                if(len(data)==2):
                    return data
                # print(data[0:small],data[small+1:len(data)])
                data1 = quick_sort(data[0:small])
                data2 = quick_sort(data[small+1:len(data)])
                print("합치기!",data1+[data[small]]+data2)
                return data1+[data[small]]+data2

        if(large > small):
            data[pivot],data[small] = data[small],data[pivot]
            print("나누기!",data[small],data)
            if(len(data)==2):
                return data
            # print(data[0:small],data[small+1:len(data)])
            data1 = quick_sort(data[0:small])
            data2 = quick_sort(data[small+1:len(data)])
            return data1+[data[small]]+data2
        else:
            data[large],data[small] = data[small],data[large]
            print("바꾸기!",data)
        # print(data)
        # time.sleep(1)

def quick_sort2(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    print(left,"/",pivot,"/",right)
    return quick_sort2(left) + [pivot] + quick_sort2(right)

# data = random_data(50,1,50)
data = [37,2,8,16,11,25,19,45,33,22]
# data = [5,3,6,1,2,4,7]
print(" start data : ",data)
print("result data : ",quick_sort(data))