# importing data
data = open("./d2/d2data.txt","r").read().splitlines()

class Report:
    def __init__(self, data: dict):
        self.data = data
        self.flag = True
        self.numberOfSafeReports = 0
        
    def splitLinesIntoArray(self):
        # splitting each line into an array instead of having it be a string
        for i in range(0,len(self.data)):
            tempArray = self.data[i].rsplit(" ")

            self.data[i] = tempArray

    def checkForIncreasingNums(self):
        # turn each line into an array with the separation points being the spaces
        # iterate through the array to check if the the next number is greater than the current number
        # if the next number isn't greater than current, then set the flag to false.

        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])-1):
                if int(self.data[i][j]) > int(self.data[i][j+1]):
                    self.flag = False
                    break
                else:
                    self.flag = True 

            # if the flag is true, then proceed to go through the array and see if each of the numbers differ by more than 3 or less than 1 
            if self.flag == True:
                self.checkForIncrementAmount(self.data[i])  

        return

    def checkForDecreasingNums(self):
        # iterate through the array to check if the the next number is less than the current number
        # if the next number isn't less than current, then set the flag to false.

        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])-1):
                if int(self.data[i][j]) < int(self.data[i][j+1]):
                    self.flag = False
                    break
                else:
                    self.flag = True

            # if the flag is true, then proceed to go through the array and see if each of the numbers differ by more than 3 or less than 1 
            if self.flag == True:
                self.checkForIncrementAmount(self.data[i]) 
        
        return
        
    def checkForIncrementAmount(self, array: dict):
        for i in range(0,len(array)-1):
            # see if the current number and next numbers differ by less than 1 or more than 3
            # if they the previous statement is true, then set flag to false
            if abs(int(array[i])-int(array[i+1])) < 1 or abs(int(array[i])-int(array[i+1])) > 3:
                self.flag = False
                break
            else:
                self.flag = True

        # if flag is true, then increment the number of safe reports  
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
