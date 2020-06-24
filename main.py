from Def import *
import random
import pprint
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
        self.score=0
    def computeScore(self):
        score = 0
        schedulearray = self.schedule.getGeneArray()
        makespandict = {}
        #get solts for each product
        for i in schedulearray:
            for j in i:
                if j[1] in makespandict:
                    makespandict[j[1]].append(schedulearray.index(i))                  
                else:
                    makespandict[j[1]] = [schedulearray.index(i)]
        totalmakespan = 0            
        for i in makespandict:               
            print("Make span of",i,makespandict[i][-1] - makespandict[i][0])
            totalmakespan += makespandict[-1] - makespandict[0]

                    
        return makespandict
class Schedule(object):
    def __init__(self, length):        
        self.chromosome=Chromosome(length)
        self.chromosome.initChromosom()
        self.length=length

    def initialize(self):
        #For each product make list of operations = tuble of machine and product
        O = []

        for i in jobs:
            O.append([(i.MNO, i), (storagetank_1,i), (i.line,i)])
        for i in O:  
            Mdur = i[0][1].cTime
            STdur = 1
            PLdur = i[2][1].PLCT
            pos1 = random.randrange(0, self.chromosome.genes - Mdur)
            pos2 = random.randrange(0, self.chromosome.genes - STdur)
            pos3 = random.randrange(0, self.chromosome.genes - PLdur)
            #assign mixing operation
            for j in range(Mdur, 0, -1):
                self.chromosome.geneArray[pos1 + j].append(i[0])
            #assign storing operation
            for k in range(STdur, 0, -1):                
                self.chromosome.geneArray[pos2 + k].append(i[1])
            #production operation
            for m in range(PLdur, 0, -1):                
                self.chromosome.geneArray[pos3 + m].append(i[2]) 
                
    def populateSchedule(self,hashtable):
        for i in hashtable.keys():
            temp=str(i)[-1]
            temp2=int(temp)
            self.chromosome.geneArray[(temp2)].append(hashtable[i])
    def getGeneArray(self):
        return self.chromosome.geneArray
    def getlength(self):
        return self.chromosome.genes
    def __repr__(self):
        return str(self.chromosome.geneArray)
    def __len__(self):
        return len(self.chromosome.geneArray)
def hashing(sch):
    hashtable={}
    genes=sch.getGeneArray()
    # obtain the firstslot at which an operation begins (its position in vector)
    #position is key operation is the value
    #time slot postition + 10 * position in time slot
    for i in genes:  
        for j in range(len(i)):
            hashtable[(genes.index(i)+(10*j))]=i[j]
    return hashtable
 
def hashReverse(schHash,length):
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

def breed(schParentA, schParentB):
    child = {}
    PAhash = hashing(schParentA)
    PBhash = hashing(schParentB)
    childP1={}
    childP2={}
    childP3={}
#     print("PAhash:",PAhash)
#     print("PBhash:",PBhash)
    #Radom portion of Parent A
#     geneA = int(random.random() * schParentA.getlength())
    geneA = int(random.randrange(0,len(list(PAhash.keys()))))
    #Radom portion of Parent B
    geneB = int(random.randrange(0,len(list(PBhash.keys()))))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
#     print("Start Gene: ",startGene)
#     print("End Gene:",endGene)
    
    #First half from parent A
    childP1={k: PAhash[k] for k in list(PAhash.keys())[:startGene]}
    #Second half from parent B
    childP2={k: PBhash[k] for k in list(PBhash.keys())[startGene:endGene+1]}
    #Rest of the genes from parent A
    childP3={k: PAhash[k] for k in list(PAhash.keys())[endGene+1:]}

    child.update(childP1)
    child.update(childP2)
    child.update(childP3)
#     print("childP1",childP1)
#     print("childP2",childP2)
#     print("childP3",childP1)
    print(child)
    childSch = hashReverse(child,schParentA.getlength())

    return childSch

def crossover(matingpool, eliteSize):
    nextGen = []
    randPool = random.sample(matingpool, len(matingpool))
    #add elite to next gen
    for i in range(0,eliteSize):
        nextGen.append(matingpool[i])
    #The rest of the generation do cross over then add to next gen
    for i in range(0, len(matingpool) - eliteSize):
        #first with last
        child = breed(matingpool[i], matingpool[len(matingpool)-i-1])
        nextGen.append(child)
    return nextGen

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
    return displayPop(pop)

start(7,24,2,10)    