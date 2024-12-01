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

    #sorting left column into its respective array    
    for i in range(0,len(leftColumnArray)):
        for j in range(i+1,len(leftColumnArray)):
            if leftColumnArray[i] > leftColumnArray[j]:
                temp = leftColumnArray[j]
                leftColumnArray[j] = leftColumnArray[i]
                leftColumnArray[i] = temp 

    #sorting right column into its respective array
    for i in range(0,len(rightColumnArray)):
        for j in range(i+1,len(rightColumnArray)):
            if rightColumnArray[i] > rightColumnArray[j]:
                temp = rightColumnArray[j]
                rightColumnArray[j] = rightColumnArray[i]
                rightColumnArray[i] = temp 

    #error handling if the columns aren't the same length (considering that the problem requires a pair of numbers, this should be always true)
    if len(leftColumnArray) != len(rightColumnArray):
        raise ValueError("left column array and right column array aren't the same length") 

    for i in range(0,len(leftColumnArray)):
        pass