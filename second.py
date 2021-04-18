ar = [[1, 2, 3, 4],
      [5, 1, 2, 3],
      [9, 5, 1, 2]]


def display():
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            print(ar[i][j], end=" ")
        print()


def is_toeplitz():
    for i in range(len(ar)-1):
        for j in range(len(ar[i])-1):
            if ar[i][j] != ar[i+1][j+1]:
                return False
    return True


Result = is_toeplitz()
print(Result)
