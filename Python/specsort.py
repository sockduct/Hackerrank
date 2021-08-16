def main():
    data = input()
    odddigits = []
    evendigits = []
    lowercase = []
    uppercase = []

    for i in data:
        if i in ['1', '3', '5', '7', '9']:
            odddigits.append(i)
        elif i in ['0', '2', '4', '6', '8']:
            evendigits.append(i)
        elif 'a' <= i <= 'z':
            lowercase.append(i)
        else:
            uppercase.append(i)

    new_string = ''.join(sorted(lowercase) + sorted(uppercase) + sorted(odddigits) + sorted(evendigits))

    print(new_string)


if __name__ == '__main__':
    main()

