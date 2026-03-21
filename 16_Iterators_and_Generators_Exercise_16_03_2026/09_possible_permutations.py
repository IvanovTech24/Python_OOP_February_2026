import itertools

def possible_permutations(ls):
    for perm in itertools.permutations(ls):
        yield list(perm)



# def possible_permutations(ls):
#     if len(ls) <= 1:
#         yield ls
#     else:
#         for i in range(len(ls)):
#             print(f"Разглеждам: {ls}")
#             for perm in possible_permutations(ls[:i] + ls[i+1:]):
#                 yield [ls[i]] + perm



# def get_permutations(ls):
#     if len(ls) <= 1:
#         return [ls]
#
#     all_perms = []
#
#     for i in range(len(ls)):
#         current_element = ls[i]
#         remaining_elements = ls[:i] + ls[i+1:]
#         sub_permutations = get_permutations(remaining_elements)
#
#         for p in sub_permutations:
#             combined = [current_element] + p
#             all_perms.append(combined)
#
#     return all_perms

# result = get_permutations([1, 2, 3])
# print(result)



[print(n) for n in possible_permutations([1, 2, 3])]
print("=========================================")
[print(n) for n in possible_permutations([1])]
