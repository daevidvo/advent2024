import re

data = open("./d3/d3data.txt","r").read().split("mul(")

class Mull:
    def __init__(self, data:dict ):
        self.total = 0
        self.data = data
        self.numberPairs = []

    def splitNumbers(self) -> None:
        regex = re.compile("^\d{1,3},\d{1,3}\)")

        for item in self.data:
            if re.match(regex,item):
                # take the regex matched item and split it by ")" then split the first element by "," since this will separate the two numbers that we'll need in the multiplication
                tempString = item.split(")")[0].split(",")

                self.numberPairs.append(tempString)

    def multiplyPairsAndAdd(self) -> int:
        for item in self.numberPairs:
            num1 = int(item[0])
            num2 = int(item[1])

            product = num1 * num2

            self.total = self.total + product

        return self.total 




if __name__ == "__main__":
    # part1
    # Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

    mull = Mull(data)

    mull.splitNumbers()

    print(mull.multiplyPairsAndAdd())
            
    pass
