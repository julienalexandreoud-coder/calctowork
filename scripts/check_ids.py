import json
from pathlib import Path
import itertools

data = json.load(open(r"C:\Microsaas\obra\src\calculators\calculators.json", encoding="utf-8"))
ids = sorted([int(c["id"]) for c in data["calculators"]])
print("Count:", len(ids))
print("Min:", min(ids), "Max:", max(ids))
ranges = []
for k, g in itertools.groupby(enumerate(ids), lambda x: x[0]-x[1]):
    group = list(g)
    ranges.append((group[0][1], group[-1][1]))
print("Ranges:", ranges)
