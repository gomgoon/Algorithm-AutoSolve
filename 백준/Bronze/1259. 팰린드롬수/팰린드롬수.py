while True:
    pal = input()

    if pal == '0':
        break

    rev_pal = pal[::-1]
    if pal == rev_pal:
        print('yes')
    else:
        print('no')