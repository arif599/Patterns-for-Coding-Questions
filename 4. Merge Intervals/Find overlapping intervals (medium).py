def findOverlap(intervals):
    intervals.sort(key = lambda i: i[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = merged[-1][1]

        if start <= lastEnd:
            # overlap
            return [start, end], merged[-1]
        else:
            merged.append([start, end])
            
if __name__ == "__main__":
    print(findOverlap([[1,4], [2,5], [7,9]]))
    print(findOverlap([[1,4], [5,7], [7,9]]))