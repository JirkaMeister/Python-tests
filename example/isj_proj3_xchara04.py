#!/usr/bin/env python3

# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """
    firstEven = "none"
    firstOdd = "none"
    even = 0
    odd = 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
            if firstEven == "none":
                firstEven = number
        else:
            odd += 1
            if firstOdd == "none":
                firstOdd = number

    if even == 0 or odd == 0 or even == odd:
        return 0
    elif even > odd:
        return firstOdd
    else:
        return firstEven
        


# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha_dictionary = {'A' : 'Alfa','B' : 'Bravo', 'C' : 'Charlie', 'D' : 'Delta', 'E' : 'Echo', 'F' : 'Foxtrot',
        'G' : 'Golf', 'H' : 'Hotel', 'I' : 'India', 'J' : 'Juliett', 'K' : 'Kilo', 'L' : 'Lima', 'M' : 'Mike',
        'N' : 'November', 'O' : 'Oscar', 'P' : 'Papa', 'Q' : 'Quebec', 'R' : 'Romeo', 'S' : 'Sierra', 'T' : 'Tango',
        'U' : 'Uniform', 'V' : 'Victor', 'W' : 'Whiskey', 'X' : 'Xray', 'Y' : 'Yankee', 'Z' : 'Zulu'}

    pilot_alpha_list = []
    for letter in word:
        if letter.upper() >= 'A' and letter.upper() <= 'Z':
            pilot_alpha_list.append(pilot_alpha_dictionary[letter.upper()])
        else:
            pilot_alpha_list = "Invalid input"  # In case of any invalid input (not a letter) that can not by transformed
            break
    
    return pilot_alpha_list 
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()