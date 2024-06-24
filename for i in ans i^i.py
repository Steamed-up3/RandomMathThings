def math():
    while True:
        try:
            ans = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid.\n')

    for i in range(ans):
        print(i**i)
    print('Done.')

math()