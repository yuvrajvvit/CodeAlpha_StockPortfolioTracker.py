# Yuv Raj
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3400,
    "INFY": 1500
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker!\n")
print("Available stocks: ", ', '.join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❌ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Quantity must be a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"✅ Added {quantity} shares of {stock} worth ₹{investment}")

 
print("\n📊 Your Portfolio Summary:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares x ₹{stock_prices[stock]} = ₹{value}")

print(f"\n💰 Total Investment: ₹{total_investment}")

save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            f.write(f"{stock}: {quantity} shares x ₹{stock_prices[stock]} = ₹{value}\n")
        f.write(f"\nTotal Investment: ₹{total_investment}\n")
    print("📁 Summary saved to 'portfolio_summary.txt'")

