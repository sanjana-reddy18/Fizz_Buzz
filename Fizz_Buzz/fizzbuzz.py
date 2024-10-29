def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Get input range from the user
try:
    start = 1
    end = 101

    # Ensure start is less than or equal to end
    if start > end:
        print("The start of the range should be less than or equal to the end.")
    else:
        # Apply FizzBuzz in the specified range
        for i in range(start, end + 1):
            print(fizz_buzz(i))

except ValueError:
    print("Please enter valid integer values.")