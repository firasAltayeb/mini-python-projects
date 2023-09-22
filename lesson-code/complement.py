import random

target = 8
nums = [random.randint(0, 9) for _ in range(5)]

print(f"nums is {nums}")
print(f"target is {target}")

comp_map = {}

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] + nums[j] == target:
#             print(f"{i} + {j}")
#             break

for i in range(len(nums)):
    print(f"map is {comp_map}")
    complement = target - nums[i]
    print(f"complement is {complement}")
    if complement in comp_map:
        print(f"{comp_map[complement]} + {i}")
        break
    comp_map[nums[i]] = i
