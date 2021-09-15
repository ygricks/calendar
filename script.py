from calendar import monthrange
from dateutil.easter import easter as get_easter
from datetime import date, timedelta


class ColoredDay:
	colors = {
		'black': 30,
		'red': 31,
		'green': 32,
		'yellow': 33,
		'blue': 34,
		'pink': 35,
		'sky': 36,
		'white': 37,
	}
	backgrounds = {
		'black': 40,
		'red': 41,
		'green': 42,
		'yellow': 43,
		'blue': 44,
		'pink': 45,
		'sky': 46,
		'white': 47,
		'grey': 90,
	}

	def __init__(self, day, **kwargs):
		self.day = day
		self.color = self.background = None
		if len(kwargs):
			self.let(**kwargs)

	def let(self, **kwargs):
		is_color = 'color' in kwargs and kwargs['color'] in self.colors
		self.color = self.colors[kwargs['color']] if is_color else None
		is_background = 'background' in kwargs and kwargs['background'] in self.backgrounds
		self.background = self.backgrounds[kwargs['background']] if is_background else None
		self.style = kwargs['style'] if 'style' in kwargs else 0

	def __repr__(self):
		if not self.color and not self.background:
			return self.day
		self.color = self.color if self.color else self.colors['white']
		self.background = self.background if self.background else self.backgrounds['black']
		if not self.style:
			self.style = 1 if self.color == self.colors['white'] or self.backgrounds == self.backgrounds['black'] else 0
		return '\x1b[%d;%d;%dm%s\x1b[0m' % (self.style, self.color, self.background, self.day)


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

	week_name = 'Lu Ma Mi Jo Vi Si Du'
	
	holydays = get_holydays(year)
	week_start, week_days = monthrange(year, month)
	title = '%s %s' % (months[month], year)
	title_len = len(week_name) // 2 + len(title) // 2
	lines = [title.rjust(title_len), week_name]
	line = ['  ' for i in range(week_start)]
	free = []

	for week_day in range(1, week_days + 1):
		day = date(year, month, week_day)
		str_day = str(day.day).rjust(2)
		cd = ColoredDay(str_day)
		is_busy = True

		if day in holydays:
			cd.let(background="yellow")
			is_busy = False
		elif day.weekday() > 4:
			cd.let(background="grey")
			is_busy = False
		elif day < today:
			cd.let(color="pink")
			is_busy = False

		if day == today:
			cd.let(color="red", style=1)

		if is_busy:
			free.append(str_day)

		line.append(str(cd))

		if day.weekday() == 6:
			lines.append(' '.join(line))
			line = []
	if len(line):
		lines.append(' '.join(line))
	if len(free):
		lines.append('')
		lines.append('more working days: %d' % len(free))
		lines.append(' '.join(free))
		lines.append(' '.join([str(i).rjust(2) for i in range(len(free), 0, -1)]))
	return lines


# console colors 
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

today = date.today()
m = month(today.year, today.month, today)
print("\n".join(m))
