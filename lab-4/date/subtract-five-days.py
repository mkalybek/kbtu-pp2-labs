from datetime import datetime, timedelta

five_days_ago = datetime.now() - timedelta(days=5)

print("Five days ago: " + five_days_ago.strftime("%Y-%m-%d"))