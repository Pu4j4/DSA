def max_product(nums):

    n = len(nums)
    max_product = float('-inf')

    for i in range(n):

        product = 1

        for j in range(i, n):

            product *= nums[j]
            max_product = max(max_product, product)

    return max_product



def max_product(nums) -> int:
    curr_max = nums[0]
    curr_min = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):

        num = nums[i]

        if num < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(num, curr_max * num)
        curr_min = min(num, curr_min * num)

        result = max(result, curr_max)

    return result

nums = [2,3,-2,4]
print(max_product(nums))