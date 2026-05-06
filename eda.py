import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 250, 300, 280, 350, 400]
}

df = pd.DataFrame(data)

# Step 2: Basic Info
print("📊 Dataset:")
print(df)

print("\n📈 Statistical Summary:")
print(df.describe())

# Step 3: Analysis
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()
avg_sales = df["Sales"].mean()

print("\n🔍 Insights:")
print("Highest Sales:", max_sales)
print("Lowest Sales:", min_sales)
print("Average Sales:", round(avg_sales, 2))

# Step 4: Visualization
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()