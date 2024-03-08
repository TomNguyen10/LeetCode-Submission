class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
    
        max_freq = max(freq_counter.values())
    
        max_freq_elements_count = sum(1 for freq in freq_counter.values() if freq == max_freq)
    
        return max_freq_elements_count * max_freq
