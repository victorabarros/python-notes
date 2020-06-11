# Challenge: https://youtu.be/41ON2EghJi0?list=WL
import time
import math


def _generate_simple_mat(size):
    mat = [[ii+size*(jj) for ii in range(size)] for jj in range(size)]
    # print(size)
    # print(
    # "\n".join([str("\t".join([str(e) for e in line])) for line in mat]))
    return mat


def search_on_matrix(mat, value):
    for line in mat:
        for element in line:
            if value == element:
                return True
    return False


def measure_complexity(seart_func, matrix_generator, nn):
    firs_dt = None
    print("n\tdt\tmath.sqrt(dt/firs_dt)")

    for n in [2 ** index for index in range(nn)]:
        mat = matrix_generator(n)

        s = time.time()
        seart_func(mat, n**2)
        # False
        seart_func(mat, n**2-1)
        # True
        dt = (time.time() - s) * 1000  # miliseconds

        if not firs_dt:
            firs_dt = dt

        print(n, "\t", dt, "\t", math.sqrt(dt/firs_dt))


if __name__ == "__main__":
    measure_complexity(search_on_matrix, _generate_simple_mat, 13)
    # TODO: fazer busca binária
