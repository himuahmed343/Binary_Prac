def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        item = data[i]
        j = i - 1
        while j>=0 and data[j] < item:
            # temp = data[j]
            # data[j] = data[j + 1]
            # data[j + 1] = temp
            
            [data[j], data[j + 1]] = [data[j +1], data[j]]

            j -= 1
    

data_list  = [10, 50, 40, 60, 20]
insertion_sort(data_list)
print(data_list)