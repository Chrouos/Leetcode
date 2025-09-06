class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_num = {}
        for index, i in enumerate(nums, start=0):
            if dict_num.get(target - i) != None and dict_num.get(target - i) != index:
                return [dict_num[target - i], index]
            
            dict_num[i] = index
            
        return None
    
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))