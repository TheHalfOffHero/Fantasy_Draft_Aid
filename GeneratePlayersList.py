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

    #GeneratePlayerList creates reader and line by line adds them to self.PlayerList property
    #This allows me to manipulate and generate other lists with all available Players
    #accessed as draftObject.generatePlayerList()
    def generatePlayerList(self):
        with open(self.csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.PlayerList.append(Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

    #written just to test that the list was actually generating
    def printPlayerList(self):
        for i in self.PlayerList:
            print(i.Name + ', ' + i.Pos)



#Uncomment to test that logic works
#test = Draft('TenTeamStandardBeerSheet.csv')
#test.generatePlayerList()
#test.printPlayerList()

#testing Player
#This works just fine but for some reason generatePlayerList gives me an empty list printed
#testPlayer = Player('Matt', 'QB', 'TB/3', 2, 3, 1, 1, 1, 1, 1)
#print(testPlayer.Name, testPlayer.Pos)

