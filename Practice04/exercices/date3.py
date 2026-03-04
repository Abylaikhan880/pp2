from datetime import datetime

now = datetime.now()

res = now.replace(microsecond=0)
print(res)