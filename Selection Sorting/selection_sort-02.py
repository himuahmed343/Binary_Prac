def select_sort(data_list):
    length = len(data_list)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if data_list[j] < data_list[min_index]:
                min_index = j
        
        if min_index != i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp





data_list = [40, 20, 60, 75, 35, 95]
select_sort(data_list)
print('Sorted List:', data_list)