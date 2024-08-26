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

def merge_sort(data):
    sub_data1 = []
    sub_data2 = []
    result = []

    if(len(data) == 2):
        if(data[0]>data[1]):
            data[0],data[1] = data[1],data[0]
        return data
    else:
        if(len(data)%2 == 0):
            sub_data1 = merge_sort(data[0:len(data)//2])
            sub_data2 = merge_sort(data[(len(data)//2):len(data)])
            print(sub_data1,sub_data2)

            pointer = 0
            pointer1 = 0
            while(len(result)<=len(sub_data1+sub_data2)):
                print("result",result,pointer,pointer1)
                if(pointer1 == len(sub_data1)):
                    ???
                if(sub_data1[pointer] > sub_data2[pointer1]):
                    result.append(sub_data2[pointer1])
                    pointer1+=1
                else:
                    result.append(sub_data1[pointer])
                    pointer+=1
                time.sleep(1)
                    
        else:
            sub_data1 = merge_sort(data[0:(len(data)+1)//2])
            sub_data2 = merge_sort(data[((len(data)+1)//2):len(data)])

    return result

        

# data = random_data(10,1,30)
data = [43,38,82,19,57,26,64,71]
print(data)
print(merge_sort(data))