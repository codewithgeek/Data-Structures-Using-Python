# Python Program to reverse an array using Two Pointers

def reverseArray(arr):
    left = 0
    right = len(arr) - 1
  
    while left < right:
        
        arr[left], arr[right] = arr[right], arr[left]
  
        left += 1
        right -= 1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")



# Python Program to reverse an array by swapping elements

def reverseArray(arr):
    n = len(arr)

    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")
