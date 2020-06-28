from Def import *
import random
import operator
import pandas
import numpy
import math
''' 
We need a slot (time-space slot) for each hour (we assume that time is in one hour granules), 
for every machine, every day. Also, we assume that manufacturing is 24 hours, 
and working days are from Sunday to Saturaday (7 days total).
We can use an list with a size 24*7*number_of_machines.
The slot should be a list because during the execution of our algorithm, 
we allow multiple operations during the same time-space slot.
There is an additional hash map(dictionary) which is used to obtain the first time-space slot 
at which an operation begins (its position in list) from the address of the product' object.
Each hour of an operation has a separate entry in the list, but there is only one entry per operation in the hash map. 
For instance, if an operation starts at 1pm and lasts for three hours, it has entries in the 1pm, 2pm, and 3pm slots.
'''
class Chromosome(object):
    def __init__(self, length):
        self.genes=length
        #Array of genes
        self.geneArray = []
    def initChromosom(self):
        #(time-space slot) for each hour slot is list
        for i in range(0,self.genes):
            self.geneArray.append([])        
    def __str__(self):
        return str(self.geneArray)

class fitness(object):
    def __init__(self, individual):
        self.schedule = individual
        self.totalmakespan=0
    def computeScore(self):
        '''Takes an individual of the population '''
        totalmakespan = 0
        schedulearray = self.schedule.getGeneArray()
        makespandict = {}
        #get solts for each product
        for i in schedulearray:
            for j in i:
                if j[1] in makespandict:
                    makespandict[j[1]].append(schedulearray.index(i))                  
                else:
                    makespandict[j[1]] = [schedulearray.index(i)]                                                     
        for i in makespandict:  
            #add total makespan last solt of operation - first slot
            totalmakespan += (makespandict[i][-1] - makespandict[i][0]) + 1           
        return totalmakespan

class Schedule(object):
    def __init__(self, length):        
        self.chromosome=Chromosome(length)
        self.chromosome.initChromosom()
        self.length=length
        
    def stpick(self, STdict, pos):
        for i in list(STdict.keys()):
            if pos not in STdict[i]:               
                return i

    def initialize(self):
        #For each product make list of operations = tuble of machine and product
        Ops = []#list of operations
        #Creating operations for each job
        for i in jobs:
            SlotsperTank = int(math.ceil(i.PPST/(i.speed*60)))
            Nbatch = int(math.ceil(i.demand/i.PPST)) 
            for n in range(Nbatch):  
                Ops.append([Operation(i.MNO, i, n, i.cTime), Operation(storagetank_2, i, n, SlotsperTank + i.PLCT), Operation(i.line, i, n, SlotsperTank + i.PLCT)])
        for i in Ops:         
            #Production Line rand positon
            pos3 = random.randrange(0, self.chromosome.genes - (i[2].dur + i[0].dur))
            #Mixer rand positon
            pos1 = random.randrange(0, self.chromosome.genes - i[0].dur) 
            i[1].set_machine(self.stpick(STdict, pos1+1))
            #assign production, storing and cleaining operation
            for m in range(i[2].dur, 0, -1):                
                self.chromosome.geneArray[pos3 + m].append(i[2])    
                self.chromosome.geneArray[pos3 + m].append(i[1]) 
                #Used slot added to Storage tank selection dict                 
                STdict[i[1].machine].append(pos3 + m)                      
            #assign mixing operation
            for j in range(i[0].dur, 0, -1):
                self.chromosome.geneArray[pos1 + j].append(i[0])  
#             #Storing   
#             for k in range(pos3, pos1+1, -1):
#                 #one slot after mixing final slot
#                 self.chromosome.geneArray[pos1 + i[0].dur + 1 + k].append(i[1])
#                 STdict[i[1].machine].append(pos1 + i[0].dur + 1 + k)  

    def populateSchedule(self,hashtable):
        for i in hashtable.keys():
            start = hashtable[i]
            end = i.dur + start
            for j in range(start, end-1):
                self.chromosome.geneArray[j].append(i)                                             
 
    def getGeneArray(self):
        return self.chromosome.geneArray
    def getlength(self):
        return self.chromosome.genes
    def __repr__(self):
        return str(self.chromosome.geneArray)
    def __len__(self):
        return len(self.chromosome.geneArray)

def encode(schedule):
    hashtable = {}
    genes = schedule.getGeneArray()
    for i in genes:
        for j in range(len(i)):            
            #key = operation  value = (time-slot, index of operation) 
            if (i[j] not in hashtable):
                hashtable[i[j]] = genes.index(i)
    return hashtable
def decode(schHash,length):
    sch = Schedule(length)
    sch.populateSchedule(schHash)
    return sch

def CreateInitPop(length, gensize):
    generation = []
    i = 0
    while (i < gensize):
        schedule = Schedule(length)
        schedule.initialize()
        generation.append(schedule)
        i += 1
    return generation

def rank(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = fitness(population[i]).computeScore()    
#     return fitnessResults
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = False)

def tournamentSelection(rankedPop, eliteSize):
    selectionPool = []
    df = pandas.DataFrame(numpy.array(rankedPop), columns=["Index","Fitness"])
    df['cumlative_sum'] = df.Fitness.cumsum()
    df['cumlative_percentage'] = 100*df.cumlative_sum/df.Fitness.sum()
    #Append elite index to selectiopool
    for i in range(0, eliteSize):
        selectionPool.append(rankedPop[i][0])
    #Non elite
    for i in range(0, len(rankedPop) - eliteSize):        
        threshold = 100*random.random()
        for j in range(0, len(rankedPop)):
            #if cumlative sum is more than threshold
            if (threshold <= df.iat[j,3]):
                selectionPool.append(rankedPop[j][0])
                break
    return selectionPool
    #return array of selected parents    

def matingPool(population, selectionPool):
    matingpool = []
    for i in range(0, len(selectionPool)):
        index = selectionPool[i]
        matingpool.append(population[index])
    return matingpool
#list of actual indviduals for mating using their index from selection pool 
#    
def breed(schParentA, schParentB):
    child = {}
    PAhash = encode(schParentA)
    PBhash = encode(schParentB)
    childP1={}
    childP2={}
    childP3={}
    #Radom portion of Parent A
    geneA = int(random.randrange(0,len(list(PAhash.keys()))))
    geneB = int(random.randrange(0,len(list(PAhash.keys()))))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    
    #swathfrom parent A
    childP1={k: PAhash[k] for k in list(PAhash.keys())[startGene:endGene]}
    #Drop allel
    for k in list(childP1.keys()):
        del PBhash[k]
    


def crossover(matingpool, eliteSize):
    nextGen = []
    # randPool = random.sample(matingpool, len(matingpool))
    #add elite to next gen
    for i in range(0,eliteSize):
        nextGen.append(matingpool[i])
    #The rest of the generation do cross over then add to next gen
    for i in range(0, len(matingpool) - eliteSize):
        #first with last
        child = breed(matingpool[i], matingpool[len(matingpool)-i-1])
        nextGen.append(child)
    return nextGen

def mutate(schHash, mutationRate, mutationSize):
    for i in range(len(schHash)):
        if(random.random() < mutationRate):
            for j in range(0,mutationSize):
                #swap mutation
                swapWith = int(random.random() * len(schHash))
                operation_1 = schHash[list(schHash.keys())[i]]
                operation_2 = schHash[list(schHash.keys())[swapWith]]
                schHash[list(schHash.keys())[i]] = operation_2
                schHash[list(schHash.keys())[swapWith]] = operation_1
    return schHash

def mutatePop(population, mutationRate, mutationSize):
    mutatedPop = []
    for i in range(0, len(population)):
        #hash pop to be ready for mutation
        mutatedHash=hashing(population[i])
        mutated = mutate(mutatedHash, mutationRate, mutationSize)
        mutatedPop.append(mutated)
    return mutatedPop    

def getNextGen(currentGen, eliteSize, mutationRate, mutationSize):
    popRanked = rank(currentGen)
    selectionResults = tournamentSelection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = crossover(matingpool, eliteSize)
    nextGenHashes = mutatePop(children, mutationRate, mutationSize)    
    nextGeneration=[]

    for i in nextGenHashes:
        individual=hashReverse(i,len(currentGen[0]))
        nextGeneration.append(individual)
    return nextGeneration        

def displayPop(population):
    displaylist = [] 
    for i in population:
        displaylist.append(i)
    print(displaylist)

def geneticAlgorithm(popSize, days, slots, eliteSize, mutationRate, mutationSize, generations):
    length=days*slots
    pop = CreateInitPop(length, popSize)
    print("Initial Score: %d"%rank(pop)[0][1])
#     displayPop(pop)

    for i in range(0, generations):
        pop = getNextGen(pop, eliteSize, mutationRate, mutationSize)
        print(pop)

    print("Final Score: " + str(rank(pop)[0][1]))
    bestScheduleIndex = rank(pop)[0][0]
    bestSchedule = pop[bestScheduleIndex]
    return bestSchedule
    
ga = geneticAlgorithm(popSize=10,days=2,slots=24, eliteSize=1, mutationRate=0.01, mutationSize=1,generations=10)    
