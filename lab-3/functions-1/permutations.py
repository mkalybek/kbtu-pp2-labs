from itertools import permutations

def all_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
