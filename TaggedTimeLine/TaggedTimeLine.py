# Author: @moran991231 (GitHub, Jaesun Park)
import time 


class TaggedTimeLine:
    # This is a kinkd of stopwatch with tag
    def __init__(self, cnt_limit=-1):
        self.start()
        self.accum = []
        self.cnt = 0 # count iteration 0,1,2, ...
        self.cnt_frame = 0 # incremented by function accumulate
        self.cnt_frame_limit = cnt_limit # stop doing accumulate when cnt_frame exceed cnt_frame_limit

    def start(self): # call this before call check or on the top of the loop
        self.times = []
        self.intervals = []
        self.check() # first tag is 

    def check(self, tag=" - "): # add a time info with tag
        self.times.append((tag, time.time()))

    def print_all(self, delimiter=""): # print all time intervals with their tags
        if len(self.times) <= 1:
            return
        if len(self.intervals) == 0:
            self.calc_all()
        builder = []
        for inv in self.intervals:
            builder.append(f"({inv[0]} {inv[1]:.4f} s){delimiter}")
        print(*builder)
        pass

    def print_tag(self, tag:str):
        # find a time with the given tag,
        # print the time interval between the given tag and its preceding tag 
        if len(self.times) <= 1:
            return
        for i, x in enumerate(self.times):
            if i==0:
                continue
            if x[0] == tag :
                print(f"{tag}:{x[1]-self.times[i-1][1]:.4f}s")
                return

    def print_interval(self, tag1:str, tag2:str): 
        # print the time interval between the given tag1 and tag2 
        if len(self.times) <= 2:
            return

        xx = []
        for x in self.times:
            if x[0] == tag1:
                xx.append(x)
            elif x[0] == tag2:
                xx.append(x)

        if len(xx) != 2:
            return
        print(f"{xx[0][0]}'s end ~ {xx[1][0]} : {xx[1][1]-xx[0][1]:.4f}s")

    def calc_all(self): # calculate all intervals in the self.times[]
        if len(self.times) <= 1:
            return
        for i in range(1, len(self.times)):
            prev = self.times[i - 1]
            cur = self.times[i]
            self.intervals.append((cur[0], cur[1] - prev[1]))
        self.intervals.append(("total", self.times[-1][1] - self.times[0][1]))

    def accumulate(self, increment: int):
        # accumlate the intervals to get average if only the number of tags isn't changed
        if len(self.intervals) == 0:
            self.calc_all()
        if len(self.accum) != len(self.intervals):
            self.accum = [0 for _ in self.intervals]  # Don't accumlate the first result
            return
        for i in range(len(self.accum)):
            self.accum[i] += self.intervals[i][1]
        self.cnt += 1
        self.cnt_frame += increment
        if self.cnt_frame_limit > 0 and self.cnt_frame_limit <= self.cnt_frame:
            return True
        else:
            return False

    def print_avg(self, delimiter=""):
        # print the result of accumulation as average
        builder = ["The average of accumulated latency per loop: \n"]
        for i in range(len(self.accum)):
            builder.append(
                f"({self.intervals[i][0]} {self.accum[i]/self.cnt:.4f} s){delimiter}"
            )
        print(*builder)