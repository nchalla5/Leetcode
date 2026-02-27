class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_freq = max(task_counter.values())
        count = 0 
        for task,freq in task_counter.items():
            if freq == max_freq:
                count += 1
        return max(len(tasks),(1 + n)*(max_freq - 1) + count)