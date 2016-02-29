class Solution(object):
    def jump(self, nums):
        step, last_max, cur_max = 0, 0, 0
        
        for i in range(len(nums) - 1):
            cur_max = max(cur_max, i + nums[i])
            if i == last_max:
                step += 1
                last_max = cur_max
                
        return step