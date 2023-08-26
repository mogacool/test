# Нужно посчитать количество символов в строке (по каждой букве)
# aabbssddfs

# def str_counter(s): # N**2
    # for sym in s:
    #     counter = 0
    #     for sub_sym in s:
    #         if sym == sub_sym:
    #             counter += 1
    #     print(sym, counter)

# def str_counter(s): # N*M
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

def str_counter(s): # N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)

# 9^2 = 81  log9 81 = 2

# log2 N = 3
lst = [1, 5, 10, 60, 1000, 7000, 7050, 10000]
elem = 1050

# n! 2^n

str_counter("aabbssddfs")