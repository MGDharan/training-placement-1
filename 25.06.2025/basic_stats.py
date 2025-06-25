# Filename:  basic_stats.py
import statistics

def calculate_stats(data):
    if not data:
        return {"mean": None, "median": None, "stdev": None}
    mean = statistics.mean(data)
    median = statistics.median(data)
    stdev = statistics.stdev(data)
    return {"mean": mean, "median": median, "stdev": stdev}

data = [1, 2, 3, 4, 5]
stats = calculate_stats(data)
print(stats)

data2 = []
stats2 = calculate_stats(data2)
print(stats2)