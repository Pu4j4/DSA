#Brute force
def  product_self(nums):
    n = len(nums)
    res = [1] * n
    for i in range(n):
        product = 1
        for j in range(n):
            if j == i:
                continue
            product *= nums[j]
        res[i] = product
    return res
nums = [1,2,4,6]
print(product_self(nums))

