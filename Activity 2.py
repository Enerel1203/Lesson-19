import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator= random.random()
    dateFormat= '%m/%d/%Y'

    startTime= time.mktime(time.strptime(startDate, dateFormat))
    endTime= time.mktime(time.strptime(endDate, dateFormat))

    randomTime= startTime + randomGenerator * (endTime - startTime)
    randomDate= time.strptime(dateFormat, time.localtime(randomTime))
    
    return randomDate
print("Random date:", getRandomDate("01/01/2016", "12/12/2018"))

