class Mixer(object):

    def __init__(self, mixerSize, cleaningTime):
        self.size = mixerSize
        self.cT = cleaningTime
        self.name = "Mixer"
    def __repr__(self):
        return str(self.name)

class StorageTank(object):

    def __init__(self, TankName, tankSize):
        self.name = TankName
        self.size = tankSize
    def __repr__(self):
        return str(self.name)

class Product(object):
    machines = []
    def __init__(self, pName, mixerNo, productionLine, netSpeed, cycleTime, PLcleaningtime, PPST, demand):
        self.name = pName #Product name
        self.MNO = mixerNo #Mixer number
        self.line = productionLine #Production Line
        self.speed = netSpeed #Net speed
        self.cTime = cycleTime #Cycle time
        self.PLCT = PLcleaningtime #Production line cleaing time
        self.PPST = PPST #Number of products per storage tank
        self.demand = demand #Demand  
    def __repr__(self):
        return str(self.name)  

class ProductionLine(object):
    def __init__(self, plName):
        self.name = plName
    def __repr__(self):
        return str(self.name)

class Operation(object):
    def __init__(self, machine, job, batch, duration):
        self.machine = machine #Machine
        self.job = job #Job or product
        self.batchno = batch #Batch number
        self.dur = duration #Operation duration
        self.name = (self.machine, self.job) 
    def set_machine(self, m):
        self.machine = m
        self.name = (self.machine, self.job)
    def __repr__(self):
        return str(self.name)

mixer_2 = Mixer(2,1)

storagetank_1 = StorageTank("StorageTank 1", 2)
storagetank_2 = StorageTank("StorageTank 2", 2)
storagetank_3 = StorageTank("StorageTank 3", 2)
storagetank_4 = StorageTank("StorageTank 4", 2)
storagetank_5 = StorageTank("StorageTank 5", 2)
storagetank_6 = StorageTank("StorageTank 6", 2)
storagetank_7 = StorageTank("StorageTank 7", 2)
storagetank_8 = StorageTank("StorageTank 8", 2)

Rollon_PL = ProductionLine("Rollon")
Tubes_PL = ProductionLine("Tubes")
Cream1_PL = ProductionLine("Cream_1")
Cream2_PL = ProductionLine("Cream_2")

Cream_Starwors50 = Product("Cream_Starwors50", mixer_2, Cream1_PL, 80, 2, 8, 40000, 40000)
Cream_Jungle150 = Product("Cream_Jungle150", mixer_2, Cream2_PL, 48, 2, 5, 13333, 16000)
Rollon_STarwors50 = Product("Rollon_STarwors50", mixer_2, Rollon_PL, 9600, 2, 4, 40000, 80000)
Tube_Jungle50 = Product("Tube_Jungle50 ", mixer_2, Tubes_PL, 72, 2, 9, 40000, 6000)


product_1 = Product("Product_1", mixer_2, Cream1_PL, 160, 2, 1,40000,80000)
product_2 = Product("Product_2", mixer_2, Cream1_PL, 96, 2, 1, 13333, 25000)
product_3 = Product("Product_3", mixer_2, Cream2_PL, 160, 2, 1, 40000, 75000)
product_4 = Product("Product_4", mixer_2, Cream2_PL, 210, 2, 1, 9524, 18000)
product_5 = Product("Product_5", mixer_2, Rollon_PL, 320, 2, 1, 40000, 40000)
product_6 = Product("Product_6", mixer_2, Rollon_PL, 320, 2, 1, 40000, 37500)
product_7 = Product("Product_7", mixer_2, Rollon_PL, 360, 2, 1, 80000, 78000)
product_8 = Product("Product_8", mixer_2, Tubes_PL, 144, 2, 1, 40000, 40000)
product_9 = Product("Product_9", mixer_2, Tubes_PL, 96, 2, 1, 13333, 11000)
product_10 = Product("Product_10", mixer_2, Tubes_PL, 120, 2, 1, 20000, 18500)

StorangeTanks = [storagetank_1, storagetank_2, storagetank_3, storagetank_4, storagetank_5, storagetank_6, storagetank_7, storagetank_8]
STdict = {}
def stinit(ST):
    for i in ST:
        STdict[i] = []
stinit(StorangeTanks)
# jobs = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10]
jobs = [Cream_Starwors50, Cream_Jungle150, Rollon_STarwors50, Tube_Jungle50]
machines = [mixer_2, Rollon_PL, Tubes_PL, Cream1_PL, Cream2_PL, StorangeTanks]



Tobestored = []


