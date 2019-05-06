"""
tasks

1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER
Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter). (NB Changed 21.04.2019)
Table Provider fields: ID, ProviderName. (NB Changed 21.04.2019)
If you want, you may add some additional fields, but not necessary.
2) Insert IT College canteen data by separate statement, other canteens as one list.
3) Create query for canteens which are open 16.15-18.00
4) Create query for canteens which are serviced by Rahva Toit

By: Hannes Toots
"""
import sqlite3

def create_connection(db):
    """
    Creates a database connection to the SQLite database 'db'
    :param db: Database to connect to
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db)
        return connection
    except sqlite3.Error as e:
        print(e)
    return None

# Create tables
def create_table(conn, sql):
    """
    Create Tables for sql database
    :param con: Connection object
    :param sql: create table statement
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Add provider to PROVIDER
def create_provider(conn, provider):
    """
    Create a new provider into the PROVIDER table
    :param conn: connection object
    :param provider: provider to insert to table
    :return:
    """
    sql = """INSERT INTO PROVIDER (ProviderName) VALUES (?)"""
    cur = conn.cursor()
    cur.execute(sql, (provider,))
    return cur.lastrowid

# Add canteen to CANTEEN
def create_canteens(conn, canteens):
    """
    Create canteens from the canteen_data list into the CANTEEN table
    :param conn: connection object
    :param canteens: canteen list
    """

    # Canteen lists for providerID
    rtCanteens = ['Economics- and social science building canteen', 'Library canteen', 'U06 building canteen']

    breasCanteens = ['Main building Deli cafe', 'Main building Daily lunch restaurant', 'Natural Science building canteen, ICT building canteen']

    sql = """INSERT INTO CANTEEN(
            ProviderID, Name, Location,
            time_open, time_closed)
            VALUES(?, ?, ?, ?, ?)"""

    cur = conn.cursor()
    # Get tuples of list
    for canteenInfo in canteens:
        # Make tuple into list
        canteenInfo = list(canteenInfo)
        # Get name of canteen
        canteenName = canteenInfo[0]

        # Get providerID with canteenName through lists above
        if canteenName in rtCanteens:
            providerID = getID(conn, 'Rahva Toit')
        elif canteenName in breasCanteens:
            providerID = getID(conn, 'Baltic Restaurants Estonia AS')
        else:
            providerID = getID(conn, 'TTÜ Sport OÜ')

        cur.execute(sql, variables)

def getID(conn, provider):
    """
    Get provider ID from PROVIDER table to insert into canteen
    :param conn: connection object
    :param provider: provider string to insert into table
    :return providerID: ID of provider in table PROVIDER
    """
    cur = conn.cursor()
    for row in cur.execute("SELECT ID FROM PROVIDER where ProviderName=?", (provider,)):
        providerID = row[0]
    return providerID

def task3(conn):
    """
    Query all rows and get canteens that are open 16.15-18.00
    :param conn: connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("""SELECT * FROM CANTEEN WHERE time_open < 16.15 AND time_closed > 18.00""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def task4(conn, ProviderID):
    """
    Query all rows and get canteens served by Rahva Toit
    :param conn: connection object
    :param ProviderID: provider to check for
    :return:
    """
    cur = conn.cursor()
    cur.execute("""SELECT * FROM CANTEEN WHERE ProviderID=?""", (ProviderID,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    # constants for sql queries, not used because they are already done.
    sql_canteen_table = '''CREATE TABLE IF NOT EXISTS CANTEEN(
                            ID integer PRIMARY KEY,
                            ProviderID text NOT NULL,
                            Name text NOT NULL,
                            Location text NOT NULL,
                            time_open integer NOT NULL,
                            time_closed integer NOT NULL)'''
    sql_provider_table = '''CREATE TABLE IF NOT EXISTS PROVIDER(
                            ID integer PRIMARY KEY,
                            ProviderName text NOT NULL)'''

    # constant list for providers, already done
    providers = ['Rahva Toit', 'Baltic Restaurants Estonia AS', 'TTÜ Sport OÜ']

    # data to insert into sql database, already done
    canteen_data =[('Library canteen', 'Ehitajate tee 7', 8.30, 19.00),
                ('Main building Deli cafe', 'Ehitajate tee 5', 9.00, 16.30),
                ('Main building Daily lunch restaurant', 'Ehitajate tee 5', 9.00, 16.30),
                ('U06 building canteen', '', 9.00, 16.00),
                ('Natural Science building canteen', 'Akadeemia tee 15', 9.00, 16.00),
                ('ICT building canteen', 'Raja 15', 9.00, 16.00),
                ('Sports building canteen', 'Männiliiva 7', 11.00, 20.00)]


    db = "./DINERS"
    conn = create_connection(db)
    with conn:

        # Create tables, already done
        #create_table(conn, sql_canteen_table)
        #create_table(conn, sql_provider_table)

        # Create canteens, not necessary as canteens are done
        #create_canteens(conn, canteen_data)

        # Create providers, not necessary as providers are done
        #for provider in providers:
            #create_provider(conn, provider)

        # Insert ITCollege data as one list, not necessary as its done
        # PS : i dont know who gives bitstop food :)
        #cur = conn.cursor()
        #cur.execute("""INSERT INTO CANTEEN(ProviderID, Name, Location,time_open, time_closed) VALUES('?', 'bitStop KOHVIK', 'Raja 4c', 9.30, 16.00)""")

        # Query all canteens between certain time (task 3)
        print("\nGetting queries for canteens open 16.15 - 18.00 \n")
        task3(conn)

        # Query canteens serviced by Rahva toit
        # Get id of "Rahva Toit"
        rtID = getID(conn, "Rahva Toit")
        print("\nGetting queries for Rahva Toit, ID: {} \n".format(rtID))
        task4(conn, rtID)

if __name__ == '__main__':
    main()

"""
This comment has the sql statements for creating the database,
tables and inserting the rows

    sql_canteen_table = '''CREATE TABLE IF NOT EXISTS CANTEEN(
                            ID integer PRIMARY KEY,
                            ProviderID text NOT NULL,
                            Name text NOT NULL,
                            Location text NOT NULL,
                            time_open integer NOT NULL,
                            time_closed integer NOT NULL)'''
    sql_provider_table = '''CREATE TABLE IF NOT EXISTS PROVIDER(
                            ID integer PRIMARY KEY,
                            ProviderName text NOT NULL)'''
create_table(conn, sql_canteen_table)
create_table(conn, sql_provider_table)

providers = ['Rahva Toit', 'Baltic Restaurants Estonia AS', 'TTÜ Sport OÜ']
    for provider in providers:
        create_provider(conn, provider)

canteen_data =[('Library canteen', 'Ehitajate tee 7', 8.30, 19.00),
                ('Main building Deli cafe', 'Ehitajate tee 5', 9.00, 16.30),
                ('Main building Daily lunch restaurant', 'Ehitajate tee 5', 9.00, 16.30),
                ('U06 building canteen', '', 9.00, 16.00),
                ('Natural Science building canteen', 'Akadeemia tee 15', 9.00, 16.00),
                ('ICT building canteen', 'Raja 15', 9.00, 16.00),
                ('Sports building canteen', 'Männiliiva 7', 11.00, 20.00)]
"""
