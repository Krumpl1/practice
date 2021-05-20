def min(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

def main():
    print(min(20, 35, 29))

if __name__ == "__main__":
    main()