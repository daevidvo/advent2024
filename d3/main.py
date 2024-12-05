import re

data = open("./d3/d3data.txt","r").read().split("mul(")

class Stack:
    def __init__(self, data:dict ):
        self.stack = data 
    
    def append(self, data: str) -> dict:
        return self.stack.append()
    
    def pop(self) -> str:
        return self.stack.pop()
    



if __name__ == "__main__":
    # part1
    # Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

    mulStack = Stack(data)

    regex = re.compile("^\d{1,3},\d{1,3}\)")

    for item in mulStack.stack:
        if re.match(regex,item):
            tempString = item.split(")")

            
            
    pass
