from sales_person import SalesPerson
from sales_force import SalesForce

def main():

    sale1 = SalesForce()
    sale1.add_data("salesData.txt")
    sale1.quota_report(600)


main()