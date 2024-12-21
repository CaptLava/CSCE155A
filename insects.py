
'''
class Dragonfly:
	def __init__(self):
		self.legs = 6
		self.pairs_of_wings = 2
		self.species = 'Dragonfly'
	def display(self):
		print(f'Insect species: {self.species}. It has {self.legs} legs, and {self.pairs_of_wings} wings')

class Spider:
	def __init__(self):
		self.legs = 8
		self.pairs_of_wings = 0
		self.species = 'Spider'
	def display(self):
		print(f'Insect species: {self.species}. It has {self.legs} legs, and {self.pairs_of_wings} wings')

class Cicadas:
	def __init__(self):
		self.legs = 6
		self.pairs_of_wings = 1
		self.species = 'Cicada'
	def display(self):
		print(f'Insect species: {self.species}. It has {self.legs} legs, and {self.pairs_of_wings} wings')








dragonfly = Dragonfly()
spider = Spider()
cicada = Cicadas()

dragonfly.display()
spider.display()
cicada.display()
'''


class Insect:
	def __init__(self,a,b,c):
		self.legs = a
		self.pairs_of_wings = b
		self.species = c
	def display(self):
		print(f'Insect species: {self.species}. It has {self.legs} legs, and {self.pairs_of_wings} wings')

total_num = int(input('Enter total number of insects:'))
total_legs = int(input('Enter total number of legs:'))
total_wings = int(input('Enter total number of wings: '))

def calculate_spider_and_others(dragonfly,spider):
	num_of_other_than_spiders = (total_num * spider.legs - total_legs)/(spider.legs - dragonfly.legs)
	return total_num - num_of_other_than_spiders, num_of_other_than_spiders

def calculate_dragonfly_and_cicada(other_num, dragonfly, cicada):
	cicada_num = (other_num * dragonfly.pairs_of_wings - total_wings)/ (dragonfly.pairs_of_wings - cicada.pairs_of_wings)
	return other_num - cicada_num, cicada_num

dragonfly = Insect(6,2,'dragonfly')
cicada = Insect(6,1,'cicada')
spider = Insect(8,0,'spider')



spider_count, other_count = calculate_spider_and_others(dragonfly, spider)

dragonfly_count, cicada_count = calculate_dragonfly_and_cicada(other_count, dragonfly, cicada)
print(f'Spiders: {spider_count}, Cicadas: {cicada_count}, Dragonflies: {dragonfly_count}')



















dragonfly.display()
spider.display()
cicada.display()













