def insert(intervals, new_interval):
    # insert new_interval into merged intervals
    new_interval_start = new_interval[0]

    if new_interval_start < intervals[0][0]:
        intervals.insert(0, new_interval)
    elif new_interval_start > intervals[-1][0]:
        intervals.append(new_interval)
    else:
        for i in range(len(intervals)-1):
            if new_interval_start > intervals[i][0] and new_interval_start < intervals[i+1][0]:
                intervals.insert(i+1, new_interval)
                
    return mergeIntervals(intervals)

def mergeIntervals(intervals):
    # merge any overlapping intervals
    merged = [intervals[0]]
    for start, end in intervals:
        lastEnd = merged[-1][1]

        if start <= lastEnd:
            merged[-1][1] = max(end, lastEnd)
        else:
            merged.append([start, end])

    return merged

print(insert([[1,3], [5,7], [8,12]], [4,6]))
print(insert([[1,3], [5,7], [8,12]], [4,10]))
print(insert([[2,3],[5,7]], [1,4]))