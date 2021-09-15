from calendar import monthrange
from dateutil.easter import easter as get_easter
from datetime import date, timedelta


def get_holydays(year):
	holydays = {
		# anul nou
		date(year, 1, 1),
		# craciun pe stil vechi
		date(year, 1, 7),
		# sarbatoarea craciunul pe stil vechi
		date(year, 1, 8),
		# ziua internationala a femeii
		date(year, 3, 8),
		# siua muncii
		date(year, 5, 1),
		# ziua victoriei
		date(year, 5, 9),
		# ziua copiilor
		date(year, 6, 1),
		# ziua independentei
		date(year, 8, 27),
		# ziua nationala a limbii
		date(year, 8, 31),
		# craciun pe stil nou
		date(year, 12, 25),
	}

	# prima zi de pasti
	easter = get_easter(year, 2)
	holydays.add(easter)
	# doua zi de pasti
	holydays.add(easter + timedelta(days=1))
	# pastele blajeni
	holydays.add(easter + timedelta(days=8))
	return holydays


def month(year, month, today):
	months = [
		'Ianuarie', 'Februarie', 'Martie', 
		'Aprilie', 'Mai', 'Iunie',
		'Iulie', 'August', 'Septembrie',
		'Octombrie', 'Noiembrie', 'Decembrie'
	]
	holydays = get_holydays(year)
	style = {
		# weekend
		'w': '\x1b[2;30;90m%s\x1b[0m',
		# holidays
		'h': '\x1b[2;30;43m%s\x1b[0m',
		# past
		'p': '\x1b[2;35;40m%s\x1b[0m',
	}
	week_name = 'Lu Ma Mi Jo Vi Si Du'
	week_start, week_days = monthrange(year, month)

	title = '%s %s' % (months[month], year)
	title_len = len(week_name) // 2 + len(title) // 2
	lines = [title.rjust(title_len), week_name]
	line = ['  ' for i in range(week_start)]

	for week_day in range(1, week_days + 1):
		day = date(year, month, week_day)
		day_str = str(day.day).rjust(2)

		if day in holydays:
			day_str = style['h'] % (day_str)
		elif day.weekday() > 4:
			day_str = style['w'] % (day_str)
		elif day <= today:
			day_str = style['p'] % (day_str)

		line.append(day_str)

		if day.weekday() == 6:
			lines.append(' '.join(line))
			line = []
	return lines


# console colors 
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

today = date.today()
m = month(today.year, today.month, today)
print("\n".join(m))
