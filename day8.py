import pandas as pd

import pandas as pd
data = pd.read_csv(r"C:\Users\Sree harshitha\OneDrive\Desktop\Day_8_sales_data.csv")

# Data Filtering
filtered= data[data["Sales"] > 1000]
region = data[data["Region"] == "East"]

# Data Processing
data["Profit_Per_Unit"] = data["Profit"] / data["Quantity"]
data["High_Sales"] = data["Sales"].apply(lambda x: "Yes" if x > 1000 else "No")

# Print Results
print(filtered)
print(region)
print(data)