'''
 a.

--PSEUDOCODE--

HEAPIFY(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap A[i] with A[largest]
        HEAPIFY(A, n, largest)

BUILD-MAX-HEAP(A):
    n = length(A)
    for i = floor(n / 2) - 1 down to 0:
        HEAPIFY(A, n, i)

HEAPSORT(A):
    BUILD-MAX-HEAP(A)
    for i = length(A) - 1 down to 1:
        swap A[0] with A[i]
        HEAPIFY(A, i, 0)

'''

'''
b.

1. Time Complexity
    = Building the Heap: O(n)
        - Each heapify operation takes O(log k) and it is called for k = n/2.
    = Sorting the Heap: O(nlog n)
        - Extracting the maximum element involves O(log n) and it is done n - 1 times.
    = Space Complexity
        - HeapSort is an inplace algorithm, meaning it doesn't require additional memory beyond the input array => O(1).
    = Stability
        HeapSort is not stable, as the relative order of equal elements may change during the sorting process.
'''



# c.

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Example usage
data = [4, 10, 3, 5, 1]
print("Original array:", data)
heap_sort(data)
print("Sorted array:", data)