

def print_prime_factors(number):
    print(number, "=", end=' ') #printing the parameter
    for i in range(2, number):
        while number % i == 0:
            print(i, end=' ')
            number //= i  # number = number // i
            if number != 1:
                print('*', end=' ')
        if number == 1:
            break

print_prime_factors(300)