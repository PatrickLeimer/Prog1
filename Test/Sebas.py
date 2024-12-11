import sys

def solution(A):
    rows = []

    for height in A:
        assigned = False
        for row in rows:
            if row[-1] > height:
                row.append(height)
                assigned = True
                break

        if not assigned:
            rows.append([height])

    return len(rows)


def main():
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    sys.stdout.write(str(solution(A)))

main()