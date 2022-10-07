# SIMPLE PYTHON AND SQL QUERIES

This project contains two distinct sub projects:

- A python script that gets a list of specific tech stock prices from the [Finnhub](https://finnhub.io/) free api, finds the most volatile stock and writes the data gotten to a csv file.

- An `SQL_Queries` folder that contains various SQL queries ran on the [Try-SQL Editor](https://www.w3schools.com/sql/trysql.asp?file_name=trysql_select_all). The code structure:

```
.
├── SQL_QUERIES
│   ├── avg_price_data.sql        # SQL query to get the average price of all products
│   ├── berlin_customers.sql      # SQL query to get all the customers in Berlin city
│   ├── customers.sql             # SQL query to get customers with above 3 orders
│   ├── mexico_city.sql           # SQL query to get all the customers in Mexico city
│   ├── orders.sql                # SQL query to find all orders between a certain date
│   ├── products.sql              # SQL query to find the number of products that have a certain price
│   ├── same_city_cus.sql         # SQL query to get all the customers in the same city
```
## Installation

Clone this repository on your local machine by using the `git clone` command

For the SQL queries, they can be run on the [W3Schools Try-SQL Editor](https://www.w3schools.com/sql/trysql.asp?file_name=trysql_select_all)

For the python project:

> **Requirements**: Python `(v.3)` and above. If you're unsure of what python version you are using, run `python --version` on your terminal

### Opening the folder

- Run `cd python-script` to go into the python-script folder

### Virtual Environment

- Create a virtual environment called `venv`. For more information in creating a python virtual environment, visit the [Real Python Website](https://realpython.com/python-virtual-environments-a-primer/)

### Dependencies

- Run `python -m pip install -r requirements.txt` to install the project dependencies

#### Storing Secrets and Keys

- Create a `.env` file in the root folder of the `python-script`. Use the `.env.sample` file to create the necessary secret keys

## Testing the service

- Run `python main.py`