# 1
import random
def losowa(a, b, n):
    A = [[random.randint(0, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def zamW(A, i, j):
    kopia = []
    for k in range(len(A[0])):
        kopia.append(A[i][k])
        A[i][k] = A[j][k]
        A[j][k] = kopia[k]
    return A


def przemW(A, i, k):
    for l in range(len(A[0])):
        A[i][l] = int(A[i][l] * k)
    return A


def dodajW(A, i, j, k):
    k = int(k)
    if k < 0:
        k *= -1
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] += A[j][a]
    else:
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] -= A[j][a]
    return A


def Gauss(A):
    for wiersz in range(len(A)):
        j = wiersz
        i = 0
        while A[j][i] == 0:
              j += 1
              if j == len(A):
                 j = wiersz
                 i += 1
                 if i == len(A[0]):
                    return A
        x = A[j][i]
        A = zamW(A, wiersz, j)
        A = przemW(A, wiersz, 1/x)
        for m in range(wiersz+1, len(A)):
            if A[m][wiersz] != 0:
                A = dodajW(A, m, wiersz, A[m][wiersz])
    return A


b = int(input('Ilość wierszy macierzy A: '))
a = int(input('Ilość kolumn macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
wyswietl(A)
print('\n')
wyswietl(Gauss(A))

print('\n')
# 2
import random
def losowa(a, b, n):
    A = [[random.randint(1, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def zamW(A, i, j):
    kopia = []
    for k in range(len(A[0])):
        kopia.append(A[i][k])
        A[i][k] = A[j][k]
        A[j][k] = kopia[k]
    return A


def przemW(A, i, k):
    for l in range(len(A[0])):
        A[i][l] = int(A[i][l] * k)
    return A


def dodajW(A, i, j, k):
    k = int(k)
    if k < 0:
        k *= -1
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] += A[j][a]
    else:
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] -= A[j][a]
    return A


def Gauss(A):
    B = A
    for wiersz in range(len(B)):
        j = wiersz
        i = 0
        while B[j][i] == 0:
              j += 1
              if j == len(B):
                 j = wiersz
                 i += 1
                 if i == len(B[0]):
                    return B
        x = B[j][i]
        B = zamW(B, wiersz, j)
        B = przemW(B, wiersz, 1/x)
        for m in range(wiersz+1, len(B)):
            if B[m][wiersz] != 0:
                B = dodajW(B, m, wiersz, B[m][wiersz])
    return B


def rz(A):
    rzad = 0
    B = Gauss(A)
    for i in range(len(B)):
        check = 0
        for j in range(len(B[0])):
            if B[i][j] != 0:
                check += 1
                if check == 1:
                    rzad += 1
    return rzad

b = 3
a = 4
n = 4
for i in range(100):
    A = losowa(a, b, n)
    print('\n')
    rzad = rz(A)
    print(rzad)
    if rzad < 3:
        wyswietl(A)
        print('\n')
        wyswietl(Gauss(A))
        input('')

print('\n')
# 3
import random
def losowa(a, b, n):
    A = [[random.randint(0, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def zamW(A, i, j):
    kopia = []
    for k in range(len(A[0])):
        kopia.append(A[i][k])
        A[i][k] = A[j][k]
        A[j][k] = kopia[k]
    return A


def przemW(A, i, k):
    for l in range(len(A[0])):
        A[i][l] = int(A[i][l] * k)
    return A


def dodajW(A, i, j, k):
    k = int(k)
    if k < 0:
        k *= -1
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] += A[j][a]
    else:
        for l in range(0, k):
            for a in range(len(A[0])):
                A[i][a] -= A[j][a]
    return A


def Gauss(A):
    for wiersz in range(len(A)):
        j = wiersz
        i = 0
        while A[j][i] == 0:
              j += 1
              if j == len(A):
                 j = wiersz
                 i += 1
                 if i == len(A[0]):
                    return A
        x = A[j][i]
        A = zamW(A, wiersz, j)
        A = przemW(A, wiersz, 1/x)
        for m in range(wiersz+1, len(A)):
            if A[m][wiersz] != 0:
                A = dodajW(A, m, wiersz, A[m][wiersz])
    return A


def Gauss2(A):
    if len(A) == len(A[0]):
        A = Gauss(A)
        for i in range(len(A)):
            for j in range(i + 1, len(A[0])):
                if A[i][j] != 0:
                    A = dodajW(A, i, j, A[i][j])
        return A
    else:
        print('Bląd! Macierz nie ma równych wymiarów!')
        return A


b = int(input('Ilość wierszy macierzy A: '))
a = int(input('Ilość kolumn macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
wyswietl(A)
print('\n')
wyswietl(Gauss2(A))

print('\n')
# 4
import random
from copy import deepcopy
def losowa(a, b, n):
    A = [[random.randint(0, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def zamW(A, i, j):
    B = deepcopy(A)
    kopia = []
    for k in range(len(B[0])):
        kopia.append(B[i][k])
        B[i][k] = B[j][k]
        B[j][k] = kopia[k]
    return B


def przemW(A, i, k):
    B = deepcopy(A)
    for l in range(len(B[0])):
        B[i][l] = int(B[i][l] * k)
    return B


def dodajW(A, i, j, k):
    B = deepcopy(A)
    k = int(k)
    if k < 0:
        k *= -1
        for l in range(0, k):
            for a in range(len(B[0])):
                B[i][a] += B[j][a]
    else:
        for l in range(0, k):
            for a in range(len(B[0])):
                B[i][a] -= B[j][a]
    return B


def Gauss(A):
    B = deepcopy(A)
    for wiersz in range(len(B)):
        j = wiersz
        i = 0
        while B[j][i] == 0:
              j += 1
              if j == len(B):
                 j = wiersz
                 i += 1
                 if i == len(B[0]):
                    return B
        x = B[j][i]
        B = zamW(B, wiersz, j)
        B = przemW(B, wiersz, 1/x)
        for m in range(wiersz+1, len(B)):
            if B[m][wiersz] != 0:
                B = dodajW(B, m, wiersz, B[m][wiersz])
    return B


def Gauss2(A):
    if len(A) == len(A[0]):
        B = Gauss(A)
        for i in range(len(B)):
            for j in range(i + 1, len(B[0])):
                if B[i][j] != 0:
                    B = dodajW(B, i, j, B[i][j])
        return B
    else:
        print('Bląd! Macierz nie ma równych wymiarów!')
        return A


def odwr(A):
    B = Gauss2(A)
    C = deepcopy(B)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:
                if A[i][j] < 0:
                    for l in range(1, A[i][j]+1):
                        for a in range(len(A[0])):
                            A[i][a] += C[j][a]
                            B[i][a] += C[j][a]
                else:
                    for l in range(1, A[i][j]+1):
                        for a in range(len(A[0])):
                            A[i][a] -= C[j][a]
                            B[i][a] -= C[j][a]
        if A[i][i] != 1:
            for a in range(len(A[0])):
                A[i][a] += C[i][a]
                B[i][a] += C[i][a]
    return B


def pomnoz(A, B):
    W = []
    iloscwierszy = int(len(A))
    ilosckolumn = int(len(A[0]))
    if iloscwierszy == len(B) and ilosckolumn == len(B[0]):
        W = [[0 for i in range(ilosckolumn)] for j in range(iloscwierszy)]
        for i in range(iloscwierszy):
            for k in range(ilosckolumn):
                iloczyn = 0
                for j in range(ilosckolumn):
                    iloczyn += A[i][j]*B[j][k]
                W[i][k] = iloczyn
        return W
    else:
        return W


n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(3, 3, n)
kopiaA = deepcopy(A)
wyswietl(A)
print('\n')
wyswietl(pomnoz(kopiaA, odwr(A)))