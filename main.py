###Solution to exercise 46 from ben stephenson's "the python workbook".

print('Enter the month and day:')
m, d = input().split(',')

this_month = m
day_of_month = int(d)
total_days = 0

spring_first = 79
summer_first = 172
fall_first = 265
winter_first = 355

monthdays = { 'january': 31,
              'february': 28,
              'march': 31,
              'april': 30,
              'may': 31,
              'june': 30,
              'july': 31,
              'august': 31,
              'september': 30,
              'october': 31,
              'november': 30,
              'december': 31 }

if this_month in monthdays.keys():
  if day_of_month > monthdays[this_month]:
    day_of_month = monthdays[this_month]


for i in monthdays.keys():
  total_days += monthdays[i]
  if i == this_month:
    total_days = total_days - monthdays[i] + day_of_month
    break

print(total_days)

if total_days < spring_first:
  print('It\'s still winter.')
elif total_days < summer_first:
  print('It\'s still spring.')
elif total_days < fall_first:
  print('It\'s still summer.')
elif total_days < winter_first:
  print('It\'s still fall.')
else:
  print('It\'s still winter.')
