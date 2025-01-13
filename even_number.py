# Write a function that takes a list of integers and returns a new list with only the even numbers.
def even_number(num):
    even = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
    return even
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_number(num))