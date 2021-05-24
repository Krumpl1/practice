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
    if x % 3 == 0:
        return True
    elif x % 5 == 0:
        return True
    else:
        return False

#5-ös feladat: 3 szám közül bármelyik 2 összege egyenlő a harmadik szám közül fingom sincs
#def sum(a, b, c)

#6-os feladat: 3 szám közül mind a 3 szám páros-e
def even(a, b, c):
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return True
    else:
        return False

# #7-es feladat: 2 szó és az ABC sorrend
# def alph(tojas, sajtkrem)
#     if word1 > word2:
#         return

#9-es feladat: ker 2 poz szamot
def main():
    print(min(20, 35, 29))
    print(max(7, 18, 9))
    #print(value(63))
    print(ratio(15))
    print(even(2, 8, 14))

if __name__ == "__main__":
    main()