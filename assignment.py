def calc(x, y, z):
    print("_________")
    print((y + x) / 2)
    print((x - z) / 2)
    print((x + z) / 2)
    print("_________")


def generate_permutations(nums):
    # Create all permutations with positive/negative combinations
    for a in [nums[0], -nums[0]]:
        for b in [nums[1], -nums[1]]:
            for c in [nums[2], -nums[2]]:
                calc(a, b, c)


# Generate all permutations
generate_permutations([2, 6, 4])
