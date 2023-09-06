def filter_string(s: str) -> str:
    """Returns string without stop words"""
    stop_words = ['Python', 'php', 'go', 'C']
    return ' '.join(list(filter(lambda x: x not in stop_words, s.split())))


s = 'Hello Python user php python C not go'
print(filter_string(s))  # Hello user python not
