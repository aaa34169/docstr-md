"""#Test file"""

import random
from random import random


def my_func(param0, param1=1.):
    """
    This is my function.

    Parameters
    ----------
    param0 : str
        This is parameter 0.

    param1 : float, default=1.0
        This is parameter 1.

    Returns
    -------
    None

    Examples
    --------
    ```python
    my_func('hello', 'world')
    ```

    Out:

    ```
    hello world
    ```
    """
    print(param0, param1)


class MyClass():
    """
    This is my class.

    Parameters
    ----------
    param0 : str
        This is parameter 0.

    param1 : str or None, default=None
        This is parameter 1.

    Attributes
    ----------
    attr0 : str
        This is attribute 0.

    attr1: str or None
        This is attribute 1.

    Notes
    -----
    This is a note.

    Examples
    --------
    ```python
    x = MyClass('param0')
    x.print_greeting()
    ```

    Out:

    ```
    hello world
    ```
    """
    def __init__(self, param0, param1=None):
        self.attr0 = param0
        self.attr1 = param1

    def print_greeting(self, name='world'):
        '''
        This method returns a greeting.

        Parameters
        ----------
        name : str
            This is the name of the person to greet.

        Returns
        -------
        greeting : str
            Of the form 'hello, {name}!'.
        '''
        return 'hello, {}!'.format(name)