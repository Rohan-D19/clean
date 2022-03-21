import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Luminosity"]

df = df.rename({
  'Distance':"distance"
  'Star_name':"star"
  'Mass':"mass"
  'Radius':"radius"
}).axis='columns'

df.to_csv('main_csv')
