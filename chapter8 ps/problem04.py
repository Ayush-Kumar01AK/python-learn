
# n = int(input("Entre the number: "))

# def sum_n(n):
#     return n*(n+1)/2

# a = sum_n(n)
# print(f"sum of first {n} number is {a}")



# WITH RESURSIVE

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n == 1):
        return 1
    else:
        return sum(n-1) + n

n = int(input("Entre the number: "))

print(sum(n))
