print("Sort")
n = int(input("enter n: "))
array = []
for i in range(n):
    num = int(input())
    array.append(num)
print(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            change = array[j]
            array[j] = array[j+1]
            array[j+1] = change

print("sorted array")
print(array)