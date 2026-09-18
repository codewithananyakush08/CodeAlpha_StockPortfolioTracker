#Stock Portfolio Tracker
stock_prices={
"AAPL":180,
"TASA":250,
"GOOGL":140,
"MSFT":420,
"AMZN":180
}
try:

    stock=input("Enter stock name: ").upper()
    quantity=int(input("Enter Quantity:"))
    if quantity<=0:
        print("Quantity must be a positive number.")
    elif stock in stock_prices:
        price=stock_prices[stock]
        total=price*quantity
        print("\n--- Stock Portfolio---")
        print("Stock: ",stock)
        print("Price per share: ",price)
        print("Quantity:",quantity)
        print("Total Investment:",total)
    else:
        print("Stock not available.")  
except ValueError:
    print("Invalid input! Quantity must be a wholenumber(e.g 5 not'five' or '2.5').")   
except Exception as e:
    print("Something went wrong:",e)           


    

