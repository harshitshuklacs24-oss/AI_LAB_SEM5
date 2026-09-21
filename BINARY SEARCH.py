def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23

result = binary_search(numbers, target_val)
print(f"Element found at index: {result}") 