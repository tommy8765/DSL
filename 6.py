def counting_Sort(arr, p):
    n = len(arr)
    result = [0] * n
    c = [0] * 10

    for i in range(0, n):
        index = arr[i] // p
        c[index % 10] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // p
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = result[i]


def radix_Sort(arr):
    maximum = max(arr)
    p = 1
    while maximum // p > 0:
        counting_Sort(arr, p)
        p *= 10


# Taking input from the user
try:
    input_str = input("Enter a list of integers separated by space: ")
    array = list(map(int, input_str.split()))
except ValueError:
    print("Invalid input. Please enter integers separated by space.")
    exit()

print("The original array is:", array)
radix_Sort(array)
print("The sorted array is:", array)

