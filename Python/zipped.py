def main():
    students, subjects = map(int, input().split())
    matrix = []

    for _ in range(subjects):
        matrix.append(map(float, input().split()))

    student_score_tuples = zip(*matrix)
    for student_scores in student_score_tuples:
        res = sum(student_scores)/subjects
        print(f'{res:.1f}')

if __name__ == '__main__':
    main()

