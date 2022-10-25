print("Sort")
n = int(input("enter n: "))
array = []
for i in range(n):
    num = int(input())
    array.append(num)
print(array)
dir = 42
while(dir !=1 and dir != 2): dir = int(input("<1>, sort increasion\n<2>, sort reduction\n"))
if(dir == 1):
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                change = array[j]
                array[j] = array[j+1]
                array[j+1] = change
if(dir == 2):
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                change = array[j]
                array[j] = array[j+1]
                array[j+1] = change
print("sorted array")
print(array)