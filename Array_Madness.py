def array_madness(a, b):
    sum_of_squares_a = sum(x ** 2 for x in a)
    sum_of_cubes_b = sum(x ** 3 for x in b)
    return sum_of_squares_a > sum_of_cubes_b