class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = [0] * self.n
        for i in range(self.n):
            self.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        index += 1
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1) if left > 0 else self.prefix_sum(right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
