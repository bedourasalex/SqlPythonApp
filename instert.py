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


insert_best_companies("epsa", 1906, "soft_drinks", 10000)
insert_best_companies("eneba", 1990, "games", 4000)
insert_best_companies("metaxa", 1911, "bourbons", 30)
insert_best_companies("karelia", 1906, "ciggaretes", 800)
insert_best_companies("ots", 2003, "software_maker", 280)
insert_best_companies("olympic_air", 1903, "aeroplanes", 1000)


