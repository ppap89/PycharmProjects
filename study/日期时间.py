from datetime import  datetime
now = datetime.now()
print(now)

print(type(now))

dt  = datetime(2021,9,18,11,27)  #创建datetime
print(dt)

t = dt.timestamp() ##time转换timestamp(float)
print(datetime.fromtimestamp(t)) #timestamp转换time
print(datetime.utcfromtimestamp(t)) #timestamp转换UTCtime

strday = datetime.strptime('2021-09-18 11:27:00','%Y-%m-%d %H:%M:%S')  #str转换datetime
print(strday)

print(now.strftime('%Y,%m,%d,%H,%M')) #date转str

from datetime import timedelta
print(now)
print(now + timedelta(days=1,hours=2))

from datetime import timezone ,timedelta
utc8 = timezone(timedelta(hours=8))
print(utc8)
dt=now.replace(tzinfo=utc8)
print(dt)

def to_timestamp(dt_str, tz_str):
    utcdt = dt_str.replace(tzinfo = timezone.utc)
    bjt = utcdt.astimezone(timezone(tmedelta(hours=8)))
    time=timestamp（bjt）
    print(time)

