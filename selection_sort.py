import random
import time

def random_data(len,start,end):
    data = []
    for i in range(0,len):
        data.append(random.randint(start,end))
    return data

def selection_sort(data):
    min = data[0]
    pointer = 0
    min_pointer = 0
    loop = True
    check = 0
    while loop:
        # print(data,pointer)
        
        min = data[pointer]
        min_pointer = pointer
        for i in range(pointer, len(data)):
            if(min >= data[i]):
                min = data[i]
                min_pointer = i

        data[min_pointer] = data[pointer]
        data[pointer] = min
        
        if(pointer == len(data)-1):
            pointer = 0
            check = 0
            for i in range(1,len(data)):
                if(data[i] - data[i-1] >= 0):
                    check += 1
            if(check == len(data)-1):
                loop = False

        else:
            pointer += 1
        # time.sleep(1)
    return data

def selection_sort2(data):
    min = data[0]
    pointer = 0
    min_pointer = 0
    for i in range(0,len(data)):
        min = data[pointer]
        min_pointer = pointer
        for i in range(pointer, len(data)):
            if(min >= data[i]):
                min = data[i]
                min_pointer = i
        data[min_pointer] = data[pointer]
        data[pointer] = min
        pointer += 1
    return data

def selection_sort3(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


# print(random_data(4,1,2)) #길이4, 1~2 정수 뽑기
data = random_data(30000,1,30)
# data = [15,11,1,3,8]
print(data)
print(selection_sort3(data))