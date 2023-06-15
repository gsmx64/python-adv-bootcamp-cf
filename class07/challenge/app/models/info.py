""" Info Model for Decorator's Challenge """
# __doc__ (Info Model file for little app for Decorator´s Challenge)


class Info():
    """
    Class for Info Credits

    Arguments:
    None

    Runs the App.

    >>> info = Info()
    >>> info.show_credits(True)

    TODO:
        -

    """

    @classmethod
    def show_credits(cls, print_credits: True) -> object:
        """
        Class-Method to return credits

        Arguments:
        cls
        print_credits (boolean)

        Prints at exit the app all credits if print_credits is True,
        else returns a dictionary with credits (str/dict)

        TODO:
            -
        """
        info = {
            'title': 'Decorator´s Challengers',
            'version': '1.0.0',
            'date': '2023-06-15',
            'developer': 'Gonzalo Mahserdjian',
            'developer_alias': 'gsmx64',
            'package': 'Bootcamp Código Facilito Python Avanzado',
            'subpackage': 'Class 07 Practice Challenge',
            'class': 'Decorators',
            'bootcamp roadmap': 'https://codigofacilito.com/bootcamps/python-avanzado/roadmap',  # noqa: E501  # pylint: disable=line-too-long
            'license': 'GNU/GPL version 3',
            'license link': 'https://www.gnu.org/licenses/gpl-3.0.txt'
        }

        if print_credits:
            for keys, values in info.items():
                print(f'{keys}: {values}')
        return info

    def dummy_func(self):
        """ Dummy DocString"""
        return None
