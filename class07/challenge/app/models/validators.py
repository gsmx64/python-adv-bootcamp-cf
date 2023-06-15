""" Validators Model for Decorator's Challenge """
# __doc__ (Validators Model file for little app for Decorator´s Challenge)


class Validators():
    """
    Class for Validations

    Arguments:
    -

    Makes some validations.

    >>> validate = Validators()
    >>> validate.validate_int(1)
    True

    TODO:
        -

    """

    @classmethod
    def validate_int(cls, variable):
        """
        Class-Method for int validation

        Arguments:
        func (int)

        Check if the variable is an integer (int)

        >>> validate = Validators()
        >>> validate.validate_int(1)
        True

        TODO:
            -
        """
        if not isinstance(variable, int):
            return f'>>> La variable "{str(variable)}" NO es un entero.'
        return None

    def dummy_func(self):
        """ Dummy DocString"""
        return None
