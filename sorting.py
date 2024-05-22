import random

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, comparisons, swaps

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return arr, comparisons, swaps

def main():
    original_list = random.sample(range(1, 100), 10)
    print(f"Original list: {original_list}")

    bubble_sorted_list, bubble_comparisons, bubble_swaps = bubble_sort(original_list.copy())
    print(f"Bubble Sorted list: {bubble_sorted_list}")
    print(f"Bubble Sort - Comparisons: {bubble_comparisons}, Swaps: {bubble_swaps}")

    selection_sorted_list, selection_comparisons, selection_swaps = selection_sort(original_list.copy())
    print(f"Selection Sorted list: {selection_sorted_list}")
    print(f"Selection Sort - Comparisons: {selection_comparisons}, Swaps: {selection_swaps}")

if __name__ == "__main__":
    main()
