def query_hits(strings, queries):
    return [strings.count(query) for query in queries]


def main():
    n = int(input())
    strings = [input() for _ in range(n)]
    q = int(input())
    queries = [input() for _ in range(q)]

    print(f'Matches:  {query_hits(strings, queries)}')


if __name__ == '__main__':
    main()
