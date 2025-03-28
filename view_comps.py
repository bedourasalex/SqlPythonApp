from connection import get_connection

def view_comps():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM comp_name"
    cursor.excecute(sql)
    comp_names = cursor.fetchall()

    if comp_names:
        print("List of company names")
        for comp_names in comp_name:
            print(f"Id: {comp_name[0]}, year_created: {comp_name[1]}, comp_type: {comp_name[2]}, employee_number:{comp_name[3]}")

    else:
        print("there are no company names")
    cursor.close()
    connection.close()

sview_comps()