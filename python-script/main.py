from stocks.stock_prices import get_data

def main():
    url = "pain"
    new_url = get_data()
    print(new_url)

if __name__ == "__main__":
    main()