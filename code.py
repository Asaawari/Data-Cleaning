import csv
import pandas as pd 

df = pd.read_csv("final.csv")

temp_headers = []
temp_df = []

temp_name = df[df['Name'].notna()]
temp_mass = df[df['Mass'].notna()]
temp_radius = df[df['Radius'].notna()]
temp_distance = df[df['Distance'].notna()]
temp_headers.append(df[0])
temp_df.append(list(zip(temp_name, temp_mass, temp_radius, temp_distance)), columns=("Name", "Mass", "Radius", "Distance"))

with open("cleaned.csv",'a+') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)   
    csvWriter.writerows(temp_df)