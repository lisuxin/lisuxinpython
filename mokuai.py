def narcissistic_number(x):
    z = x
    Series = []
    while x:
        i = x % 10
        Series.append(i)
        x = x // 10
    y = 0
    for i in Series:
        y = y + i ** 3
    if y == z:
        return True
    else:
        return False


if __name__ == "__main__":
    print(narcissistic_number(153))
    print(narcissistic_number(161))
