#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    main = []
    for i in matrix:
        sub = list(map(lambda x: x ** 2, i))
        main.append(sub)
    return main
