import re


# Input:  lowercase word list
# Output:  word score
def score_words(word_list):
    '''
    * Vowels:  a, e, i, o, u, sometimes y
    * Score:
      * single word:
        * 2 if has even number of vowels
        * 1 otherwise
      * total = sum of word scores
    '''
    return sum(
        2 if len(re.findall(r'[aeiouy]', word)) % 2 == 0 else 1
        for word in word_list
    )


def main():
    num_words = int(input())
    words = input().split()
    score = score_words(words)

    print(f'{score}')


if __name__ == '__main__':
    main()
