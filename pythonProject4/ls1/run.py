import pyodbc

print(pyodbc.drivers())
def connect():
    connection_string = ("DRIVER={ODBC Driver 18 for SQL Server};"
                         "Server=COMP7A2\\SQLEXPRESS;"
                        "Database=db0;"
                        "Trusted_Connection=yes;"
                        "Encrypt = yes;"
                        "TrustServerCertificate=yes;")
    connection = pyodbc.connect(connection_string)
    return connection

def main():
    table_name = "orderss"
    conn = connect()
    print_data(select_data(conn, table_name))
    add_data(conn, table_name)


def select_data(conn, name):
    cursor = conn.cursor()
    sql_command = "SELECT TOP 10 * FROM dbo.orderss"
    cursor.execute(sql_command)
    return cursor

def add_data(conn, name):
    cursor = conn.cursor()
    sql_command = f"INSERT INTO dbo.{name}(id, product, price) VALUES(?,?,?)"
    cursor.execute(sql_command, 15.0, 'salsa', 150.0)
    cursor.commit()


def print_data(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)

main()