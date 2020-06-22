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
        #Storage Tank Chromosome
        self.STchromosome = Chromosome(length)
        self.STchromosome.initChromosom()
        self.STlength = length
        #Production Line Chromosome
        self.PLchromosome = Chromosome(length)
        self.PLchromosome.initChromosom()
        self.PLlength = length

    def initialize(self):
        ''' loop over jobs list for each product
        loop for the number of slots needed by each product
        randomly add product in random time slots to genearray
        '''        
        #Schedule Mixers chromosome
        for i in jobs:            
            #Mixing total time: Mixing time + mixer cleaning time
            MTT = i.cTime + i.MNO.cT
            if (i.isOutSourced == True):
                Tobestored.append(i)
            else:         
                #Step = no. of needed continous slots       
                for j in range(0, MTT, 2):
                    k = random.randrange(0,  self.Mchromosome.genes-1)                
                    if (len(self.Mchromosome.geneArray[k]) == 0):
                    #Constrain no.9 each product takes 2 slots for mixing
                    #To be changed for variable amount of time needed for mixing
                        self.Mchromosome.geneArray[k].append(i)
                        self.Mchromosome.geneArray[k+1].append(i)   
                #Add mixed products to be stored 
                Tobestored.append(i)
        #Schedule Storage Tanks chromosome        
        # for i in Tobestored:
        #     for j in range(2):
        #         self.STchromosome.geneArray[random.randrange(0,  self.STchromosome.genes)].append(i)     

    def __repr__(self):
        return str(self.Mchromosome.geneArray)
    def __len__(self):
        return len(self.Mchromosome.geneArray)
'''
       #Schedule Production Line chromosome        
        for i in jobs:
            for j in range(int(i.line.cT)):
                self.PLchromosome.geneArray[random.randrange(0,  self.PLchromosome.genes)].append(i)   
'''
 
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
    
# pp = pprint.PrettyPrinter(width = 4)

def displayPop(population):
    displaylist = [] 
    for i in population:
        # for j in i:
        displaylist.append(i)
    print(displaylist)
    # print("Generation 1")
    # pprint.pprint(displaylist[0])
    # print("Generation 2")
    # pprint.pprint(displaylist[1])

def start(days, hours, machines, popsize):
    length = days*hours*machines
    pop = CreateInitPop(length,popsize)
    displayPop(pop)

start(7,24,2,10)    