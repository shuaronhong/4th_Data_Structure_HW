class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) <= 1:
            return len(tasks)

        t_count = collections.defaultdict(int)
        for task in tasks:
            t_count[task] -= 1

        pqueue = []
        for t in t_count.keys():
            heapq.heappush(pqueue, (t_count[t], t))

        res = 0
        while pqueue:
            i = 0
            tmp_task = []
            while i <= n:
                if len(pqueue) > 0:
                    elem = heapq.heappop(pqueue)
                    count = elem[0]
                    task = elem[1]
                    if count < -1:
                        tmp_task.append((count + 1, task))
                res += 1
                if len(pqueue) == 0 and tmp_task == []:
                    break
                i += 1
            for t in tmp_task:
                heapq.heappush(pqueue, t)
        return res