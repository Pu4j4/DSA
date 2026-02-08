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


#optimized
def product_self(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

nums = [1,2,4,6]
print(product_self(nums))