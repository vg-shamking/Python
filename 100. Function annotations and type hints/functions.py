def multiply(x: float, y: float) -> float:
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards as backwards.
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """

    :rtype: object
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """
    Return the `n` th Fibonacci number, for positive `n` .
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()
