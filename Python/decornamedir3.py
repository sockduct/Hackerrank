def formal(ns):
    first,last,age,sex = ns
    return ('Mr. ' if sex == 'M' else 'Ms. ') + first + ' ' + last

def std(f):
    def inner(ns):
        return map(formal, f(ns))
    return inner

@std
def nsort(ns):
    return [x for x in sorted(ns, key=lambda x: x[2])]

n = int(input())
for x in nsort([input().split() for x in range(n)]):
    print(x)
