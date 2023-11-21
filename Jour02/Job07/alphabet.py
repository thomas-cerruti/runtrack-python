alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, len(alphabet) + 1):
    subset = alphabet[:i*2-1]
    repeated_subset = (subset * 2)[:i*2-1]
    print(repeated_subset)