def merge(intervals):
    intervals.sort(key = lambda i: i[0]) # sorting by the start value
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = merged[-1][1]
        
        # if the intervals overlap
        if start <= lastEnd: 
            merged[-1][1] = max(end, lastEnd) # cahnge the end value of the last interval
        else:
            # if intervals don't overlap just append to the list
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[4,5]]))
