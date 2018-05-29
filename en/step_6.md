--- challenge ---

## Challenge: complete the documentation

Can you add docstrings to all the methods and properties of the `Card` and `Deck` classes to describe what they do?

--- hints ---

--- hint ---

+ Add a docstring directly under the methods definition `def`.

```python
    def shuffle(self):
        """ A description of what the shuffle method does """
        random.shuffle(self._cards)
```

--- /hint ---

--- hint ---

+ Only add a docstring to a properties **getter** that describes what the property is — the **setter** doesn't need one.

```python
    @property
    def suit(self):
        """ Gets or sets the suit of the Card """
        return self._suit

    @suit.setter
    def suit(self, suit):
        # there is no need for a docstring on a setter
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")
```

Adding a docstring to the setter will not cause an error, but `pydoc` will ignore it when generating the documentation.

--- /hint ---

--- /hints ---

+ When you have added docstrings to your code, you can run the `pydoc` command again to generate updated documentation.

--- /challenge ---
