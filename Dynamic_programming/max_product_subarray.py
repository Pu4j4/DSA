def max_product(nums):

    n = len(nums)
    max_product = float('-inf')

    for i in range(n):

        product = 1

        for j in range(i, n):

            product *= nums[j]
            max_product = max(max_product, product)

    return max_product