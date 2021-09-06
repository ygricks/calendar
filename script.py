from calendar import monthrange
from dateutil.easter import easter
from datetime import date

today = date.today()
free = {
	date(today.year, 1, 1), # anul nou
	date(today.year, 1, 7), # craciun pe stil vechi
	date(today.year, 1, 8), # sarbatoarea craciunul pe stil vechi
	date(today.year, 3, 8), # ziua internationala a femeii
	date(today.year, 5, 1), # siua muncii


	date(today.year, 5, 3), # doua zi de pasti
	date(today.year, 5, 9), # ziua victoriei
	date(today.year, 5, 10), # pastele blajeni
	date(today.year, 6, 1), # ziua copiilor
	date(today.year, 8, 27), # ziua independentei
	date(today.year, 8, 31), # ziua nationala a limbii
	date(today.year, 12, 25), # craciun pe stil nou
}
# prima zi de pasti
free.add(easter(today.year, 2))
print()


def month(year, month):
	months = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August',
	'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']
	week_name = 'Lu Ma Mi Jo Vi Si Du'
	week_start, week_days = monthrange(year, month)

	title = '%s %s' % (months[month], year)
	title_len = len(week_name) // 2 + len(title) // 2
	lines = [title.rjust(title_len), week_name]
	line = []
	start = week_start * -1 + 1
	for i in range(start, week_days + 1):
		day = str(i).rjust(2) if i > 0 else '  '
		if i % 7 == 4 or i % 7 == 5:
			# line.append('\033[96m%s\033[0m' % (day))
			line.append('\x1b[3;33;40m%s\x1b[0m' % (day))
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
