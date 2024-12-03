# importing data
data = open("./d2/d2data.txt","r").read().splitlines()

class Report:
    def __init__(self, data: dict, flag: bool):
        self.data = data
        self.flag = True
        self.type = ""
        self.numberOfSafeReports = 0
        
    def splitLinesIntoArray(self):
        for i in range(0,len(self.data)):
            tempArray = self.data[i].rsplit(" ")

            self.data[i] = tempArray

    def checkForIncreasingNums(self):
        # turn each line into an array with the separation points being the spaces
        # iterate through the array to check if the the next number is greater than the previous number
        # if the next number isn't greater than previous, then set the flag to false.

        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                if self.data[i][j] > self.data[i][j+1]:
                    self.flag = False
                    return

        self.type = "increasing" 
        return self.checkForIncrementAmount()            

    def checkForDecreasingNums(self):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                if self.data[i][j] < self.data[i][j+1]:
                    self.flag = False
                    return

        return self.checkForIncrementAmount()

    def checkForIncrementAmount(self):
        if self.type == "increasing":
            


        pass

if __name__ == "__main__":
    # part1

    # So, a report only counts as safe if both of the following are true:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    report = Report(data)

    print(report.data)
    22
    pass
