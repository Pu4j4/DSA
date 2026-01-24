#brute force
from collections import Counter
def least_interval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    count_max = sum(1 for v in freq.values() if v == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + count_max)

#optimized
def least_interval(tasks, n):
    freq = Counter(tasks)
    cooldown = {}
    time = 0

    while freq:
        available = []
        for task in freq:
            if task not in cooldown or cooldown[task] <= time:
                available.append(task)

        if available:
            task = max(available, key=lambda x: freq[x])
            freq[task] -= 1
            if freq[task] == 0:
                del freq[task]
            cooldown[task] = time + n + 1

        time += 1

    return time



