from typing import Tuple

class CryptoAlgorithms():
  @staticmethod
  def exp_by_mod_from_right_to_left(init_number: int,
                                    degree: int,
                                    module: int) -> int:
    """
    Performs exponentiation of a number modulo using
    the algorithm of "exponentiation from right to left",
    known as also as a method of rapid exponentiation modulo.

    The method is based on the representation of the exponent
    in binary form and sequential squaring the base number,
    taking into account the binary representation of the degree.
    Algorithmizes and captures changes using (log n), where n
    is the time pointer.

    Parameters:
      init_number (int): The initial number that is needed
        raise it to a degree.
      degree (int): The degree to which the initial number
        is raised.
      module (int): The module for the modulo operation.

    Returns:
      int: Increase the value (init_number ** degree) %
        of the module.
    """

    if degree < 0:
      return -1
    if module <= 0:
      return -2

    degree_binary = format(degree, 'b')[::-1]
    remainder_of_div = 1
    for i in range(len(degree_binary)):
      if(degree_binary[i] == '1'):
        remainder_of_div = remainder_of_div * init_number % module
      init_number = init_number * init_number % module

    return remainder_of_div

  @staticmethod
  def general_euclid_alg(first_number: int,
                         second_number: int) -> Tuple[int, int, int]:
    """
    Implements the Extended Euclidean Algorithm to find the
    greatest common divisor (GCD) of two integers, as well
    as the coefficients of Bézout's identity.

    This method calculates the GCD of two integers,
    `first_number` and `second_number`.
    Additionally, it finds the integers x and y such that:
    first_number * x + second_number * y =
    gcd(first_number, second_number).
    Returns a tuple (gcd, x, y), where:
      - gcd: The greatest common divisor
              of first_number and second_number.
      - x, y: The coefficients satisfying Bézout's identity.

    Note: If the first number is less than the second,
    the method returns -1, indicating invalid input
    for the algorithm.

    Parameters:
      first_number (int): The first integer.
      second_number (int): The second integer.

    Returns:
      Tuple[int, int, int]: A tuple containing the GCD and
                            Bézout's coefficients (gcd, x, y).
    """

    if first_number < second_number:
        return -1

    current = (first_number, 1, 0)
    next = (second_number, 0, 1)

    while next[0] != 0:
      quotient = current[0] // next[0]
      remainder = (current[0] % next[0],
                  current[1] - quotient * next[1],
                  current[2] - quotient * next[2])
      current, next = next, remainder

    return current
