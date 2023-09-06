def sort_elements(elements: list) -> list:
    """Returns sorted list of tuples by second item"""
    elements.sort(key=lambda x: x[1])
    return elements


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(sort_elements(elements))
