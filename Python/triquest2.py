# Notes:
# * Not using functions, flat per problem requirements
# * Must be two lines
# * Cannot use strings/string functions
#   e.g., can't do this:
#   for line in range(1, trisize := int(input()) + 1):
#       print(int(''.join([str(i) for i in range(1, line + 1)] + [str(j) for j in range(line - 1, 0, -1)])))
# * Cannot use a 2nd for
#   e.g., can't do this:
#       [print(k, end='') for k in [i for i in range(1, line + 1)] + [j for j in range(line - 1, 0, -1)] + ['\n'] ]

for line in range(1, trisize := int(input()) + 1):
    # For submission, make this into single line:
    print(
        sum(map(lambda t: t[0] * 10**t[1],
            list(zip(range(1, line + 1), range(line)))
            + list(zip(range(line - 1, 0, -1), range(line, line * 2)))
            )
        )
    )
