class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [
            [pos_num1, pos_num2]
            for pos_num1, num1 in enumerate(nums)
            for pos_num2, num2 in enumerate(nums)
            if num1 + num2 == target
        ]
        return result[0]


s1 = Solution()

print(s1.twoSum(nums=[3, 2, 4], target=6))
