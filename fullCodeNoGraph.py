import pandas as pd
import statistics
from matplotlib import pyplot as plt

df = pd.read_csv("titanic.csv")
#print(df) #printed a brief summary of my data

#i deleted the unnecessary data from my data set e.g the cabin number as half of thie data was empty
#i cleaned up the age data as some ages were undefined and this would mess with my data


#Proving my Hypothesis!
#1. more 3rd class than 1st class
df1 = df['Pclass']
print(df1)
#Using a for loop to count the number of third class passengers on board
threeCount = 0
for i in df1:
    if i == 3:
        threeCount+=1
print("Third Class:", threeCount)

#Using a for loop to count the number of first class passengers on board
oneCount = 0
for i in df1:
    if i == 1:
        oneCount+=1
print("First Class:", oneCount)

#Finding the difference between them to prove the hypothesis
difference = threeCount - oneCount
print("There is", difference, "more 3rd class passengers!")
print("Hypothesis was correct!!!")

#2. There were more males than females on board
df1 = df['Sex']
print(df1)
#Using a for loop to count the number of males in the Data Set
maleCount = 0
for i in df1:
    if i == "male":
        maleCount +=1
print("There are", maleCount, "males on board")

#Using a for loop to count the number of females in the Data Set
femaleCount = 0
for i in df1:
    if i == "female":
        femaleCount +=1
print("There are", femaleCount, "females on board")

#Finding the difference between the number of males and females on board
diff = maleCount - femaleCount
print("There is", diff, "more males than females on board!")
print("Hypothesis was correct!!!")

#3. More people died than survived
df1 = df['Survived']
print(df1)

#Finding out the number of people dead also using a for loop
deadCount = 0
for i in df1:
    if i == 0:
        deadCount += 1
print("There are", deadCount, "passengers dead")

#Finding the number of passengers that survived using a for loop
aliveCount = 0
for i in df1:
    if i == 1:
        aliveCount += 1
print("There are", aliveCount, "passengers alive")

#Getting the difference to prove my hypothesis
difference = deadCount - aliveCount
print("There were:", difference, "more passengers dead")
print("Hypothesis was correct!!!")

#4. The most frequent age is 30
df1 = df['Age']
mode = statistics.mode(df1)
print("The most frequent age is:", mode)
print("Hypothesis was Incorrect!")
