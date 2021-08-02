def insertion_sort(dataList):
    n = len(dataList)
    for i in range(1, n):
        item = dataList[i]
        # print(i)
        j = i - 1
        while j >= 0 and dataList[j] > item:
            dataList[j + 1] = dataList[j]
            j = j - 1
        
        dataList[j + 1] = item


dataList = [5, 3, 1, 2]
insertion_sort(dataList)
print(dataList)