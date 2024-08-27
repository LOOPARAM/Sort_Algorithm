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

def split_data(data):
    sub_data1 = []
    sub_data2 = []

    if(len(data)%2 == 0):
        sub_data1 = (data[0:len(data)//2])
        sub_data2 = (data[(len(data)//2):len(data)])
    else:
        sub_data1 = (data[0:(len(data)+1)//2])
        sub_data2 = (data[((len(data)+1)//2):len(data)])
    print(data,"나누기->",sub_data1,sub_data2)
    return sub_data1,sub_data2

def sort(data1,data2):
    result = []
    p1 = 0
    p2 = 0
    for i in range(0,(len(data1)*2)):
        if(p1==len(data1)):
            for j in range(p2,len(data2)):
                result.append(data2[j])
            return result
        if(p2==len(data2)):
            for j in range(p1,len(data1)):
                result.append(data1[j])
            return result

        if(data1[p1] < data2[p2]):
            result.append(data1[p1])
            p1 += 1
        else:
            result.append(data2[p2])
            p2 += 1
        # print(result,p1,p2)
    return result

def merge_sort(data):
    if(len(data) == 1):
        return data
    sub_data1 = merge_sort(split_data(data)[0])
    sub_data2 = merge_sort(split_data(data)[1])
    result = sort(sub_data1,sub_data2)
    print("정렬->",result)

    return result

# data = random_data(10,1,30)
data = [37,2,8,16,11,25,19,45,33,22]
print(" start data : ",data)
print("result data : ",merge_sort(data))