import csv

stock_prices = {
  
    "TCS": 4200,
    "INFY": 1650,
    "RELIANCE": 2900,
    "HDFCBANK": 1750

}

total = 0
records = []

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

while True:
    stock = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    qty = int(input("Enter Quantity: "))

    value = stock_prices[stock] * qty
    total += value

    records.append([stock, qty, value])

print("\n------ Portfolio Summary ------")

for r in records:
    print(f"{r[0]} x {r[1]} = ${r[2]}")

print(f"\nTotal Investment = ${total}")

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Value"])
    writer.writerows(records)

print("\nPortfolio saved as portfolio.csv")
