""" Problem Statement

Given a list of intervals, merge all overlapping intervals and return the merged intervals. """


def merge_intervals(intervals):
    intervals.sort()
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example
intervals = [[1,3],[2,6],[8,10],[15,18]]

print("Merged Intervals:", merge_intervals(intervals))
