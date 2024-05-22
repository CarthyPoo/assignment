#okay look it looks like a lot but don't worry we'll work as we go, this is the best way to learn trust me 0_0
#summary of what this program does is print the sorted list using bubble and selection sort then printing the amount of comparisons of values it needed to make
#then print the amount of steps(swaps) it had to make.

import random

def bubble_sort(arr):                                         # Loop through the array
    n = len(?)                                                 # Get the length of the array
    comparisons = ?                                           # Initialize the comparisons counter
    swaps = ?                                                # Initialize the swaps counter\

    for i in range(n):                                        # Loop through the array
        for j in range(0, n-i-1):                             # Inner loop to compare adjacent elements
            comparisons += 1                                  # Increment the comparisons counter
            if arr[j] ? arr[?]:                               # If the current element is greater than the next element, swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1                                    # Increment the swaps counter

    return ????????                                           # Return the sorted array and the counters

def selection_sort(arr):
    n = ?                                # Get the length of the array
    comparisons = ?                      # Initialize the comparisons counter
    swaps = ?                           # Initialize the swaps counter
                                                
    for i in range(n):                  # Loop through the array
        min_idx = i                     # Assume the current position is the minimum
        for j in range(i+1, n):         # Inner loop to find the actual minimum element
            comparisons += ?            # Increment the comparisons counter
            if arr[j] ? arr[min_idx]:   # If a smaller element is found, update the minimum index
                min_idx = j             

        arr[i], arr[min_idx] = arr[min_idx], arr[i]     # Swap the found minimum element with the first unsorted element
        swaps += 1
    return ???????                                          # Return the sorted array and the counters

def main():
    original_list = random.sample(range(1, 100), 10)     # Generate a list of 10 random numbers between 1 and 99
    print(f"Original list: {original_list}")

    bubble_sorted_list, bubble_comparisons, bubble_swaps = bubble_sort(original_list.copy())
    print(f"Bubble Sorted list: {bubble_sorted_list}")
    print(f"Bubble Sort - Comparisons: {bubble_comparisons}, Swaps: {bubble_swaps}")

    selection_sorted_list, selection_comparisons, selection_swaps = selection_sort(original_list.copy())
    print(f"Selection Sorted list: {selection_sorted_list}")
    print(f"Selection Sort - Comparisons: {selection_comparisons}, Swaps: {selection_swaps}")

if __name__ == "__main__":
    main()
