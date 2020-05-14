'''# Test'''

import random
from random import random

'''## src.test.**my_func**'''

def my_func(param0, param1=1.):
    '''
    This is my function.

    Parameters
    ----------
    param0 : str
        This is parameter 0. `param0`.

    param1 : float
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
    '''
    print(param0, param1)



'''##src.test.**MyClass**'''

class MyClass():
    '''
    This is my class.
    Its description is on multiple lines.

    And it's two paragraphs long.

    Parameters
    ----------
    param0 : str
        This is parameter 0.

    param1 : int
        This is parameter 1.

    param2 : callable
        This is parameter 2.

    Attributes
    ----------
    attr0 : str
        This is attribute 0.

    attr1: int
        This is attribute 1.

    Notes
    -----
    This is a note.

    Examples
    --------
    ```python
    print('hello world')
    ```

    Out:

    ```
    hello world
    ```
    '''
    def __init__(self, param0, param1=1, param2=(lambda x: x)):
        self.attr0 = param0
        self.attr1 = param1
        self.attr2 = param2

    def print_greeting(self, name='world'):
        '''
        This method prints a greeting.

        Parameters
        ----------
        name : str
            This is the name of the person to greet.

        Returns
        -------
        greeting : str
            Of the form 'hello, {name}!'.
        '''
        greeting = 'hello, {}!'.format(name)
        print(greeting)
        return greeting

    def print_goodbye(self, name='moon'):
        '''
        This method prints goodbye.

        Parameters
        ----------
        name : str, default='moon'
            The name of the person to say goodbye to.

        Returns
        -------
        goodbye : str
            Of the form 'goodbye, {name}!'

        Notes
        -----
        This is a note.

        Examples
        --------
        ```python
        cls = MyClass(param0, param1)
        cls.print_goodbye()
        ```

        Out:

        ```
        goodbye, moon!
        ```
        '''
        goodbye = 'goodbye, {}!'.format(name)
        print(goodbye)
        return goodbye