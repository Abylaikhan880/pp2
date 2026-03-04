from datetime import datetime

str1 = input()
str2 = input()

date1 = datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(str2, "%Y-%m-%d %H:%M:%S")

res = date2 - date1

print(res.total_seconds())