import csv
import pandas as pd 

df = pd.read_csv("final.csv")

df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
final_data = df.dropna()
final_data.reset_index(drop=True,inplace = True)

temp_headers = []
temp_df = []

# temp_name = final_data[df['Star_name'].notna()]
# temp_mass = final_data[df['Mass'].notna()]
# temp_radius = final_data[df['Radius'].notna()]
# # temp_distance = final_data[df['Distance'].notna()]
# temp_headers.append(df[0])
# temp_df.append(list(zip(temp_name, temp_mass, temp_radius, temp_distance)), columns=("Name", "Mass", "Radius", "Distance"))

# with open("cleaned.csv",'w') as f:
#     csvWriter = csv.writer(f)
#     csvWriter.writerow(temp_headers)   
#     csvWriter.writerows(final_data)

final_data.to_csv("cleaned.csv")