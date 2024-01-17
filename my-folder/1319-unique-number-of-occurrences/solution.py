class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = Counter(arr)
        hash_set = set(hash_map.values())
        return len(hash_map) == len(hash_set)
