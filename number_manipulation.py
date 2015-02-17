
def digitize_number(number):
    result = []
    
    while number > 0:
        result.append(number % 10)
        number /= 10

    return result

def are_permutation(number_one, number_two):
    """Function that compares if two numbers are permutation of each other i.e. if they
       are consisted of the same digits."""
    first = digitize_number(number_one)
    second = digitize_number(number_two)
    first.sort()
    second.sort()
    return first == second


