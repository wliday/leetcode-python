class Solution(object):
    def findKthLargest(self, nums, k):
        self.buildMinHeap(nums, k)

        print nums
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[0], nums[i] = nums[i], nums[0]
                self.minHeapify(nums, 0, k)

        return nums[0]

    def minHeapify(self, nums, idx, k):
        lson = idx * 2 + 1
        rson = idx * 2 + 2

        smallest = idx
        if lson < k and nums[lson] < nums[idx]:
            smallest = lson

        if rson < k and nums[rson] < nums[smallest]:
            smallest = rson

        if smallest != idx:
            nums[smallest], nums[idx] = nums[idx], nums[smallest]
            self.minHeapify(nums, smallest, k)

    def buildMinHeap(self, nums, k):
        for i in range(k >> 1, -1, -1):
            self.minHeapify(nums, i, k)