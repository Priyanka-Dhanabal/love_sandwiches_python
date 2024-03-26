# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# To check if API is working. content from sales worksheet was displayed
#sales = SHEET.worksheet('sales') 
#data = sales.get_all_values()
#print(data)

def get_sales_data():
    ''' 
    Get sales figures input from the user
    '''
    while True:

        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        validate_data(sales_data)

        if validate_data(sales_data):
            print('Data is valid !')
            break

    return sales_data

def validate_data(values):
    '''
    Inside the try, converts all strings values to integers.
    raises value error if string can not be converted into int.
    or if there arent exactly 6 values.
    '''

    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError( 
                f"Exactly 6 values required, you provide {len(values)}"
            )
        
    except ValueError as e:
        print(f"invalid data: {e}, please try again. \n")
        return False
    return True


def update_sales_worksheet(data):
    """
    update sales worksheet, add new row with the list of data provided.
    """
    print("Updating the Sales worksheet.....\n")
    sales_worksheet = SHEET.worksheet('sales')

    sales_worksheet.append_row(data)

    print("Sales worksheet updated successfully \n")


def calculate_surplus_data(data):
    """
    Compare sales with stock and calculates the surplus for each item type.
    Stock value minus Sales sales value equals to surplus
    - positive = was a waste
    - negative = extra made when stock ran out
    """
    print("Calculating surplus data ..... \n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)


def main():
    
    """
    Run all the profram function. 
    """
    data = get_sales_data()
    sales_data = [num for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)





print("Welcome... !\n ")
main()


