from connection import get_connection

def insert_best_companies(comp_name, year_created, comp_type, employee_number):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO best_companies(comp_name, year_created, comp_type, employee_number) VALUES (%s, %s, %s, %s)"
    values = (comp_name, year_created, comp_type, employee_number)
    cursor.excecute(sql, values)
    connection.commit()
    print("The company has been added to the database!")
    cursor.close()
    connection.close()


comp_name = input("Give me the name of the company:")
year_created = int(input("Give me the year tha the company was created:"))
comp_type = input("Give me the company type:")
employee_number = int(input("Give me the number of employees that work inside the company"))

insert_best_companies(comp_name, year_created, comp_type, employee_number)
