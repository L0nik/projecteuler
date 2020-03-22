
def solution1(num, mul_1, mul_2):
    res = 0
    for i in range(1, num):
        if (i % mul_1 == 0) or (i % mul_2 == 0):
            res += i
    return res

def solution2(num, mul_1, mul_2):

    """
    This way of solving the problem, while being slightly more complex,
    allows to significantly reduce the number of iterations
    """

    res = 0
    a = num // mul_1
    b = num // mul_2

    if num % mul_1 != 0:
        a = a + 1
    if num % mul_2 != 0:
        b = b + 1

    for i in range(1, a):
        current_number = mul_1*i
        res = res + current_number

    for i in range(1, b):
        current_number = mul_2*i
        if (current_number % mul_1 != 0):
            res = res + current_number

    return res

def print_result(solution_number, num, mul1, mul2):
    solution_number = solution_number - 1
    solution_list = [solution1, solution2]
    chosen_solution = solution_list[solution_number]
    res = chosen_solution(num, mul1, mul2)
    print(res)

print_result(2, 1000, 3, 5)
