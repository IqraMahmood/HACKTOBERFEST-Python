#List is a collection of items enclosed in square bracket and each item is separated by comma.

lst = [1,2,3,4,5]

print(lst)   #[1,2,3,4,5]

print(lst[0:2])   #[1,2]

lst.pop()
print(lst)   #[1,2,3,4]

lst[1] = 10
print(lst)  #[1,10,3,4]

lst.sort()
print(lst)   #[1,3,4,10]

print(max(lst))  #10

print(min(lst))  #1
