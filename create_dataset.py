import pandas as pd
import numpy as np

np.random.seed(42)

records = 100

data = {
    "Student_ID": range(1, records + 1),
    "Study_Hours": np.random.randint(1, 10, records),
    "Attendance": np.random.randint(50, 100, records),
    "Assignments": np.random.randint(40, 100, records),
    "Marks": np.random.randint(35, 100, records)
}

df = pd.DataFrame(data)

df.to_csv("dataset.csv", index=False)

print("✅ dataset.csv created successfully!")
print(df.head())