# 재귀함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))  #4!=4x3x2x1
print(factorial(5))

# 피보나치 수열
1, 1, 2, 3, 5, 8
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))

