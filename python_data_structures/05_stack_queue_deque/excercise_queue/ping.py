from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.ping_list=[]

    def ping(self, t: int) -> int:
        # 1. 将当前请求加入队列
        self.queue.append(t)
        # 2. 移除不在 [t - 3000, t] 范围内的请求
        if t>3000:
            small=t-3000
            big=t
            index=0
            while(
                self.queue and
                (small>self.queue[0] or self.queue[0]>t)
            ):
                deque(self.queue)

        return len(self.queue)

