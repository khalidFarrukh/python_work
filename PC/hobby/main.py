import copy
import random


def initialize_population(_p, i_p):
    i = 0
    for c in _p:
        _p[c][0] = i_p[i]
        i += 1
    return _p


def Find_x_value_of_chromosome(_p):
    length = 0
    sum = 0
    for c in _p:
        length = len(_p[c][0])
        p = length - 1
        si = 0

        # converting binary chromosomes into decimal X value
        decimal = 0
        while si < length:
            bit = int(_p[c][0][si])
            decimal += bit * (2 ** p)
            p -= 1
            si += 1
        _p[c][1] = decimal
        sum += decimal
    return _p, sum, length


def fitness_val_function(_p):
    for c in _p:
        r = -1.0 * (((_p[c][1]) ** 2.0) / 10.0) + (3.0 * _p[c][1])
        r = float("{:.1f}".format(r))
        if r > 31:
            _p[c][2] = 0
        _p[c][2] = r
    return _p


def selection_probability(_p, sig_sum):
    for c in _p:
        _p[c][3] = float("{:.1f}".format(((_p[c][2] * 1.0) / (sig_sum * 1.0)) * 100))
    return _p


def any_selection_prob_greater_than(inum, _p):
    for c in _p:
        if _p[c][3] >= inum:
            return True
    return False


def Reproduction(_p, length):
    i = 1
    i_p = []
    random.seed()
    length = len(_p)
    while i < length:
        if _p[str(i)][4] == False:
            _p[str(i)][4] = True
            cross1 = _p[str(i)][0]
            cross2 = None
            while True:
                j = random.randrange(1, 11)
                if j != i and _p[str(j)][4] == False:
                    point = random.randrange(1, 4)
                    print("single point cross over location = ", point)
                    _p[str(j)][4] = True
                    cross2 = _p[str(j)][0]
                    print("parents : ", cross1, " < - > ", cross2)
                    c1a = cross1[:point]
                    c1b = cross1[point:]
                    c2a = cross2[:point]
                    c2b = cross2[point:]
                    temp1 = c1a + c2b
                    temp2 = c2a + c1b
                    print("childs  : ", temp1, " ***** ", temp2)
                    print("\n")
                    i_p.append(temp1)
                    i_p.append(temp2)
                    break
        i += 1
    return i_p


def Mutation(i_p):
    random.seed()
    j = 0
    i = 0
    length = len(i_p)
    while i < length:
        j = random.randrange(0, 5)
        if i_p[i][j] == "0":
            i_p[i] = i_p[i][:j] + "1" + i_p[i][j + 1 :]
        elif i_p[i][j] == "1":
            i_p[i] = i_p[i][:j] + "0" + i_p[i][j + 1 :]
        i += 1
    return i_p


# def convert_decimal_to_binary_list_of_strings(_p,length):
#     i_p=[]
#     str1 = ""
#     i=0
#     while i<length:
#         str1+="0"
#         i+=1
#     for c in _p:
#         TLength = length-1
#         str2 = copy.deepcopy(str1)
#         number = _p[c][3]
#         while TLength>-1:
#             rem = int(number%2)
#             number = int(number/2)
#             str2 = str2[:TLength] + str(rem) + str2[TLength+1:]
#             TLength-=1
#         i_p.append(str2)
#     return i_p


initial_population = [
    "01011",
    "11010",
    "00010",
    "01110",
    "01100",
    "11110",
    "10110",
    "01001",
    "00011",
    "10001",
]

gen = 0
while True:
    _population = {
        "1": [None, None, None, None, False],
        "2": [None, None, None, None, False],
        "3": [None, None, None, None, False],
        "4": [None, None, None, None, False],
        "5": [None, None, None, None, False],
        "6": [None, None, None, None, False],
        "7": [None, None, None, None, False],
        "8": [None, None, None, None, False],
        "9": [None, None, None, None, False],
        "10": [None, None, None, None, False],
    }
    _population = initialize_population(_population, initial_population)
    _population, sigma_sum, length = Find_x_value_of_chromosome(_population)
    _population = fitness_val_function(_population)
    _population = selection_probability(_population, sigma_sum)
    for c in _population:
        print(c + " : ", end="")
        for d in _population[c]:
            print("\t", d, end="")
        print()
    print("\n")
    if any_selection_prob_greater_than(55.0, _population) == True:
        break
    initial_population = Reproduction(_population, length)
    if gen == 3:
        initial_population = Mutation(initial_population)
        gen = 0
    # print(initial_population)
    # initial_population = convert_decimal_to_binary_list_of_strings(_population,length)
    # print(initial_population)
    gen += 1
