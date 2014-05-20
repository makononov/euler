import datetime

d = datetime.date(1901, 01, 01)
count = 0
year = 1900
while d < datetime.date(2001, 01, 01):
	print "Testing %i/%i/%i" % (d.month, d.day, d.year)

	if d.weekday() == 6 and d.day == 1:
		count += 1
	if d.month == 12:
		d = d.replace(year = d.year+1, month=1)
	else:
		d = d.replace(month = d.month + 1)

print count

