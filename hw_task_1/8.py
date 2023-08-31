def abb(words: str) -> str:
    """Returns the abbreviation of input string"""
    if type(words) != str:
        raise Exception("Incorrect input")
    print(*[i[0] for i in words.split(' ')], sep='')


abb('Hello world')
abb('As soon as possible')
abb(1)