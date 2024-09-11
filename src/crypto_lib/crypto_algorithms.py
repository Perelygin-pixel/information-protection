
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

    degree_binary = format(degree, 'b')[::-1]
    remainder_of_div = 1
    for i in range(len(degree_binary)):
      if(degree_binary[i] == '1'):
        remainder_of_div = remainder_of_div * init_number % module
      init_number = init_number * init_number % module

    return remainder_of_div
