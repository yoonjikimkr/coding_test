def find_second_largest(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i];
    return num[1];

num = list(map(int, input().split()));
print(find_second_largest(num));