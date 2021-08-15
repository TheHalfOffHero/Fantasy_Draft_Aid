import csv

#Player class
#Takes columns from csv and creates objects
class Player:
    def __init__(self, Name, Pos, Tm_and_Bye, Average, Stdev, Rank, Tier, ECR, ECRAvgVSAdp,PS): #Not sure what PS is so its not included in Player Object for now
        self.Name = Name
        self.Pos = Pos
        self.Tm_and_Bye = Tm_and_Bye
        self.Average = Average
        self.Stdev = Stdev
        self.Rank = Rank
        self.Tier = Tier
        self.ECR = ECR
        self.ECRAvgVSAdp = ECRAvgVSAdp


#Draft Class will include all draftable players with all values in csv included, with the exception of the last one.
class Draft:
    def __init__(self, csv):
        self.csv = csv
        self.PlayerList = []
        self.QBList = []
        self.RBList = []
        self.WRList = []
        self.TEList = []

    #GeneratePlayerList creates reader and line by line adds them to self.PlayerList property
    #This allows me to manipulate and generate other lists with all available Players
    #accessed as draftObject.generatePlayerList()
    def generatePlayerList(self):
        with open(self.csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.PlayerList.append(Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

        for player in self.PlayerList:
            if player.Pos == 'QB':
                self.QBList.append(player)
            elif player.Pos == 'RB':
                self.RBList.append(player)
            elif player.Pos == 'WR':
                self.WRList.append(player)
            elif player.Pos == 'TE':
                self.TEList.append(player)


    #written just to test that the list was actually generating
    def printPlayerList(self):
        for i in self.PlayerList:
            print("============================")
            print(i.Name + ', ' + i.Pos)
            print("============================")

    def printQBList(self):
        for i in self.QBList:
            print(i.Name + ', ' + i.Pos)
        print("============================")

    def printRBList(self):
        for i in self.RBList:
            print(i.Name + ', ' + i.Pos)
        print("============================")

    def printWRList(self):
        for i in self.WRList:
            print(i.Name + ', ' + i.Pos)
        print("============================")

    def printTEList(self):
        for i in self.TEList:
            print(i.Name + ', ' + i.Pos)
        print("============================")



#Uncomment to test that logic works
#test = Draft('TenTeamStandardBeerSheet.csv')
#test.generatePlayerList()
#test.printPlayerList()
#test.printQBList()
#test.printRBList()
#test.printWRList()
#test.printTEList()