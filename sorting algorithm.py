def ListSorter(array):
    n = len(array)
    for x in range(n):
        already_sorted = True
        for j in range(n - x - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array
   
if __name__ == "__main__":
    array = [5,2,1,6,2,3,9,7,8,11]
    x=ListSorter(array)
    print(x)
    
