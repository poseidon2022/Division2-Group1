class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        my_list = list()
        d = intervals[0][1]
        inter = intervals[0]
        second = intervals[0][1]
        for i in range(len(intervals)-1):
            if d >= intervals[i+1][0]:
                second = intervals[i+1][1] if intervals[i+1][1]>second else second
                inter = [inter[0],second]
                d = inter[1]
            else:
                my_list.append(inter)
                inter = intervals[i+1]
                d = inter[1]
                second = intervals[i+1][1]
        my_list.append(inter)
        return my_list