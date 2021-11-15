"""
Name: Derek Bolch
sales_person.py

Problem: this program will create a class that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    Class to create and store data for SalesPerson objects
    """
    def __init__(self, employee_id, name):
        """
        Constructor that creates a SalesPerson object taking in employee id as
        a string or int and name as a string
        """
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []


    def get_id(self):
        """
        Method that returns the objects employee id
        """
        return self.employee_id


    def get_name(self):
        """
        Method that returns the objects name
        """
        return self.name


    def set_name(self, name):
        """
        Method that sets the objects name to the name string
        """
        self.name = name


    def enter_sale(self, sale):
        """
        Method that adds sale to the list of the objects sales
        """
        self.sales.append(float(sale))


    def total_sales(self):
        """
        Method that sums all the sales in the objects sales list and returns that value
        """
        acc = 0
        for i in range(len(self.sales)):
            acc = acc + self.sales[i]
        return acc


    def get_sales(self):
        """
        Method that returns the objects list of sales
        """
        return self.sales


    def met_quota(self, quota):
        """
        Method that returns true if total_sales is greater than quota and false if not
        """
        if quota <= self.total_sales():
            return True
        return False


    def compare_to(self, other):
        """
        Method that compares the total sales of self to the total sales of other
        """
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0


    def __str__(self):
        """
        Method that returns a string of self information
        """
        return str(self.employee_id) + "-" + self.name + ":" + str(self.total_sales())
