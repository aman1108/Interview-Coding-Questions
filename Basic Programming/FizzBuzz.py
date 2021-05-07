def solve(n):
    ans=[]
    for i in range(n):
        if (i%3 and i%5):
            ans.append("FizzBuzz")
        elif (i%3):
            ans.append("Fizz")
        elif (i%5):
            ans.append("Buzz")
        else:
            ans.append(str(i+1))
    return ans
