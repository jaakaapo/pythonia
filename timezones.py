import pytz
import arrow

DATETIME_DEFAULT_FORMAT = 'YYYY-MM-DDTHH:mm:ssZZ'

starttime = arrow.now().format(DATETIME_DEFAULT_FORMAT)
endtime = arrow.now().shift(hours=+70).format(DATETIME_DEFAULT_FORMAT)

print(type(starttime))
print(starttime)
print(endtime)