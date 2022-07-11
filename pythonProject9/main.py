'''from datetime import *
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("current time is:", currentTime)
time=datetime.now().time()
print("current time:",time)'''

import datetime
current_time=datetime.datetime.now()
print("current date and time is:",current_time)


from datetime import datetime, timedelta
presentday = datetime.now()
yesterday = presentday-timedelta(1)
tomorrow = presentday+timedelta(1)
print("yesterday:", yesterday.strftime("%d-%m-%Y"))
print("today:", presentday.strftime("%d-%m-%Y"))
print("tomorrow:", tomorrow.strftime("%d-%m-%Y"))



