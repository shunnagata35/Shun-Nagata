import csv, statistics
from datetime import datetime
import matplotlib.pyplot as plt

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

rcvMax = rcvList[0]
rcvMin = rcvList[-1]
rcvRange = rcvList[0] - rcvList[-1]
rcvMean = statistics.mean(rcvList)
rcvMedian = statistics.median(rcvList)


print("Max:", round(rcvMax, 3))
print("Min:", round(rcvMin, 3))
print("Range:", round(rcvRange, 3))
print("Mean:", round(rcvMean, 3))
print("Median:", round(rcvMedian, 3))

plt.title("RCV Histogram", fontsize=20)
plt.xlabel("RCV", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(True)

freqs, bins, patches = plt.hist(rcvList, bins=int(rcvRange/0.01))
# print(freqs)
# print(bins)

modeIndex = freqs.argmax()
rcvMode = round((bins[modeIndex] + bins[modeIndex+1])/2, 3)
print("Mode:", rcvMode)
print("Mode-mean:", abs(rcvMode - rcvMean))
print("Median-mean:", abs(rcvMedian - rcvMean))

# plt.savefig("rcv-" + today + ".png")
plt.show()
