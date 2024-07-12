import os
from bs4 import BeautifulSoup
import pandas as pd

file_path = r"C:\Users\Desktop\python\project1"

folders = os.listdir(file_path)
data = {"ile_name":[],"SGPA":[],"CGPA":[]}

for folder in folders:
    data_files_path = os.path.join(file_path, folder,'found')
    
    if not os.path.exists(data_files_path):
        print(f"Path {data_files_path} does not exist.")
        continue

    data_files = os.listdir(data_files_path)

for file in data_files:
    file_name = os.path.join(file_path, folder,'found', file)
    print(f"Processing file: {file}")

    data['file_name'].append(file)
    
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        data['SGPA'].append(soup.find_all("td", class_ = "border1")[-5].text.replace("\xa0",""))
        data['CGPA'].append(soup.find_all("td", class_ = "border1")[-3].text.replace("\xa0",""))        

    except Exception as e:
        print("Error processing file ")
        

dataframe = pd.DataFrame(data)
dataframe.to_csv("Record.csv")
print("Completed")