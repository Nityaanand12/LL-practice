def fibnonci(n):
    if n <= 1:
        return n
    return fibnonci(n-2) + fibnonci(n-1)
    
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

for i in range(10):
    print(fibnonci(i))
print("====")
for i in range(10):
    print(factorial(i))
