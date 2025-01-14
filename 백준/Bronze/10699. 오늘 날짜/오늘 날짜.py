from datetime import datetime, timedelta

utc = datetime.now()

kst = utc + timedelta(hours=9)

seoul = str(kst)

print(seoul[:10])