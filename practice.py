def max(a, b):
    if a > b:
        return a
    else:
        return b

def max2(a, b, c):
    if a > b and a > c:
            return a
    elif b > c and b > a:
            return b
    else:
        return c



def length(list):
    counter = 0
    for x in list:
        counter += 1
    return counter

def wovel(a):
    vowel = ["a, e, i, o, u"]
    for letter in vowel:
        if letter == a:
            return True
    return False

def translate(a):
    consonant = ["t, h, s, f, n"]
    vowel


def main():
    print("Hello World!")
    print(max(5, 6))
    print(max2(10, 13, 18))
    kecske = [4, 8, 12, 13, 21, 42, 40]
    soros = "tizenharom"
    print(length(kecske))
    print(length(soros))
    a = "i"
    print(wovel(a))


if __name__ == "__main__":
    main()
