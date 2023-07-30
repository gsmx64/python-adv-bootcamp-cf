# Usando slices para modificar listas

nums = [1, 2, 3, 4, 5]

nums[1:3] = [0, 0, 0, 0, 0]
# range(1, 5) -> [1, 2, 3, 4]
print(nums)
