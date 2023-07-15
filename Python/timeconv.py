#! /usr/bin/env python3

from collections import namedtuple
import re

time12 = namedtuple('time12', ['hour', 'min', 'sec', 'period'])

def conv24(timestr):
    regexstr = r'(\d{1,2}):(\d{1,2}):(\d{1,2})([aApP][mM])'
    timedata = time12(*re.match(regexstr, timestr).groups())

    match timedata:
        case (hour, min, sec, 'AM' | 'am' | 'aM' | 'Am'):
            hour = '00' if hour == '12' else hour
            return f'{hour:0>2}:{min:0>2}:{sec:0>2}'
        case (hour, min, sec, 'PM' | 'pm' | 'pM' | 'Pm'):
            hour = 12 if hour == '12' else int(hour) + 12
            return f'{hour:0>2}:{min:0>2}:{sec:0>2}'
        case _:
            raise ValueError(f'Unsupported format:  {timedata}')

def main():
    data = input('12-hour time (HH:MM:SS[AM|PM]):  ')
    print(conv24(data))

if __name__ == '__main__':
    main()
