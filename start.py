import pandas as pd
import statistics
from matplotlib import pyplot as plt

df = pd.read_csv("titanic.csv")
print(df) #printed a brief summary of my data

#i deleted the unnecessary data from my data set e.g the cabin number as half of thie data was empty
#i cleaned up the age data as some ages were undefined and this would mess with my data

