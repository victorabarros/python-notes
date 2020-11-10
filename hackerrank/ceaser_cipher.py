# Complete the caesarCipher function below.
def caesarCipher(s, k):
    resp = ''
    for ii in s:
        if ii == '-':
            resp += ii
            continue

        c = ord(ii)
        j = c + k

        if ii.islower():
            while 122 < j:
                j -= 26
        elif ii.isupper():
            while 90 < j:
                j -= 26
        # if 90 < j < 97 or 122 < j:
        #     j -= 26

        resp += chr(j)

    return resp


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # s = input()

    # k = int(input())

    for word, k, ans in [
        ('Always-Look-on-the-Bright-Side-of-Life', 5,
         'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'),
        ('middle-Outz', 2, 'okffng-Qwvb'),
        ('z', 2+26*4, 'b')
    ]:
        result = caesarCipher(word, k)
        print(result, result == ans)

    # fptr.write(result + '\n')

    # fptr.close()
