def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
x = 13

if binary_search(arr, x):
    print("Значение найдено!")
else:
    print("Значение не найдено.")
