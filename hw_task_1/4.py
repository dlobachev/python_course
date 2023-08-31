def check_interval(a):
    """Prints '+' if input value in interval (-100; 100), and '-' if not"""
    if a > 100 or a < -100:
        print('-')
    else:
        print('+')
