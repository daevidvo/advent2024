# importing data
data = open("./d2/d2data.txt","r").read().splitlines()

class Report:
    def __init__(self, data: dict):
        self.data = data
        self.flag = True
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
            for j in range(0,len(self.data[i])-1):
                if int(self.data[i][j]) > int(self.data[i][j+1]):
                    self.flag = False
                    break
                else:
                    self.flag = True 
            
            if self.flag == True:
                self.checkForIncrementAmount(self.data[i])  

        return

    def checkForDecreasingNums(self):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])-1):
                if int(self.data[i][j]) < int(self.data[i][j+1]):
                    self.flag = False
                    break
                else:
                    self.flag = True
            
            if self.flag == True:
                self.checkForIncrementAmount(self.data[i]) 
        
        return
        
    def checkForIncrementAmount(self, array: dict):
        print(array)

        for i in range(0,len(array)-1):
            print(array[i])
            if abs(int(array[i])-int(array[i+1])) < 1 or abs(int(array[i])-int(array[i+1])) > 3:
                self.flag = False
                break
            else:
                self.flag = True
        
        if self.flag == True:
            self.numberOfSafeReports+=1
         
        return

    def returnNumberOfSafeReports(self):
        return self.numberOfSafeReports 
if __name__ == "__main__":
    # part1

    # So, a report only counts as safe if both of the following are true:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

    report = Report(data)

    report.splitLinesIntoArray()

    report.checkForDecreasingNums()

    report.checkForIncreasingNums()

    print(report.returnNumberOfSafeReports())
