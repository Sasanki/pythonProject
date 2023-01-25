def compute_the_lowest_value(numbers):
    ans = numbers(0) # tutaj błąd
    for i in range(1, len(numbers)):
        if numbers[i] < ans:
            ans = numbers[i]
    return ans

a = [4, 2, 0, 5, 11, 9, 2]
b = [-5, 3, 2, -1, 9]
c = [1, 6, -2, 8, 10, -3]
print(compute_the_lowest_value(a))

