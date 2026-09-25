import csv
import random
import pandas as pd

# Create csv file
num_rows = 100
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Age', 'Salary'])
    for i in range(1, num_rows + 1):
        age = random.randint(18, 65)
        salary = round(random.uniform(30000, 120000), 2)
        writer.writerow([i, age, salary])

# Read csv file and show statistics
df = pd.read_csv('data.csv')
print(df.describe())