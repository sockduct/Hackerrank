'''
HRML:
* <tagname1 attrname1 = "value" attrname2 = "value" ...>
  <nestedtagname2 attrname1 ...>
  </nestedtagname2>
  </tagname1>

HRML syntax:
* space after tagname (if attrs), attrname, '=', and value unless it's the last one

Query:
* tag#~attr#, tag#.nestedtag#~attr#
Note:  If no such attr return "Not Found!"

Input:
* N Q # N=# of HRML lines, Q=# of queries
'''

def main():
    stack: List[str]
    n: int
    q: int
    n, q = [int(e) for e in input().split()]

    for i in range(n):
        for e in input().split():
            # Cases:
            # 1) <tag>   # Opening tag, no attrs
            # 2) <tag    # Opening tag, attrs
            # 3) attr
            # 4) =       # attr = val
            # 5) value
            # 6) value>  # End tag
            # 7) </tag>  # Closing tag
            if e.startswith('<') and e.endswith('>'):
                pass
            elif e.startswith('<') and not e.endswith('>'):
                pass
            elif e

if __name__ == '__main__':
    main()

