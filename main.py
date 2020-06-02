from Def import *
import random
class Chromosome(object):
	def __init__(self, length):
		self.genes=length
        #Array of genes
		self.geneArray = []

	def initChromosom(self):
		for i in range(0,self.genes):
			self.geneArray.append([])        
	def __str__(self):
		return str(self.geneArray)

class fitness(object):
	def __init__(self, individual):
		self.schedule = individual
		self.score=0

class Schedule(object):
    def __init__(self, length):        
        self.chromosome=Chromosome(length)
        self.chromosome.initChromosom()
        self.length=length

    def initialize(self):
        ''' loop over jobs list for each product
        loop for the number of slots needed by each product
        randomly add product to genearray
         '''
        print("in initailize")
        for i in jobs:
            for j in range(int(i.totaltime)):
                self.chromosome.geneArray[random.randrange(0, self.chromosome.genes)].append(i)                
    def __repr__(self):
        return str(self.chromosome.geneArray)

def crossover(a,b):
    pass

def mutate():
    pass

def CreateInitPop(length, gensize):
    generation = []
    i = 0
    while (i < gensize):
        schedule = Schedule(length)
        schedule.initialize()
        generation.append(schedule)
        i += 1
    return generation

def displayPop(population):
	displaylist=[]
	for i in population:
		displaylist.append(i)
	print(displaylist)

def start():
    pop = CreateInitPop(5,1)

    displayPop(pop)

start()    