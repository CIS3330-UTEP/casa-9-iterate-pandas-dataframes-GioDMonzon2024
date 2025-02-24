import pandas as pd

# Method 4: Using iterrows() method
df = pd.read_csv("big-mac-full-index.csv")

print("Using iterrows():")
for index, row in df.iterrows():
    price_in_usd = row["local_price"] / row["dollar_ex"]
    print(f"{row['name']} ({row['date']}): ${price_in_usd:.2f}")


# Method 6: Using apply() method
df = pd.read_csv("big-mac-full-index.csv")

print("\nUsing apply():")
df["price_in_usd"] = df.apply(lambda row: row["local_price"] / row["dollar_ex"], axis=1)

for index, row in df.iterrows():
    print(f"{row['name']} ({row['date']}): ${row['price_in_usd']:.2f}")
