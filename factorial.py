# factorials using for loop


def factorial(num):
    result = 1
    for i in range(2,num+1):
        result *= i
    return result
    


# factorial using recursion

def factorial_recur(num):
    if num < 0:
        return "incorrect"
    
    elif num == 0 or num == 1:
        return 1
    
    else:
        return num * factorial_recur(num-1)



if __name__ == "__main__":
    print(factorial(10))
    print(factorial_recur(10))