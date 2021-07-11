def bubble_sort(data):
    length = len(data)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp


    # for i in range
    

data_list = [8, 15, 3, 5, 2]
ll = bubble_sort(data_list)
print(data_list)
