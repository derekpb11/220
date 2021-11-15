"""
Name: Derek Bolch
sales_force.py

Problem: this program will create a class that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from sales_person import SalesPerson
class SalesForce:

    def __init__(self):
        self.sales_people = []


    def add_data(self, file_name):
        in_file = open(file_name, 'r')

        for line in in_file:
            employee_list = line.split(",")
            temp_employee = SalesPerson(employee_list[0], employee_list[1])
            temp_sales = employee_list[2].split(" ")
            temp_sales.pop(0)
            float_sales = []
            for item in temp_sales:
                float_sales.append(float(item))
            for i in range(len(temp_sales)):
                temp_employee.enter_sale(temp_sales[i])
            self.sales_people.append(temp_employee)


    def quota_report(self, quota):
        total_quota_list = []
        for i in self.sales_people:
            temp_name = self.sales_people[i]
            temp_id = int(self.sales_people[i].get_id())
            temp_total = self.sales_people[i].total_sales()
            temp_met = False
            if quota < temp_total:
                temp_met = True
            else:
                temp_met = False
            quota_list = [temp_id, temp_name, temp_total, temp_met]
            total_quota_list.append(quota_list)
        return total_quota_list