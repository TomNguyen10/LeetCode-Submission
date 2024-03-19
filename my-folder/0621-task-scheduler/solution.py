class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        max_freq = max(task_counts)
        max_freq_tasks = task_counts.count(max_freq)
        
        min_intervals = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        return max(len(tasks), min_intervals)

