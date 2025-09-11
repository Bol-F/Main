def matrix_2x2(a, b, c, d):
    return a * d - b * c


def matrix_3x3(a, b, c, d, e, f, g, h, i):
    return (
        a * matrix_2x2(e, f, h, i)
        - b * matrix_2x2(d, f, g, i)
        + c * matrix_2x2(d, e, g, h)
    )


def matrix_4x4(a, b, c, d, e, f, g, h, i, j, k, l, m, z, o, p):
    return (
        a * matrix_3x3(f, g, h, j, k, l, z, o, p)
        - b * matrix_3x3(e, g, h, i, k, l, m, o, p)
        + c * matrix_3x3(e, f, h, i, j, l, m, z, p)
        - d * matrix_3x3(e, f, g, i, j, k, m, z, o)
    )


import sys

dimension = int(input("What is the dimension of your matrix ?\n:"))
if dimension <= 1:
    print("What ?\nReally nigga?")
    sys.exit()

elif dimension == 2:
    a = int(input("What is the a_00 ? \n:"))
    b = int(input("What is the a_01 ? \n:"))

    c = int(input("What is the a_10 ? \n:"))
    d = int(input("What is the a_11 ? \n:"))

    print(
        "det of your matrix is equal to this number  --->",
        matrix_2x2(a, b, c, d),
        "\nU don't even find the determinant of 2x2 matrix\nWhat is the purpose fo ur existance \nTHINK ABOUT IT !!!",
    )

elif dimension == 3:
    a = int(input("What is the a_00 ? \n:"))
    b = int(input("What is the a_01 ? \n:"))
    c = int(input("What is the a_02 ? \n:"))

    d = int(input("What is the a_10 ? \n:"))
    e = int(input("What is the a_11 ? \n:"))
    f = int(input("What is the a_12 ? \n:"))

    g = int(input("What is the a_20 ? \n:"))
    h = int(input("What is the a_21 ? \n:"))
    i = int(input("What is the a_22 ? \n:"))

    print(
        "det of your matrix is equal to this number  --->",
        matrix_3x3(a, b, c, d, e, f, g, h, i),
        "\nOkay, but it isn't too hard to count",
    )

elif dimension == 4:
    a = int(input("What is the a_00 ? \n:"))
    b = int(input("What is the a_01 ? \n:"))
    c = int(input("What is the a_02 ? \n:"))
    d = int(input("What is the a_03 ? \n:"))

    e = int(input("What is the a_10 ? \n:"))
    f = int(input("What is the a_11 ? \n:"))
    g = int(input("What is the a_12 ? \n:"))
    h = int(input("What is the a_13 ? \n:"))

    i = int(input("What is the a_20 ? \n:"))
    j = int(input("What is the a_21 ? \n:"))
    k = int(input("What is the a_22 ? \n:"))
    l = int(input("What is the a_23 ? \n:"))

    m = int(input("What is the a_30 ? \n:"))
    z = int(input("What is the a_31 ? \n:"))
    o = int(input("What is the a_32 ? \n:"))
    p = int(input("What is the a_33 ? \n:"))

    print(
        "det of your matrix is equal to this number  --->",
        matrix_4x4(a, b, c, d, e, f, g, h, i, j, k, l, m, z, o, p),
        "\nbruh ?! \nno way that you need this",
    )
