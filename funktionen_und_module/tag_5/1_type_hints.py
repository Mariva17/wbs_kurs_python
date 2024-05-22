"""
unveränderliche Datentypen

"""

def repeater(word: str, number: int=1) -> str:
    """Repeat a word.
    Args:
        word: word to repeat
        number: how many times should word to repeated

    Returns:
        repeated word
    """
    return word * number

result = repeater("hallo", number=3)
print(result)
print(repeater.__annotations__) # {'word': <class 'str'>, 'number': <class 'int'>, 'return': <class 'str'>}

