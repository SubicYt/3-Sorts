def bubble_sort(matrix):
    first_row = matrix[0]
    iterations = 0
    isSorted = False

    for iterator in range(len(first_row)-1):
        for i in range(len(first_row)-1):
            if first_row[i] > first_row[i+1]:
                first_row[i], first_row[i+1] = first_row[i+1], first_row[i]
                iterations = iterations + 1

    return first_row, iterations

def selection_sort(matrix):
    L = matrix[2]
    iterations = 0
    n = len(L)
    for i in range(n-1):
        #assumes i index is the min element
        min_index = i
        for j in range(i+1, n):
            #Compares the next elements in the array
            #If the next elements are smaller they are put in their correct place
            if L[j] < L[min_index]:
                min_index = j
                L[i], L[min_index] = L[min_index], L[i]
                iterations += 1

                #Why is selection sort so hard for me to understand lol
    return L, iterations

def insertion_sort(matrix):
    L = matrix[1]
    iterations = 0
    for i in range(len(L)):
        for j in range(len(L)-i, len(L)):#look at the last i items of list

            if L[j-1] > L[j]: #If the items are out of order
                L[j], L[j-1] = L[j-1], L[j] #Switches order of items
                iterations += 1
            #very intuitive sorting method
    return L, iterations

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements

    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1:
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list

if __name__ == "__main__":
    array = [[5,4,3,2,1],[5,4,3,2,1],[5,4,3,2,1]]
    array2 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

    print(f"bubble sort {bubble_sort(array)}")
    print(f"selection sort {selection_sort(array)}")
    print(f"insertion sort {insertion_sort(array)}")
