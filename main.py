from Def import *
import random
import pprint
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
        #Mixer chromosome
        self.Mchromosome=Chromosome(length)
        self.Mchromosome.initChromosom()
        self.Mlength=length

    def initialize(self):
        ''' loop over jobs list for each product
        loop for the number of slots needed by each product
        randomly add product to genearray
         '''        
        # for i in jobs:
        #     for j in range(int(i.totaltime)):
        #         self.chromosome.geneArray[random.randrange(0, self.chromosome.genes)].append(i)                

        #Schedule Mixers chromosome
        counter = 0
        for i in jobs:
            #Mixing time + mixer cleaning time
            # while( counter < int(i.cTime + i.MNO.cT)):
            for j in range(int(i.cTime + i.MNO.cT)):
                self.Mchromosome.geneArray[random.randrange(0,  self.Mchromosome.genes)].append(i)
                print(i)
                counter +=1
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
    
# pp = pprint.PrettyPrinter(indent=24, compact=True)


def displayPop(population):
    displaylist = [] 
    for i in population:
        displaylist.append(i)
    print("Generation 1")
    print(displaylist[0])
    print("Generation 2")
    print(displaylist[1])

def start():
    pop = CreateInitPop(12,2)

    displayPop(pop)

start()    