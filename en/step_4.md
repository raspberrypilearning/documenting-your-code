## Documenting your code

If you look through the `card.py` program, you will notice that there is no additional information in the code that describes how it works or how to use it. 

The program is small, so you could probably review the code and work out how the interface works and what each function does. But what about programs that have a thousand lines of code? Or even a million? It would be extremely difficult and time-consuming to figure out how such big programs work without some additional information.

Python allows you to add information about your program into the code using [**docstrings**](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring). Docstrings are the basis for creating documentation for your code.

You add docstrings at the start of a module, class, or function in the form of a string framed by three double quotation marks `"""` on either side:

```python
def helloworld():
    """ prints 'hello world' to the screen """
    print("hello world")
```

Docstrings can be a single line (as in the example above), or they can span multiple lines:

```python
def helloworld():
    """
    This function prints 'hello world' to the screen.
    It accepts no arguments and returns nothing.
    """
    print("hello world")
```

--- task ---

+ You first task is to add a docstring to the `Card` class to describe the class and what it is for.

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

+ Add a suitable docstring to the `Deck` class to describe it.

--- hints ---

--- hint ---

+ Follow the same format as the docstring in the `Card` class.

--- /hint ---

--- hint ---

+ The `Deck` class represents a deck of playing cards in order.

--- /hint ---

--- hint ---

```python
class Deck:
    """
    The Deck class represents a deck of playing cards in order.
    """
    def __init__(self):

        self._cards = []
        self.populate()
```

--- /hint ---

--- /hints ---

--- /task ---
