#importing data
data = open("./d1/d1data.txt","r").read().splitlines()

#split columns into two arrays
#sort arrays
#go through both arrays and subtract each corresponding element from one another

if __name__ == "__main__":
    print(data)

    #declaring arrays
    leftColumnArray = []
    rightColumnArray = []

    #adding individual elements into their respective arrays
    for item in data:
        leftColumnElement = item[0:5]
        rightColumnElement = item[8:]

        leftColumnArray.append(leftColumnElement)
        rightColumnArray.append(rightColumnElement)
