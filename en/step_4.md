## Documenting your code

If you look at the `card.py` program you will notice that there is no additional information in the code which describes how it works or how to use it. 

This is a small program so you could probably review the code and work out how the interface works and what each function does, but what if this program had a thousand lines of code? Or a million? Very quickly it wouldn't be possible to work it out and you would need some more information.

Python allows you add information about your program into the code using [DocStrings](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring) and these are the basis for creating documentation for your code.

*DocStrings* are added to the code using triple double quotes `"""` at the start of a module, class or function:

```python
def helloworld():
    """ prints 'hello world' to the screen """
    print("hello world")
```

*DocStrings* can be a single line (as in the example above), or over multiple lines:

```python
def helloworld():
    """
    This function prints 'hello world' to the screen.
    It accepts no arguments and returns nothing.
    """
    print("hello world")
```

--- task ---

The first step is to add a *docstring* to the **Card** class which describes the class and what it is for.

```python
class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    def __init__(self, suit, number):

        self._suit = suit
        self._number = number
```

--- /task ---

--- task ---

Add a suitable *docstring* to the **Deck** class to describe it.

--- hints ---

--- hint ---

Follow the same format as the *docstring* in the Card class.

--- /hint ---

--- hint ---

*The Deck class represents a deck of playing cards in an order*

--- /hint ---

--- hint ---

```python
class Deck:
    """
    The Deck class represents a deck of playing cards in an order.
    """
    def __init__(self):

        self._cards = []
        self.populate()
```

--- /hint ---

--- /hints ---

--- /task ---
