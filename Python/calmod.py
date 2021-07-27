'''
Input:
* date: MM DD YYYY (2000 < YYYY < 3000)

Goal:
* Determine what the day is for date

Output:
* Day in all caps (e.g., MONDAY)
'''

import calendar

def main():
    year: int
    month: int
    day: int
    weekday: int
    dayname: str

    month, day, year = [int(e) for e in input().split()]
    weekday = calendar.weekday(year, month, day)
    dayname = calendar.day_name[weekday]

    print(f'{dayname.upper()}')


if __name__ == '__main__':
    main()

