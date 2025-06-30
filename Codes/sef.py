import pandas as pd

# Create some data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False)

df = pd.read_excel("output.xlsx")
print(df)
