# 1-es feladat: kell az legkisebb
def min(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
# 2-es feladat: kell a legnagyobb
def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
# 3-as feladat: dolgozat pontszám és az érdemjegy kell
# nem tudom még, input kell v or idk
# def value(x):
#     if x < 50
#         return 1
#     elif x >= 50 and x < 60:
#         return 2
#     elif x >= 60 and x < 70:
#         return 3
#     elif x >= 70 and x < 85:
#         return 4
#     else:
#         return 5

#4-es feladat: osztható 3 v 5
def ratio(x):
    if x // 5:
        return True
    elif x // 3:
        return True
    else:
        return False

#5-ös feladat: 3 szám közül bármelyik 2 összege egyenlő a harmadik szám közül fingom sincs
#def sum(a, b, c)

# #6-os feladat: 3 szám közül mind a 3 szám páros-e
# def even(a, b, c):
#     if even % 2:
#         return True
#     else:
#         return False



def main():
    print(min(20, 35, 29))
    print(max(7, 18, 9))
    #print(value(63))
    print(ratio(44))
    #print(even(6, 8, 10))

if __name__ == "__main__":
    main()