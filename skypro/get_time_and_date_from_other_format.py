from datetime import datetime

thedate = datetime.fromisoformat("2020-12-06 23:14")

print(thedate.year)
print(thedate.month)
print(thedate.day)

print(thedate.hour)
print(thedate.minute)

# Выведет:
#
# 2020
# 12
# 6
# 23
# 14