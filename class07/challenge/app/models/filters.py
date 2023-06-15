""" Filters Model for Decorator's Challenge """
# __doc__ (Filters Model file for little app for Decorator´s Challenge)


class Filters():
    """
    Class for Filters

    Arguments:
    -

    Filters data types.

    >>> filter = Validations()
    True

    TODO:
        -

    """

    @classmethod
    def data_type(cls, value):
        """
        Class-Method for int validation

        Arguments:
        value (bool:int:float:str)

        Filter a variable (bool:int:float:str)

        >>> filters = Filters()
        >>> type(filters.data_type('True'))
        <class 'bool'>

        TODO:
            -
        """

        if value.lower() == 'true':
            return bool(True)

        if value.lower() == 'false':
            return bool(False)

        if value.isnumeric():
            return int(value)

        if value.replace('.', '', 1).isdigit():
            return float(value)

        return str(value)

    def dummy_func(self):
        """ Dummy DocString"""
        return None
