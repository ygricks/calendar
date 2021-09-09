from calendar import monthrange
from dateutil.easter import easter as get_easter
from datetime import date, timedelta

today = date.today()
def get_holydays(year):
	holydays = {
		date(year, 1, 1), # anul nou
		date(year, 1, 7), # craciun pe stil vechi
		date(year, 1, 8), # sarbatoarea craciunul pe stil vechi
		date(year, 3, 8), # ziua internationala a femeii
		date(year, 5, 1), # siua muncii
		date(year, 5, 9), # ziua victoriei
		date(year, 6, 1), # ziua copiilor
		date(year, 8, 27), # ziua independentei
		date(year, 8, 31), # ziua nationala a limbii
		date(year, 12, 25), # craciun pe stil nou
	}

	# prima zi de pasti
	easter = get_easter(year, 2)
	holydays.add(easter)
	# doua zi de pasti
	holydays.add(easter + timedelta(days=1))
	# pastele blajeni
	holydays.add(easter + timedelta(days=8))
	return holydays


def month(year, month):
	months = [
		'Ianuarie', 'Februarie', 'Martie', 
		'Aprilie', 'Mai', 'Iunie',
		'Iulie', 'August', 'Septembrie',
		'Octombrie', 'Noiembrie', 'Decembrie'
	]
	style = {
		'h': '\x1b[2;30;90m%s\x1b[0m'
	}
	week_name = 'Lu Ma Mi Jo Vi Si Du'
	week_start, week_days = monthrange(year, month)

	title = '%s %s' % (months[month], year)
	title_len = len(week_name) // 2 + len(title) // 2
	lines = [title.rjust(title_len), week_name]
	line = []
	start = week_start * -1 + 1
	for i in range(start, week_days + 1):
		day = str(i).rjust(2) if i > 0 else '  '
		if i % 7 in (4, 5):
			# line.append('\033[96m%s\033[0m' % (day))
			line.append(style['h'] % (day))
			# line.append('\x1b[3;33;40m%s\x1b[0m' % (day))

			# line.append('\x1b[0;35;40m%s\x1b[0m' % (day))
			# line.append('\x1b[2;38;40m%s\x1b[0m' % (day))
			# line.append('\x1b[3;37;40m%s\x1b[0m' % (day))
			# all colors https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
		else:
			line.append(day)
		if i % 7 == 5:
			lines.append(' '.join(line))
			line = []
	return lines


m = month(today.year, today.month)
print("\n".join(m))
