import sys
sys.setrecursionlimit(10000)

counter = 0

def partition(A, p, r):  # Lomuto's scheme
    global counter
    x = A[r]
    i = p-1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = list(map(int, input("Enter numbers: ").split()))
quicksort(A, 0, len(A)-1)
print("Sorted list:", A)
print("Counter value:", counter)
