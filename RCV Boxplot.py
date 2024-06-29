import csv
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

rcvPlayerNameList = []
rcvList = []

dt = datetime.now().isoformat()
today = dt.split("T")[0]

with open("rcv-" + today + ".csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        if len(row) < 2:
            print(f"complete row: {row}")
            continue
        try:
            rcvPlayerNameList.append([float(row[0]), row[1]])
            rcvList.append(float(row[0]))
        except ValueError as ve:
            print(f"Skipping row with invalid data: {row} ({ve})")

# print(rcvPlayerNameList)
# print(rcvList)

rcvMax = max(rcvList)
rcvMin = min(rcvList)
rcvRange = rcvMax - rcvMin
rcvMean = statistics.mean(rcvList)
rcvMedian = statistics.median(rcvList)
q1, q2, q3 = np.percentile(rcvList, [25, 50, 75])
iqr = q3 - q1
rightWhisker = q3 + 1.5 * iqr
leftWhisker = q1 - 1.5 * iqr


print("Max:", round(rcvMax, 3))
print("Min:", round(rcvMin, 3))
print("Range:", round(rcvRange, 3))
print("Mean:", round(rcvMean, 3))
print("Median:", round(rcvMedian, 3))
print("Q1:", round(q1, 3))
print("Q2:", round(q2, 3))
print("Q3:", round(q3, 3))
print("IQR:", round(iqr, 3))
print("rightWhisker:", round(rightWhisker, 3))
print("leftWhisker:", round(leftWhisker, 3))



plt.figure(figsize=(10, 6))
plt.boxplot(rcvList, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))


plt.title("RCV Boxplot", fontsize=20)
plt.xlabel("RCV", fontsize=14)
plt.grid(True)



plt.show()
