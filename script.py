import Final_DAQ
import sys

efficiency = 0
data = []

print(sys.argv)

if len(sys.argv) > 1:
  interval = int(sys.argv[1]) # Seconds between each measurement
  if len(sys.argv) > 2:
    num_intervals = int(sys.argv[2]) # Number of intervals measured
    if len(sys.argv) > 3:
        name = str(sys.argv[3]) # Name of the File


final = Final_DAQ.Final(efficiency, data)

final.acquire_data(interval, num_intervals, name)

final.parse_data()