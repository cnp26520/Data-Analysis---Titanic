import numpy as np
import pandas as pd
df = pd.read_csv("train.csv")
df.head()
print(df.head())
rich = (df[df["Pclass"] < 2])
print(rich.mean(0))
poor = (df[df["Pclass"] >2])
print(poor.mean(0))
#(rich[rich["Survived"] == 1])
#By looking at the two charts we see that those who were in first class had a far higher chance of surviving
#Showing bias towards the wealthy in making it out alive.
#print(lol[lol["Survived"] == 1])
#print(rich.Pclass.count())
print(df.mean(0))
young = (df[df["Age"] < 29])
print(young.mean(0))
old = (df[df["Age"] > 29])
print(old.mean(0))
#by comparing it right down the center we see clearly that there is almost no distinciton between
#Age and survivability of the people
#print((df[df["Pclass"] == 3]).value_counts())
males = (df[df["Sex"] == "male"])
print(males.mean(0))
males_living = (males[males["Survived"] == "1"])
females = (df[df["Sex"] == "female"])
print(females.mean(0))
#Here we see an absolutely humongous discrepancy between the survivors found between males and females.
#It shows that females were far more likely than Males, which means they must have been offered far more sports
#Who said Chivalry was dead.