import csv
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



rcvPlayerNameList = []
avgPlayerNameList = []
rcvList = []
avgList = []

dt = datetime.now().isoformat()
today = dt.split("T")[0]

with open("rcv-" + today + ".csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        if len(row) < 2:
            print(f"complete row: {row}")
            continue
        try:
            rcvPlayerNameList.append([float(row[0]), row[1]])
            rcvList.append(float(row[0]))
        except ValueError as ve:
            print(f"Skipping row with invalid data: {row} ({ve})")
            
with open("avg-" + today + ".csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        if len(row) < 2:
            print(f"complete row: {row}")
            continue
        try:
            avgPlayerNameList.append([float(row[0]), row[1]])
            avgList.append(float(row[0]))
        except ValueError as ve:
            print(f"Skipping row with invalid data: {row} ({ve})")



x = np.array(rcvList)
y = np.array(avgList)
    


plt.scatter(x, y)
plt.show()
