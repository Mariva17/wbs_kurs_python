"""
Typehints für Container


mypy-Extension von matan Gover in VSCode ist besser als Pyright
"""
def check_dict(d: dict[str, int], word: str) -> int | None:
    """Rückgabewert ist int oder None (int | None)"""
    if word in d:
        return d[word]
    return None

def print_name(names: list[str]):
    for name in names:
        print(name.lower())

namens_liste = ["Bob", "Alice", "Anna"]
print_name(namens_liste)


d = {
    "a": 12,
    "b": 43,
}

check_dict(d, "a")