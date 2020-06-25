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

mixer_2 = Mixer(2,1)

storagetank_1 = StorageTank("StorageTank_1", 2)
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
Rollon_STarwors50 = Product("Rollon_STarwors50", mixer_2, Rollon_PL, 9600, 2, 4, 40000, 242000)
Tube_Jungle50 = Product("Tube_Jungle50 ", mixer_2, Tubes_PL, 72, 2, 9, 40000, 6000)

StorangeTanks = [storagetank_1, storagetank_2, storagetank_3, storagetank_4, storagetank_5, storagetank_6, storagetank_7, storagetank_8]

jobs = [Cream_Starwors50, Cream_Jungle150, Rollon_STarwors50, Tube_Jungle50]
machines = [mixer_2, Rollon_PL, Tubes_PL, Cream1_PL, Cream2_PL, StorangeTanks]
# operations = [(machines[0],jobs[0]),(machines[5][1],jobs[0])]


Tobestored = []


'''
            #    8  9   10  11  12  01  02  03  
Mchromosome = [ [], [Ferrari], [Ferrari], [Ferrari], [Ferrari], [Ferrari], [], [], [], [], [], [], #Sunday
               [], [], [], [], [], [], [], [], [Ferrari], [], [], [], #Monday
               [], [], [], [], [], [], [], [], [Ferrari], [], [], [] , #Tuesday
               [], [], [], [], [], [], [], [], [Ferrari], [], [], [] , #Wednesday
               [], [], [], [], [], [], [], [] , [Ferrari], [], [], [] ] #Thursday

          
'''