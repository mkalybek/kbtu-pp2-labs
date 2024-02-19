from datetime import datetime

date1 = datetime(2024, 2, 15, 12, 0, 0)
date2 = datetime(2024, 2, 20, 14, 30, 15)

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()
print("Diff in seconds:", difference_in_seconds)
