from datetime import datetime
import calendar
yıl= datetime.now().year
i=1
while i<13:
  print(calendar.month(yıl, i))
  i+=1


