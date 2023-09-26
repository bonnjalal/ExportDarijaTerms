


def jalal(i):
    i = i
    i += 1
    print(i)

    if(i < 5):
        i = jalal(5)
    return i


print(jalal(1))
