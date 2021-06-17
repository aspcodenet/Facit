# fakturadat = idag
# forfallodag = idag + 30 dagar
# om förfallodag är lördag -> fredagen innan
# om förfallodag är söndag -> måndagen efter

import datetime
import calendar
import swedishCalendar


datum = datetime.datetime.now()

print(datum.strftime("%Y-%m-%d %H:%M:%S"))
print(datum.strftime("%Y-%m-%d"))

print(f"År: {datum.year}")
print(f"Månad: {datum.month}")
print(f"Day: {datum.day}")
print(f"Hour: {datum.hour}")
print(f"Minute: {datum.minute}")
print(f"Second: {datum.second}")
print(f"Millisecond: {datum.microsecond/1000}")

weekday = datum.weekday()
print(f"Weekday: {weekday}")

#Skriva ut veckodag - finnas i annan import
print(calendar.day_name[weekday])

print(swedishCalendar.day_name[weekday])

#Att lägga på - ex fakturan ska betalas om 30 dagar
enddate = datum + datetime.timedelta(days=30)


#Dagar kvar till julafon?
datum1 = datetime.datetime.now()
datum2 = datetime.datetime(datum1.year,12,24)
diff = datum2 - datum1
print(diff.days)

