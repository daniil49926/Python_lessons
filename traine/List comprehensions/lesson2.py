"""
TASK01

import random

original_prices = [random.randint(-50, 150) for i in range(5)]
new_prices = original_prices[:]
for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print(f"Мы потеряли:  {abs(sum(original_prices) - sum(new_prices))}")
"""
"""
TASK02

nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
print(f"{nums[:5]}\n"
      f"{nums[:len(nums) - 2]}\n"
      f"{nums[::2]}\n"
      f"{nums[1::2]}\n"
      f"{nums[::-1]}\n"
      f"{nums[::-2]}\n")
"""

