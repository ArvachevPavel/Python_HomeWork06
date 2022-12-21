import math

nums = []
gcds = []

while True:
    a = input()
    if not a:
        break
    nums.append(int(a))


gcds = [math.gcd(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]

print(gcds)

