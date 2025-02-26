import sys

def min_moves(nums):
    median = sorted(nums)[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    with open(sys.argv[1], "r") as file:
        nums = [int(line.strip()) for line in file]

print(min_moves(nums))