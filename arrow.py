import time

w = 24
h = 20
initial = 0
for y in range(0,h):
	
	if y <= int(h/2):
		number_stars = 1
	else:
		initial +=1
		number_stars = initial*2 +1
	start_index = (w-number_stars)/2
	end_index = start_index + number_stars
	for x in range(0,w):
		if (start_index <= x <= end_index):
			print('\033[32m*', end='',flush = True)
		else:
			print('\033[97m.', end='',flush=True)
		time.sleep(.01)
	print('\033[0m')

