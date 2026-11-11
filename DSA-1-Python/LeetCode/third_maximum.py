nums = [10, 10, 8, 5]

nums = list(set(nums))
nums.sort()

print(nums[-1])
print(nums[-2])
print(nums[-3])

# alternative sol
class Solution:
    def thirdMax(self, nums):
        unique_nums = sorted(set(nums))

        if len(unique_nums) < 3:
            return unique_nums[-1]

        return unique_nums[-3]


obj = Solution()

nums = [98, 43, 78, 65, 100]

print(obj.thirdMax(nums))