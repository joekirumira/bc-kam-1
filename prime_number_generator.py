def generate_prime_numbers(n):
    prime_numbers = []
    test_numbers = [2,3]
    if isinstance(n, int):
        if n > 0:
            for num in range(2, n):
                if num in test_numbers:
                    prime_numbers.append(num)
                else:
                    is_prime = True
                    for test_number in test_numbers:
                        if num % test_number == 0:
                            is_prime = False
                    if is_prime == True:
                        prime_numbers.append(num)
            return prime_numbers
        else:
            return "range is a negative number"
    else:
        return "range is not integer"