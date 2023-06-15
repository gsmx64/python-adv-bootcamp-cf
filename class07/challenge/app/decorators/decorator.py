""" Decorator for Decorator's Challenge """
# __doc__ (Decorator file for little app for Decorator´s Challenge)

import functools

from app.models.validators import Validators


def decorator_validate_int(func: int) -> int:
    """
    Decorator for integer validation

    Arguments:
    args (int)

    Decorates a function for integer variable validations (int)

    TODO:
        -
    """

    @functools.wraps(func)
    def wrapped_validate_int(*args) -> object:
        validations = Validators()
        errors = []
        for arg in args:
            if validations.validate_int(arg):
                errors = validations.validate_int(arg)
                raise TypeError(''.join(str(errors)))
        return func(*args)
    return wrapped_validate_int
