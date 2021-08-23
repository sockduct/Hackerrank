import re

def main():
    string = input()
    res = re.split('[.,]', string)
    for i in res:
        print(i)

if __name__ == '__main__':
    main()

