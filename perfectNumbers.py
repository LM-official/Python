# %% :::::::::::::::::::::::::::::::::::: SOURCES :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
# perfect numbers definition:       https://en.wikipedia.org/wiki/Perfect_number
# every even perfect number:
    # - is a triangular number:     https://en.wikipedia.org/wiki/Triangular_number
    # - is an hexagonal number:     https://en.wikipedia.org/wiki/Hexagonal_number#:~:text=1%2C%206%2C%2015%2C%2028,.)%20is%20a%20hexagonal%20number.
    # - is a practical number:      https://en.wikipedia.org/wiki/Practical_number
    # - has a binary expression with p values ​​equal to one followed by p-1 zeros (p prime)
        # examples:
        # 6 base 10 = 110 base 2
        # 28 base 10 = 11100 base 2
    
# Mersenne's theory:                https://en.wikipedia.org/wiki/Mersenne_prime
# sympy.isprime(n):                 https://docs.sympy.org/latest/modules/ntheory.html
# list of perfect numbers:          https://en.wikipedia.org/wiki/List_of_Mersenne_primes_and_perfect_numbers
    # first 12 perfect numbers:
    # 6
    # 28
    # 496
    # 8 128
    # 33 550 336 (8 digits)
    # 8 589 869 056 (10 digits)
    # 137 438 691 328 (12 digits)
    # 2 305 843 008 139 952 128 (19 digits)
    # 2 658 455 991 569 831 744 654 692 615 953 842 176 (37 digits)
    # 191 561 942 608 236 107 294 793 378 084 303 638 130 997 321 548 169 216 (54 digits)
    # 13 164 036 458 569 648 337 239 753 460 458 722 910 223 472 318 386 943 117 783 728 128 (65 digits)
    # 14 474 011 154 664 524 427 946 373 126 085 988 481 573 677 491 474 835 889 066 354 349 131 199 152 128 (77 digits)
    
    
    
from time import time
from sys import get_int_max_str_digits
from sympy import isprime
# For large numbers, isprime() uses probabilistic algorithms, such as the Miller-Rabin test, which may return a false positive.
# These algorithms minimize the chance of error, if the test returns True, the probability that the number is not prime is extremely low.

MAX_DIGITS = get_int_max_str_digits() # the limit for integer string conversion (standard: 4300 digits)
# use sys.set_int_max_str_digits() to increase the limit



# %% :::::::::::::::::::::::::::::::::::::::::::: FUNCTION 1 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
def n_perfect_numbers(n_values: int, prime_start: int = 1) -> tuple[list[int], list[int]]:
    """
    Returns the list of the first n-th perfect numbers and the prime numbers that generate them
    """
    
    # input checks
    if not isinstance(n_values, int): raise TypeError(f"TypeError: expected int, got {n_values.__class__.__name__}")
    if n_values == 0: return ([], []) # computes 0 values
    if not isinstance(prime_start, int): raise TypeError(f"TypeError: expected int, got {prime_start.__class__.__name__}")
    if prime_start < 0: prime_start = 1 # skips negative values
    
    
    time_start = time()
    perfect_numbers = list()
    prime_perfect = list()
    
    while True:
        prime_start += 1
        
        mersenne = 2**prime_start-1 # calculates Mersenne's number
        if not isprime(mersenne): continue # avoid useless computation
        
        perfect_number = 2**(prime_start-1)*mersenne # valid <=> Mersenne's number is prime
        # all perfect number computed using Mersenne's number are even
        perfect_numbers.append(perfect_number)
        prime_perfect.append(prime_start)
        
        if len(perfect_numbers) >= n_values: break # ends loop

    print(f"execution time: {time()-time_start}sec.\n")
    return (perfect_numbers, prime_perfect)

    
    
# %% :::::::::::::::::::::::::::::::::::::::::::: FUNCTION 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
def print_perfect_number_list(number_list: list[int]) -> None:
    """
    Prints the list of perfect numbers
    """
    
    # input checks
    if not isinstance(number_list, list): raise TypeError(f"TypeError: expected list, got {number_list.__class__.__name__}")
    if number_list == list():
        print("Empty list")
        return None
    
    

    def decomposer(number: int, max_digits: int = MAX_DIGITS) -> list[str]:
        """
        Decompose a number with more than max_digits digits into blocks with less than max_digits digits
        """
        # input checks
        if not isinstance(number, int): raise TypeError(f"TypeError: expected int, got {number.__class__.__name__}")
        # not tested with negative numbers
        
        block_size = 10**max_digits
        
        if number <= block_size: return [str(number)] # base case
        
        block = str(number % block_size).zfill(max_digits) # takes the last max_digits digits
        # if there were leading zeros they would be lost, zfill() adds them back, adjusting the block size
        rest = number // block_size # the rest of the number
        
        return decomposer(rest) + [block]   
    
    
    
    print("perfect number found:")
    # 21th perfect number: ValueError: Exceeds the limit (4300 digits) for integer string conversion
    # upgraded code for perfect numbers > 20th perfect number
    for index, number in enumerate(number_list, start=1):
        decomposed_number = decomposer(number)

        # n blocks with MAX_DIGITS digits + 1 block with less than MAX_DIGITS digits
        digits = (len(decomposed_number)-1)*MAX_DIGITS + len(decomposed_number[0])
        print(f"{index}° ({digits} digits)")

        for part in decomposed_number: print(part)
        print("")
    
   

# %% :::::::::::::::::::::::::::::::::::::::::::::::::::::: TESTS ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: #
if __name__ == '__main__':
    list_lenght = 0
    while list_lenght < 1:
        try: list_lenght = int(input("how many perfect numbers to search for? "))
        except ValueError: print("Invalid input, enter a valid number")
        
    perfect_list, prime_list = n_perfect_numbers(list_lenght)
    print(f"prime numbers that generate the perfect numbers: {prime_list}")
    print_perfect_number_list(perfect_list)
    
    # with this program you could find the first 38 perfect number, the limits are:
        # - the computation time
        # - the print capacity: you could have 1000 blocks (as many as maximum recursion depth by default of python)
        # of 4300 digits (the maximum digits that python could print in one time (with print python convert integer to string
        # and 4300 is the limit of the convertion by default))

    # MY RESULTS (with i7-9700)
    # first 20 perfect number computed in ~ 40 seconds (prime number: 4423)
    
    # first 21 perfect number computed in ~ 12 minutes (prime number: 9689)
    # the 21th perfect number computed in ~ 11 minutes (prime number: 9689) (start searching from 4423)
    
    # first 22 perfect number computed in ~ 13 minutes (prime number: 9941)
    # the 22th perfect number computed in ~ 74 seconds (prime number: 9941) (start searching from 9689)
    
    # first 23 perfect number computed in ~ 20 minutes (prime number: 11213)
    # the 23th perfect number computed in ~ 7 minutes (prime number: 11213) (start searching from 9941)
    
    # the 24th perfect number computed in ~ 2 hours and 40 minutes (prime number: 19937) (start searching from 11213)
    
    # the 25th perfect number computed in ~ 1 hour (prime number: 21701) (start searching from 19937)
    
    # the 26th perfect number not computed yet (start searching from 21701)
    
# %% ::::::::::::::::::::::::::::::::::::::::::::::: POSSIBILE UPGRADES ::::::::::::::::::::::::::::::::::::::::::::::::::::::: #

# ̶b̶e̶t̶t̶e̶r̶ ̶a̶l̶g̶o̶r̶i̶t̶h̶m̶ ̶f̶o̶r̶ ̶m̶o̶l̶t̶i̶p̶l̶i̶c̶a̶t̶i̶o̶n̶ ̶(̶h̶a̶r̶v̶e̶y̶ ̶h̶o̶e̶v̶e̶n̶ ̶a̶l̶g̶o̶r̶i̶t̶h̶m̶)̶ ̶ ̶ ̶ ̶ ̶h̶t̶t̶p̶s̶:̶/̶/̶e̶n̶.̶w̶i̶k̶i̶p̶e̶d̶i̶a̶.̶o̶r̶g̶/̶w̶i̶k̶i̶/̶M̶u̶l̶t̶i̶p̶l̶i̶c̶a̶t̶i̶o̶n̶_̶a̶l̶g̶o̶r̶i̶t̶h̶m̶
# No, Python switch automatically to better algorithm for non galactic number (too big numbers)
# (Karatsuba            https://en.wikipedia.org/wiki/Karatsuba_algorithm, 
# Toom-Cook             https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication and
# Schönhage-Strassen    https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm)


# use multiprocessing for computing
# increment the maximum depth of recursion
# increment the maximum limit for integer string conversion (sys.set_int_max_str_digits() to increase the limit)