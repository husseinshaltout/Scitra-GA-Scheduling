class Mixer(object):

    def __init__(self, mixerSize, cleaningTime):
        self.size = mixerSize
        self.cT = cleaningTime

class StorageTank(object):

    def __init__(self, TankName, tankSize, cleaningTime):
        self.name = TankName
        self.size = tankSize
        self.cT = cleaningTime

class ProductionLine(object):
    def __init__(self, plName, cleaningTime):
        self.name = plName
        self.cT= cleaningTime
    def __repr__(self):
        return str(self.name)
class Product(Mixer):
    machines = []
    def __init__(self, mL, pName, mixerNo, productionLine, COT, netSpeed, headCount, cycleTime, isOutSourced):
        self.machines = mL
        self.name = pName
        self.MNO = mixerNo
        self.line = productionLine
        self.cot  = COT #Change over time
        self.speed = netSpeed #Net speed
        self.heads = headCount
        self.cTime = cycleTime #Cycle time
        self.totaltime = self.cot + self.cTime + self.MNO.cT + self.line.cT
    def __repr__(self):
        return str(self.name)

mixer_2 = Mixer(2,1.5)
mixer_1 = Mixer(0.5,1.5)

storagetank_1 = StorageTank("StorageTank 1", 2, 1.5)
storagetank_2 = StorageTank("StorageTank 2", 2, 1.5)
storagetank_3 = StorageTank("StorageTank 3", 2, 1.5)
storagetank_4 = StorageTank("StorageTank 4", 2, 1.5)
storagetank_5 = StorageTank("StorageTank 5", 2, 1.5)
storagetank_6 = StorageTank("StorageTank 6", 2, 1.5)
storagetank_7 = StorageTank("StorageTank 7", 2, 1.5)
storagetank_8 = StorageTank("StorageTank 8", 2, 1.5)

Rollon_PL = ProductionLine("Rollon",1)
Tubes_PL = ProductionLine("Tubes",1)
Cream1_PL = ProductionLine("Cream 1",1)
Cream2_PL = ProductionLine("Cream 2",1)

Ferrari = Product("Mixer 2", "Ferrari1", mixer_2, Cream1_PL, 1.5, 32, 8, 6, False)
StarWors = Product("Mixer 1", "Cream Star wors20", mixer_1, Cream2_PL, 1.5, 44, 8, 0, True)
jobs = (Ferrari, StarWors)
# print(jobs[0].totaltime, jobs[0].cot, jobs[0].cTime, jobs[0].MNO.cT, jobs[0].line.cT)