import pandas as pd
data = pd.read_csv(r"C:\Users\Sree harshitha\OneDrive\Desktop\Day_11_banking_data.csv")
sorted = data.sort_values(by="Account_Balance", ascending=False).head(10)
data["Transaction_Rank"] = data.groupby("Branch")["Transaction_Amount"].rank(ascending=False)
print(sorted)
print(data)