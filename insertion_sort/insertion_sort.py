def insertion_sort(unsorted_list):
    for i in range(1,len(unsorted_list)):
        j = i-1
        temp = unsorted_list[i]
        while j >= 0 and temp < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = temp
    

if __name__ == "__main__":
    arr = [20,18,12,8,5,-2] 
    print(arr)
    insertion_sort(arr) 
    for i in range(len(arr)): 
        print (arr[i])     
    print(arr)