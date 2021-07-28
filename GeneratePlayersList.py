import csv
#Might use pandas? csv module is in every python 3 installation. Might be easier

#import pandas as pd
#df=pd.read_csv('TenTeamStandardBeerSheet.csv', encoding='us-ascii');
#print(df.to_string());

# We want to read int he csv and instantiate a list of Player Objects so we can manipulate as necessary
# columns: Name,Pos,Tm/Bye,Average,Stdev,Rank,Tier,ECR,ECRAvg,ECR VS. ADP,PS,Baseline

#Player class
#Takes columns from csv and creates objects
class Player:
    def __init__(self, Name, Pos, Tm_and_Bye, Average, Stdev, Rank, Tier, ECR, ECRAvgVSAdp,PS):
        self.Name = Name
        self.Pos = Pos
        self.Tm_and_Bye = Tm_and_Bye
        self.Average = Average
        self.Stdev = Stdev
        self.Rank = Rank
        self.Tier = Tier
        self.ECR = ECR
        self.ECRAvgVSAdp = ECRAvgVSAdp


class Draft:
    def __init__(self, csv):
        self.csv = csv
        self.PlayerList = []

    def generatePlayerList(self):
        with open(self.csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                self.PlayerList.append(Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

#test = Draft('TenTeamStandardBeerSheet.csv')
#test.generatePlayerList
#print(test.PlayerList)

#This works just fine but for some reason generatePlayerList gives me an empty list printed
testPlayer = Player('Matt', 'QB', 'TB/3', 2, 3, 1, 1, 1, 1, 1)
print(testPlayer.Name, testPlayer.Pos)