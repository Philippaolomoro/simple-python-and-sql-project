from stocks.stock_prices import get_data
import csv

def get_volatile_stock():
    stock_data = get_data()
    volatile_stock = max(stock_data, key=lambda x:x['dp'])
    return volatile_stock

def get_necessary_volatile_stock_data():
    volatile_stock = [get_volatile_stock()]
    new_list = []
    for x in volatile_stock:
        listing = [x["ss"], x["dp"], x["c"], x["pc"]]
        new_list.extend(listing)
    return new_list

def main():
    volatile_stock = get_necessary_volatile_stock_data()
    csv_header = ["stock_symbol", "percentage_change", "current_price", "last_close_price"]
    with open("volatile_stock.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerow(volatile_stock)
    print("The data has been written to the csv file")

if __name__ == "__main__":
    main()