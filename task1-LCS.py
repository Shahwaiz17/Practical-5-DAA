def lcs(a, b):

    m, n = len(a), len(b)

    c = [[0] * (n + 1) for _ in range(m + 1)]

    direction = [[''] * (n + 1) for _ in range(m + 1)]



    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:

                c[i][j] = c[i - 1][j - 1] + 1

                direction[i][j] = 'd'

            else:

                if c[i - 1][j] >= c[i][j - 1]:

                    c[i][j] = c[i - 1][j]

                    direction[i][j] = 'u'

                else:

                    c[i][j] = c[i][j - 1]

                    direction[i][j] = 's'

    print("Length matrix (c):")

    for row in c:

        print(row)

    print("\nDirection matrix:")

    for row in direction:

        print(row)

    lcs_str = []

    i, j = m, n

    while i > 0 and j > 0:

        if direction[i][j] == 'd':

            lcs_str.append(a[i - 1])

            i -= 1

            j -= 1

        elif direction[i][j] == 'u':

            i -= 1

        else:

            j -= 1

    lcs_str.reverse()

    lcs_result = ''.join(lcs_str)

    print("\nLength of LCS:", c[m][n])

    print("LCS:", lcs_result)

    return c[m][n], lcs_result

lcs("AGCCCTAAGGGCTACCTAGCTT","GACAGCCTACAAGCGTTAGCTTG")
