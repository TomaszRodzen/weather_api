"""
Napisz funkcję quick_sort, która implementować będziealgorytm sortowania szybkiego.
"""


def quick_sort(t, L, P):
    i = L
    j = P
    x = t[(L+P) // 2]

    while i < j:
        while t[i] < x:
            i = i + 1
        while x < t[j]:
            j = j - 1
        if i <= j:
            bufor = t[i]
            t[i] = t[j]
            t[j] = bufor
            i = i + 1
            j = j - 1
        if L < j:
            quick_sort(t, L, j)
        if i < P:
            quick_sort(t, i, P)


if __name__ == '__main__':
    t = [3, 1, 2, 7, 4, 6, 5, 9, 0]
    quick_sort(t, 0, len(t)-1)
    print(t)
