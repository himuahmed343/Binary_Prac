def bubble_sort(datalist):
    n = len(datalist)
    for i in range(n-1):
        swapped = False
        
        for j in range(n-i-1):
            
            if  datalist[j] > datalist[j+1]:
                temp = datalist[j]
                datalist[j] = datalist[j+1]
                datalist[j+1] = temp
                
                swapped = True
        
        if not swapped:
            break

if __name__ == '__main__':
    datalist = [2, 5, 9, 7]
    bubble_sort(datalist)
    print(datalist)