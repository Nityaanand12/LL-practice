# multiply without opeartor in python

def mul(a, b):
    if b == 0:
        return 0
    b = b-1
    return a + mul(a, b)
 
def for_loop_mul(a, b):
    num = 0
    for i in range(b):
        num += a
    return num
    
print(mul(13,5))
print(for_loop_mul(3,5))
