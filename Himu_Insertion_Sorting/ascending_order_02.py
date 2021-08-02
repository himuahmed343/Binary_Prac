def insertion_sort(data):
    # x is store the length
    x = len(data)
    for i in range(1, x):
        item = data[i]
        j = i - 1
        while j >= 0 and data[j] > item:
            data[j + 1] = data[j]
            # [data[j], data[j + 1]] = [data[j + 1], data[j]]
            j -= 1

        data[j + 1] = item


data_list = []
n = int(input('Length of list: '))
for i in range(n):
    l = int(input('Insert number: '))
    data_list.append(l)
p = data_list
insertion_sort(p)
print('Sorted List: ',p)