N = int(input())
N = N if N <= 6 else exit()

# when something is removed, all of the things they invited are removed
# we need to track the combinations
# 2 combos are certain {none of them} or {all of them}
# the other combos is {some of them}, this one can be restrictive and non-restrictive
# let's tackle the restrictive one first

count = 0 # count all combos
