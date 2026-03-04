from datetime import datetime
from datetime import timedelta

crnt = datetime.now()

res = crnt - timedelta(days=5)
print(res)