from tkinter import *
import mysql.connector
def create_cricket_database():
    connection = None  # Ensure connection is defined in the outer scope
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sarfraz9628'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Check if the database exists and create it if it does not
            cursor.execute("CREATE DATABASE IF NOT EXISTS cricket_broadcast_DB")
            print("Database 'cricket_broadcast_DB' has been created or already exists.")

            # Use the created database
            cursor.execute("USE cricket_broadcast_DB")

            # Define the DDL commands for the tables
            ddl_commands = [
                """CREATE TABLE IF NOT EXISTS bowlerstatsteam1 (
                    arm INT NOT NULL,
                    bowler VARCHAR(45) DEFAULT NULL,
                    bowlerstats VARCHAR(45) DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS bowlerstatsteam2 (
                    arm INT NOT NULL,
                    bowler VARCHAR(45) DEFAULT NULL,
                    bowlerstats VARCHAR(45) DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS extrasteam1 (
                    arm INT NOT NULL,
                    team1extras INT DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS extrateam2 (
                    arm INT NOT NULL,
                    team2extra INT DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS finishmatch (
                    matchno INT NOT NULL,
                    winningteam VARCHAR(45) DEFAULT NULL,
                    winmargin VARCHAR(45) DEFAULT NULL,
                    mom VARCHAR(45) DEFAULT NULL,
                    loosingteam VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (matchno)
                )""",
                """CREATE TABLE IF NOT EXISTS initialinfo (
                    matchno INT NOT NULL,
                    ground VARCHAR(45) DEFAULT NULL,
                    toss VARCHAR(45) DEFAULT NULL,
                    tosschoice VARCHAR(45) DEFAULT NULL,
                    team1 VARCHAR(45) DEFAULT NULL,
                    team1player1 VARCHAR(45) DEFAULT NULL,
                    team1player1shirtno VARCHAR(45) DEFAULT NULL,
                    team1player2 VARCHAR(45) DEFAULT NULL,
                    team1player2shirtno INT DEFAULT NULL,
                    team1player3 VARCHAR(45) DEFAULT NULL,
                    team1player3shirtno VARCHAR(45) DEFAULT NULL,
                    team1player4 VARCHAR(45) DEFAULT NULL,
                    team1player4shirtno VARCHAR(45) DEFAULT NULL,
                    team1player5 VARCHAR(45) DEFAULT NULL,
                    team1player5shirtno VARCHAR(45) DEFAULT NULL,
                    team1player6 VARCHAR(45) DEFAULT NULL,
                    team1player6shirtno VARCHAR(45) DEFAULT NULL,
                    team1player7 VARCHAR(45) DEFAULT NULL,
                    team1player7shirtno VARCHAR(45) DEFAULT NULL,
                    team1player8 VARCHAR(45) DEFAULT NULL,
                    team1player8shirtno VARCHAR(45) DEFAULT NULL,
                    team1player9 VARCHAR(45) DEFAULT NULL,
                    team1player9shirtno VARCHAR(45) DEFAULT NULL,
                    team1player10 VARCHAR(45) DEFAULT NULL,
                    team1player10shirtno VARCHAR(45) DEFAULT NULL,
                    team1player11 VARCHAR(45) DEFAULT NULL,
                    team1player11shirtno VARCHAR(45) DEFAULT NULL,
                    team2 VARCHAR(45) DEFAULT NULL,
                    team2player1 VARCHAR(45) DEFAULT NULL,
                    team2player1shirtno VARCHAR(45) DEFAULT NULL,
                    team2player2 VARCHAR(45) DEFAULT NULL,
                    team2player2shirtno VARCHAR(45) DEFAULT NULL,
                    team2player3 VARCHAR(45) DEFAULT NULL,
                    team2player3shirtno VARCHAR(45) DEFAULT NULL,
                    team2player4 VARCHAR(45) DEFAULT NULL,
                    team2player4shirtno VARCHAR(45) DEFAULT NULL,
                    team2player5 VARCHAR(45) DEFAULT NULL,
                    team2player5shirtno VARCHAR(45) DEFAULT NULL,
                    team2player6 VARCHAR(45) DEFAULT NULL,
                    team2player6shirtno VARCHAR(45) DEFAULT NULL,
                    team2player7 VARCHAR(45) DEFAULT NULL,
                    team2player7shirtno VARCHAR(45) DEFAULT NULL,
                    team2player8 VARCHAR(45) DEFAULT NULL,
                    team2player8shirtno VARCHAR(45) DEFAULT NULL,
                    team2player9 VARCHAR(45) DEFAULT NULL,
                    team2player9shirtno VARCHAR(45) DEFAULT NULL,
                    team2player10 VARCHAR(45) DEFAULT NULL,
                    team2player10shirtno VARCHAR(45) DEFAULT NULL,
                    team2player11 VARCHAR(45) DEFAULT NULL,
                    team2player11shirtno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (matchno)
                )""",
                """CREATE TABLE IF NOT EXISTS scoreboard1 (
                    arm INT NOT NULL,
                    striker VARCHAR(45) DEFAULT NULL,
                    strikerscore VARCHAR(45) DEFAULT NULL,
                    nonstriker VARCHAR(45) DEFAULT NULL,
                    `nonstriker score` VARCHAR(45) DEFAULT NULL,
                    team1 VARCHAR(45) DEFAULT NULL,
                    runswickets VARCHAR(45) DEFAULT NULL,
                    `over` VARCHAR(45) DEFAULT NULL,
                    bowler VARCHAR(45) DEFAULT NULL,
                    bowlerstats VARCHAR(45) DEFAULT NULL,
                    note VARCHAR(45) DEFAULT NULL,
                    impact VARCHAR(45) DEFAULT NULL,
                    team2 VARCHAR(45) DEFAULT NULL,
                    overstats VARCHAR(45) DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS team1wickets (
                    arm INT NOT NULL,
                    striker VARCHAR(45) DEFAULT NULL,
                    strikerscore VARCHAR(45) DEFAULT NULL,
                    bowler VARCHAR(45) DEFAULT NULL,
                    `over` VARCHAR(45) DEFAULT NULL,
                    bowlerstats VARCHAR(45) DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )""",
                """CREATE TABLE IF NOT EXISTS team2wickets (
                    arm INT NOT NULL,
                    striker VARCHAR(45) DEFAULT NULL,
                    strikerscore VARCHAR(45) DEFAULT NULL,
                    bowler VARCHAR(45) DEFAULT NULL,
                    `over` VARCHAR(45) DEFAULT NULL,
                    bowlerstats VARCHAR(45) DEFAULT NULL,
                    matchno VARCHAR(45) DEFAULT NULL,
                    PRIMARY KEY (arm)
                )"""
            ]

            # Execute each DDL command
            for command in ddl_commands:
                cursor.execute(command)

            print("All tables have been created successfully.")

    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to create the database and tables
create_cricket_database()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sarfraz9628",
    database="cricket_broadcast_DB")

mycursor=mydb.cursor()
root1=None
windownewstart=None
windowfirst=None
window1=None
window2=None
window=None
label1=None
label2=None
label3=None
label4=None
label5=None
label6=None
label8=None
label9=None
label10=None
label11=None
label13=None
label14=None
windowbatterteam1=None
labelrunteam1batwin=None        
labeloverteam1batwin=None        
labelextrasteam1batwin=None
labelrunteam1bowlwin=None
labeloverteam1bowlwin=None
labelextrasteam1bowlwin=None
labelteam1runsbatter1 = None
labelteam1runsbatter2 = None
labelteam1runsbatter3 = None
labelteam1runsbatter4 = None
labelteam1runsbatter5 = None
labelteam1runsbatter6 = None
labelteam1runsbatter7 = None
labelteam1runsbatter8 = None
labelteam1runsbatter9 = None
labelteam1runsbatter10 = None
labelteam1runsbatter11 = None
labelteam1wicketbatter1 = None
labelteam1wicketbatter2 = None
labelteam1wicketbatter3 = None
labelteam1wicketbatter4 = None
labelteam1wicketbatter5 = None
labelteam1wicketbatter6 = None
labelteam1wicketbatter7 = None
labelteam1wicketbatter8 = None
labelteam1wicketbatter9 = None
labelteam1wicketbatter10 = None
labelteam1wicketbatter11 = None
# Variable definitions for team2
windowbatterteam2 = None
labelrunteam2batwin=None
labeloverteam2batwin=None
labelextrasteam2batwin=None
labelrunteam2bowlwin=None
labeloverteam2bowlwin=None
labelextrasteam2bowlwin=None
labelteam2runsbatter1 = None
labelteam2runsbatter2 = None
labelteam2runsbatter3 = None
labelteam2runsbatter4 = None
labelteam2runsbatter5 = None
labelteam2runsbatter6 = None
labelteam2runsbatter7 = None
labelteam2runsbatter8 = None
labelteam2runsbatter9 = None
labelteam2runsbatter10 = None
labelteam2runsbatter11 = None
labelteam2wicketbatter1 = None
labelteam2wicketbatter2 = None
labelteam2wicketbatter3 = None
labelteam2wicketbatter4 = None
labelteam2wicketbatter5 = None
labelteam2wicketbatter6 = None
labelteam2wicketbatter7 = None
labelteam2wicketbatter8 = None
labelteam2wicketbatter9 = None
labelteam2wicketbatter10 = None
labelteam2wicketbatter11 = None

windowbowlerteam1=None
labelteam1wicketsbowler1 = None
labelteam1runsbowler1 = None
labelteam1overbowler1 = None
labelteam1wicketsbowler2 = None
labelteam1runsbowler2 = None
labelteam1overbowler2 = None
labelteam1wicketsbowler3 = None
labelteam1runsbowler3 = None
labelteam1overbowler3 = None
labelteam1wicketsbowler4 = None
labelteam1runsbowler4 = None
labelteam1overbowler4 = None
labelteam1wicketsbowler5 = None
labelteam1runsbowler5 = None
labelteam1overbowler5 = None
labelteam1wicketsbowler6 = None
labelteam1runsbowler6 = None
labelteam1overbowler6 = None
labelteam1wicketsbowler7 = None
labelteam1runsbowler7 = None
labelteam1overbowler7 = None
labelteam1wicketsbowler8 = None
labelteam1runsbowler8 = None
labelteam1overbowler8 = None

windowbowlerteam2= None
labelteam2wicketsbowler1 = None
labelteam2runsbowler1 = None
labelteam2overbowler1 = None
labelteam2wicketsbowler2 = None
labelteam2runsbowler2 = None
labelteam2overbowler2 = None
labelteam2wicketsbowler3 = None
labelteam2runsbowler3 = None
labelteam2overbowler3 = None
labelteam2wicketsbowler4 = None
labelteam2runsbowler4 = None
labelteam2overbowler4 = None
labelteam2wicketsbowler5 = None
labelteam2runsbowler5 = None
labelteam2overbowler5 = None
labelteam2wicketsbowler6 = None
labelteam2runsbowler6 = None
labelteam2overbowler6 = None
labelteam2wicketsbowler7 = None
labelteam2runsbowler7 = None
labelteam2overbowler7 = None
labelteam2wicketsbowler8 = None
labelteam2runsbowler8 = None
labelteam2overbowler8 = None
labelteam1wicketsbowler1 = None
labelteam1runsbowler1 = None
labelteam1overbowler1 = None
labelteam1wicketsbowler2 = None
labelteam1runsbowler2 = None
labelteam1overbowler2 = None
labelteam1wicketsbowler3 = None
labelteam1runsbowler3 = None
labelteam1overbowler3 = None
labelteam1wicketsbowler4 = None
labelteam1runsbowler4 = None
labelteam1overbowler4 = None
labelteam1wicketsbowler5 = None
labelteam1runsbowler5 = None
labelteam1overbowler5 = None
labelteam1wicketsbowler6 = None
labelteam1runsbowler6 = None
labelteam1overbowler6 = None
labelteam1wicketsbowler7 = None
labelteam1runsbowler7 = None
labelteam1overbowler7 = None
labelteam1wicketsbowler8 = None
labelteam1runsbowler8 = None
labelteam1overbowler8 = None

entrywindow=None
strikervalue_entry = None
strikerscorevalue_entry = None
nonstrikervalue_entry = None
nonstrikerscorevalue_entry = None
team1value_entry = None
team2value_entry = None
impactvalue_entry = None
team1scoreteam2value_entry = None
overvalue_entry = None
bowlervalue_entry = None
bowlerstatsvalue_entry = None
overstatsvalue_entry = None
notevalue_entry = None
armvalue_entry = None

# Team 1 Variables
team1wicket1_bat = None
team1wicket2_bat = None
team1wicket3_bat = None
team1wicket4_bat = None
team1wicket5_bat = None
team1wicket6_bat = None
team1wicket7_bat = None
team1wicket8_bat = None
team1wicket9_bat = None
team1wicket10_bat = None

# Team 2 Variables
team2wicket1_bat = None
team2wicket2_bat = None
team2wicket3_bat = None
team2wicket4_bat = None
team2wicket5_bat = None
team2wicket6_bat = None
team2wicket7_bat = None
team2wicket8_bat = None
team2wicket9_bat = None
team2wicket10_bat = None
# Team 1 Bowlers
team1wicket1bowl = None
team1wicket2bowl = None
team1wicket3bowl = None
team1wicket4bowl = None
team1wicket5bowl = None
team1wicket6bowl = None
team1wicket7bowl = None
team1wicket8bowl = None
team1wicket9bowl = None
team1wicket10bowl = None

# Team 2 Bowlers
team2wicket1bowl = None
team2wicket2bowl = None
team2wicket3bowl = None
team2wicket4bowl = None
team2wicket5bowl = None
team2wicket6bowl = None
team2wicket7bowl = None
team2wicket8bowl = None
team2wicket9bowl = None
team2wicket10bowl = None

from tkinter import messagebox
import sys
def quit_idle():
    global window1, windowbatterteam1, windowbowlerteam1, windowbatterteam2, windowbowlerteam2, entrywindow, windowfirst, root1
    try:
        print("quit")
        # Create a hidden Tkinter root window for the message box
        root = Tk()
        root.withdraw()  # Hide the root window to only show the message box

        # Show a confirmation message box
        response = messagebox.askyesno("Quit", "Are you sure you want to quit?")

        if response:  # If the user clicks 'Yes'
            # List all window variables to check and destroy
            windows_to_close = [
                window1, windowbatterteam1, windowbowlerteam1, 
                windowbatterteam2, windowbowlerteam2, entrywindow, 
                windowfirst, root1
            ]

            # Loop through and destroy each window if it's not None
            for window in windows_to_close:
                try:
                    if window is not None:
                        window.destroy()  # Destroy the window
                except Exception as e:
                    print(f"Error destroying a window: {e}")

            try:
                root.quit()  # Quit the main event loop
                root.destroy()  # Destroy the root window
            except Exception as e:
                print(f"Error quitting root: {e}")

            sys.exit("Exiting the application.")
        else:  # If the user clicks 'No'
            print("Canceled quitting.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
import mysql.connector
from mysql.connector import Error

def truncate_tables():
    try:
        # Connect to the cricket_broadcast_DB
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sarfraz9628',
            database='cricket_broadcast_DB'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # List of tables to truncate
            tables = [
                "bowlerstatsteam1",
                "bowlerstatsteam2",
                "extrasteam1",
                "extrateam2",
                "finishmatch",
                "initialinfo",
                "scoreboard1",
                "team1wickets",
                "team2wickets"
            ]

            # Disable foreign key checks to avoid issues with dependent tables
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

            # Truncate each table
            for table in tables:
                cursor.execute(f"TRUNCATE TABLE {table};")
                #print(f"Table '{table}' truncated successfully.")

            # Re-enable foreign key checks
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
            messagebox.showinfo("SUCESS", "App Got Reset successfully.")
            

    except Error as e:
        print(f"An error occurred while truncating tables: {e}")
    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def refresh(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry):
    global mycursor, mydb
    try:
        # Fetch the latest match number from the initialinfo table
        mycursor.execute("SELECT * FROM initialinfo")
        myresult = mycursor.fetchall()
        p = myresult[-1]
        matchno = p[0]  # Latest match number

        # List of tables to delete records from
        tables = [
            "scoreboard1", "team1wickets", "team2wickets", "extrasteam1", 
            "extrateam2", "bowlerstatsteam1", "bowlerstatsteam2"
        ]

        # Loop through each table and delete records for the specified match number
        for table in tables:
            sqlformula = f"DELETE FROM {table} WHERE matchno = %s"
            mycursor.execute(sqlformula, (matchno,))

        # Commit all changes
        mydb.commit()

        # Show a success message
        messagebox.showinfo("Success", f"All records for match number {matchno} have been deleted.")
        try:
            mycursor.execute("SELECT * FROM scoreboard1")
            k=mycursor.fetchall()
            M=k[-1][0]+1
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', {matchno.get()})")
            mydb.commit()
            #scoresentry()
            print("done1")
        except Exception as e:
            #print(e)
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            M=0
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', {matchno.get()})")
            print("done")
            mydb.commit()
            #scoresentry()

        # Refresh relevant sections
        scoresentry()
        scoreboard()
        detailsbatter(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)
        detailsbowler(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)

    except Exception as e:
        # Show an error message in case of failure
        messagebox.showerror("Error", f"An error occurred: {e}")

def define(striker,nonstriker,team1,team2,bowler):
    mycursor.execute("SELECT * from initialinfo")
    myresult=mycursor.fetchall()
    p=myresult[-1]

    if team2==p[27] and team1==p[4]:

        if striker==p[6]:
            striker=p[5]            
        elif striker==p[8]:
            striker=p[7]
        elif striker==p[10]:
            striker=p[9]
        elif striker==p[12]:
            striker=p[11]            
        elif striker==p[14]:
            striker=p[13]
        elif striker==p[16]:
            striker=p[15]
        elif striker==p[18]:
            striker=p[17]
        elif striker==p[20]:
            striker=p[19]
        elif striker==p[22]:
            striker=p[21]
        elif striker==p[24]:
            striker=p[23]
        elif striker==p[26]:
            striker=p[25]
        if nonstriker==(p[6]):
            nonstriker=p[5]
        elif nonstriker==p[8]:
            nonstriker=p[7]
        elif nonstriker==p[10]:
            nonstriker=p[9]
        elif nonstriker==p[12]:
            nonstriker=p[11]
        elif nonstriker==p[14]:
            nonstriker=p[13]
        elif nonstriker==p[16]:
            nonstriker=p[15]
        elif nonstriker==p[18]:
            nonstriker=p[17]
        elif nonstriker==p[20]:
            nonstriker=p[19]
        elif nonstriker==p[22]:
            nonstriker=p[21]
        elif nonstriker==p[24]:
            nonstriker=p[23]
        elif nonstriker==p[26]:
            nonstriker=p[25]
        
        if bowler==p[35]:
            bowler=p[34]
        elif bowler==p[37]:
            bowler=p[36]
        elif bowler==p[39]:
            bowler=p[38]
        elif bowler==p[41]:
            bowler=p[40]
        elif bowler==p[43]:
            bowler=p[42]
        elif bowler==p[45]:
            bowler=p[44]
        elif bowler==p[47]:
            bowler=p[46]
        elif bowler==p[49]:
            bowler=p[48]
            
        
    
    elif team1==p[27] and team2==p[4]:

        if striker==p[29]:
            striker=p[28]
        elif striker==p[31]:
            striker=p[30]
        elif striker==p[33]:
            striker=p[32]
        elif striker==p[35]:
            striker=p[34]
        elif striker==p[37]:
            striker=p[36]
        elif striker==p[39]:
            striker=p[38]
        elif striker==p[41]:
            striker=p[40]
        elif striker==p[43]:
            striker=p[42]
        elif striker==p[45]:
            striker=p[44]
        elif striker==p[47]:
            striker=p[46]
        elif striker==p[49]:
            striker=p[48]
        if nonstriker==p[29]:
            nonstriker=p[28]
        elif nonstriker==p[31]:
            nonstriker=p[30]
        elif nonstriker==p[33]:
            nonstriker=p[32]
        elif nonstriker==p[35]:
            nonstriker=p[34]
        elif nonstriker==p[37]:
            nonstriker=p[36]
        elif nonstriker==p[39]:
            nonstriker=p[38]
        elif nonstriker==p[41]:
            nonstriker=p[40]
        elif nonstriker==p[43]:
            nonstriker=p[42]
        elif nonstriker==p[45]:
            nonstriker=p[44]
        elif nonstriker==p[47]:
            nonstriker=p[46]
        elif nonstriker==p[49]:
            nonstriker=p[48]
        if bowler==p[12]:
            bowler=p[11]
        elif bowler==p[14]:
            bowler=p[13]
        elif bowler==p[16]:
            bowler=p[15]
        elif bowler==p[18]:
            bowler=p[17]
        elif bowler==p[20]:
            bowler=p[19]
        elif bowler==p[22]:
            bowler=p[21]
        elif bowler==p[24]:
            bowler=p[23]
        elif bowler==p[26]:
            bowler=p[25]

    return striker,nonstriker,team1,team2,bowler


def naa():
    #returns latest match no.
    mycursor.execute("SELECT * from initialinfo")
    myresult=mycursor.fetchall()
    if len(myresult)!=0:            
        p=myresult[-1]    
        return p[0]
    else:
        messagebox.showinfo("NOTE","0 MATCHES TO CONTINUE, PLEASE START A NEW MATCH")
        quit_idle()


from tkinter import messagebox  # Importing the messagebox
def delete(strikervalue, strikerscorevalue, nonstrikervalue, nonstrikerscorevalue,
           team1value, team1scoreteam2value, overvalue, bowlervalue, bowlerstatsvalue,
           overstatsvalue, notevalue, impactvalue, team2value, armvalue):
    team1scoreteam2value_edit2,   strikerscorevalue_edit2  ,bowlerstatsvalue_edit2  ,overstatsvalue_edit2,overvalue_edit2=unentryupdate(strikerscorevalue,impactvalue,team1scoreteam2value,overvalue,bowlerstatsvalue,overstatsvalue,notevalue,armvalue,team2value,bowlervalue)            
    print(team1scoreteam2value_edit2,   strikerscorevalue_edit2  ,bowlerstatsvalue_edit2,overstatsvalue_edit2,overvalue_edit2)


    strikerscorevalue.delete(0, END)
    strikerscorevalue.insert(0,strikerscorevalue_edit2 )
    
    team1scoreteam2value.delete(0, END)
    team1scoreteam2value_entry.insert(0,team1scoreteam2value_edit2)

    overvalue.delete(0, END)
    overvalue.insert(0, overvalue_edit2)


    # Clear and update the bowler's stats
    bowlerstatsvalue.delete(0, END)
    bowlerstatsvalue.insert(0, bowlerstatsvalue_edit2)

    # Clear and update the over stats
    overstatsvalue.delete(0, END)
    overstatsvalue.insert(0, overstatsvalue_edit2)
    global mycursor, mydb
    
    try:
        striker = strikervalue.get()
        strikerscore = strikerscorevalue.get()
        nonstriker = nonstrikervalue.get()
        nonstrikerscore = nonstrikerscorevalue.get()
        team1 = team1value.get()
        over = overvalue.get()
        bowler = bowlervalue.get()
        bowlerstats = bowlerstatsvalue.get()
        overstats = overstatsvalue.get()
        note = notevalue.get()
        impact = impactvalue.get()
        team1scoreteam2 = team1scoreteam2value.get()
        team2 = team2value.get()

        # Get the `arm` value from the entry
        arm = armvalue_entry.get()

        # Fetch the match number for validation
        mycursor.execute("SELECT * FROM initialinfo")
        myresult = mycursor.fetchall()
        p = myresult[-1]
        matchno = p[0]

        # Delete the record from the primary scoreboard table
        sqlformula = "DELETE FROM scoreboard1 WHERE arm = %s AND matchno = %s"
        entries = (arm, matchno)
        mycursor.execute(sqlformula, entries)

        # Delete associated records from other tables
        tables = [
            "team1wickets", "team2wickets", "extrasteam1", "extrateam2",
            "bowlerstatsteam1", "bowlerstatsteam2"
        ]
        for table in tables:
            sqlformula = f"DELETE FROM {table} WHERE arm = %s AND matchno = %s"
            mycursor.execute(sqlformula, entries)

        # Commit all changes
        mydb.commit()

        # Show a success message
        messagebox.showinfo("Success", f"Records for arm {arm} have been deleted.")

        # Refresh relevant sections
        scoresentry()
        scoreboard()
        detailsbatter(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)
        detailsbowler(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)
    
    except Exception as e:
        # Show an error message in case of failure
        messagebox.showerror("Error", f"An error occurred: {e}")


from tkinter import messagebox  # Importing the messagebox
def update(strikervalue, strikerscorevalue, nonstrikervalue, nonstrikerscorevalue,
           team1value, team1scoreteam2value, overvalue, bowlervalue, bowlerstatsvalue,
           overstatsvalue, notevalue, impactvalue, team2value, armvalue):
    team1scoreteam2value_edit2,   strikerscorevalue_edit2  ,bowlerstatsvalue_edit2  ,overstatsvalue_edit2,overvalue_edit2=unentryupdate(strikerscorevalue,impactvalue,team1scoreteam2value,                                                                                                                                       overvalue,bowlerstatsvalue,overstatsvalue,notevalue,armvalue,team2value,bowlervalue)            
    strikerscorevalue.delete(0, END)
    strikerscorevalue.insert(0,strikerscorevalue_edit2 )
    
    team1scoreteam2value.delete(0, END)
    team1scoreteam2value_entry.insert(0,team1scoreteam2value_edit2)

    overvalue.delete(0, END)
    overvalue.insert(0, overvalue_edit2)


    # Clear and update the bowler's stats
    bowlerstatsvalue.delete(0, END)
    bowlerstatsvalue.insert(0, bowlerstatsvalue_edit2)

    # Clear and update the over stats
    overstatsvalue.delete(0, END)
    overstatsvalue.insert(0, overstatsvalue_edit2)
    global scoreshow
    try:
        # Get values from the input fields
        striker = strikervalue.get()
        arm = armvalue.get()
        strikerscore = strikerscorevalue.get()
        nonstriker = nonstrikervalue.get()
        nonstrikerscore = nonstrikerscorevalue.get()
        team1 = team1value.get()
        over = overvalue.get()
        bowler = bowlervalue.get()
        bowlerstats = bowlerstatsvalue.get()
        overstats = overstatsvalue.get()
        note = notevalue.get()
        impact = impactvalue.get()
        team1scoreteam2 = team1scoreteam2value.get()
        team2 = team2value.get()

        # Fetch the match number for validation
        mycursor.execute("SELECT * FROM initialinfo")
        myresult = mycursor.fetchall()
        p = myresult[-1]
        matchno = p[0]

        # Update the scoreboard for the specific `arm`
        sqlformula = """UPDATE scoreboard1 
                        SET striker = %s, strikerscore = %s, nonstriker = %s, `nonstriker score` = %s, 
                            team1 = %s, runswickets = %s, `over` = %s, bowler = %s, bowlerstats = %s, 
                            note = %s, impact = %s, team2 = %s, overstats = %s
                        WHERE arm = %s AND matchno = %s"""

        entries = (striker, strikerscore, nonstriker, nonstrikerscore, team1, team1scoreteam2,
                   over, bowler, bowlerstats, note, impact, team2, overstats, arm, matchno)

        mycursor.execute(sqlformula, entries)
        mydb.commit()

        # Additional Updates for Specific Tables Based on Conditions
        if note.lower() in ["wicket", "w"]:
            if team1 == p[4]:  # Team 1
                sqlformula = """UPDATE team1wickets 
                                SET striker = %s, strikerscore = %s, bowler = %s, `over` = %s, bowlerstats = %s
                                WHERE arm = %s AND matchno = %s"""
                entries1 = (striker, strikerscore, bowler, over, bowlerstats, arm, matchno)
                mycursor.execute(sqlformula, entries1)
            elif team1 == p[27]:  # Team 2
                sqlformula = """UPDATE team2wickets 
                                SET striker = %s, strikerscore = %s, bowler = %s, `over` = %s, bowlerstats = %s
                                WHERE arm = %s AND matchno = %s"""
                entries1 = (striker, strikerscore, bowler, over, bowlerstats, arm, matchno)
                mycursor.execute(sqlformula, entries1)

        if note.lower().startswith("extra"):
            extra_type = note[5:]
            if team1 == p[4]:  # Team 1
                sqlformula = """UPDATE extrasteam1 
                                SET extra_type = %s
                                WHERE arm = %s AND matchno = %s"""
                entries1 = (extra_type, arm, matchno)
                mycursor.execute(sqlformula, entries1)
            elif team1 == p[27]:  # Team 2
                sqlformula = """UPDATE extrateam2 
                                SET extra_type = %s
                                WHERE arm = %s AND matchno = %s"""
                entries1 = (extra_type, arm, matchno)
                mycursor.execute(sqlformula, entries1)

        if team2 == p[4]:  # Bowler stats for Team 1
            sqlformula = """UPDATE bowlerstatsteam1 
                            SET bowler = %s, bowlerstats = %s
                            WHERE arm = %s AND matchno = %s"""
            entries1 = (bowler, bowlerstats, arm, matchno)
            mycursor.execute(sqlformula, entries1)
        elif team2 == p[27]:  # Bowler stats for Team 2
            sqlformula = """UPDATE bowlerstatsteam2 
                            SET bowler = %s, bowlerstats = %s
                            WHERE arm = %s AND matchno = %s"""
            entries1 = (bowler, bowlerstats, arm, matchno)
            mycursor.execute(sqlformula, entries1)

        # Commit all changes
        mydb.commit()

        # Show a success message
        messagebox.showinfo("Success", f"Record for arm {arm} and match number {matchno} has been updated successfully.")

        # Refresh the scoreboard
        scoresentry()
        scoreboard()
        detailsbatter(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)
        detailsbowler(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry)

    except Exception as e:
        # Show an error message in case of failure
        messagebox.showerror("Error", f"An error occurred: {e}")
        
import tkinter as tk
from tkinter import messagebox

def submit(strikervalue, strikerscorevalue, nonstrikervalue, nonstrikerscorevalue,
           team1value, team1scoreteam2value, overvalue, bowlervalue, bowlerstatsvalue,
           overstatsvalue, notevalue, impactvalue, team2value, armvalue):



    team1scoreteam2value_edit2,   strikerscorevalue_edit2  ,bowlerstatsvalue_edit2  ,overstatsvalue_edit2,overvalue_edit2=unentryupdate(strikerscorevalue,impactvalue,team1scoreteam2value,
                      overvalue,bowlerstatsvalue,overstatsvalue,notevalue,armvalue,team2value,bowlervalue)            
    strikerscorevalue.delete(0, END)
    strikerscorevalue.insert(0,strikerscorevalue_edit2 )
    
    team1scoreteam2value.delete(0, END)
    team1scoreteam2value_entry.insert(0,team1scoreteam2value_edit2)

    overvalue.delete(0, END)
    overvalue.insert(0, overvalue_edit2)


    # Clear and update the bowler's stats
    bowlerstatsvalue.delete(0, END)
    bowlerstatsvalue.insert(0, bowlerstatsvalue_edit2)

    # Clear and update the over stats
    overstatsvalue.delete(0, END)
    overstatsvalue.insert(0, overstatsvalue_edit2)
            
    (team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)=(team1value,
                                                                                                                                                                     team2value,
                                                                                                                                                                     strikervalue,
                                                                                                                                                                     strikerscorevalue, nonstrikervalue,
                                                                                                                                                                     nonstrikerscorevalue,team1scoreteam2value, overvalue, )

    
    striker = strikervalue.get()
    arm = armvalue.get()
    strikerscore = strikerscorevalue.get()
    nonstriker = nonstrikervalue.get()
    nonstrikerscore = nonstrikerscorevalue.get()
    team1 = team1value.get()
    over = overvalue.get()
    bowler = bowlervalue.get()

    bowlerstats = bowlerstatsvalue.get() 
    overstats = overstatsvalue.get()
    note = notevalue.get()
    impact = impactvalue.get()
    team1scoreteam2 = team1scoreteam2value.get()
    team2 = team2value.get()
    
    mycursor.execute("SELECT * from initialinfo")
    myresult = mycursor.fetchall()
    p = myresult[-1]
    matchno = p[0]

    n = read()
    if n[0] != int(arm):
        runswickets = team1scoreteam2
        sqlformula = """INSERT INTO scoreboard1 (arm, striker, strikerscore, nonstriker, `nonstriker score`, team1, runswickets, `over`, bowler, bowlerstats, note, impact, team2, overstats, matchno) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        entries = (arm, striker, strikerscore, nonstriker, nonstrikerscore, team1, runswickets, over, bowler, bowlerstats, note, impact, team2, overstats, matchno)
        mycursor.execute(sqlformula, entries)
        mydb.commit()

        mycursor.execute("SELECT * from initialinfo")
        myresult = mycursor.fetchall()
        p = myresult[-1]

        arm = int(arm)
        striker, nonstriker, team1, team2, bowler = define(striker, nonstriker, team1, team2, bowler)
        
        if note == "WICKET" or note == "W" or note == "wicket":
            if team1 == p[4]:
                sqlformula = """INSERT INTO team1wickets VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                entries1 = (arm, striker, strikerscore, bowler, over, bowlerstats, matchno)
                mycursor.execute(sqlformula, entries1)
                mydb.commit()
            elif team1 == p[27]:
                sqlformula = """INSERT INTO team2wickets VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                entries1 = (arm, striker, strikerscore, bowler, over, bowlerstats, matchno)
                mycursor.execute(sqlformula, entries1)
                mydb.commit()

        if note[0:5] == "EXTRA":
            if team1 == p[4]:
                sqlformula = """INSERT INTO extrasteam1 VALUES (%s, %s, %s)"""
                entries1 = (arm, note[5:], matchno)
                mycursor.execute(sqlformula, entries1)
                mydb.commit()
            elif team1 == p[27]:
                sqlformula = """INSERT INTO extrateam2 VALUES (%s, %s, %s)"""
                entries1 = (arm, note[5:], matchno)
                mycursor.execute(sqlformula, entries1)
                mydb.commit()

        if team2 == p[4]:
            sqlformula = """INSERT INTO bowlerstatsteam1 VALUES (%s, %s, %s, %s)"""
            entries1 = (arm, bowler, bowlerstats, matchno)
            mycursor.execute(sqlformula, entries1)
            mydb.commit()
        elif team2 == p[27]:
            sqlformula = """INSERT INTO bowlerstatsteam2 VALUES (%s, %s, %s, %s)"""
            entries1 = (arm, bowler, bowlerstats, matchno)
            mycursor.execute(sqlformula, entries1)
            mydb.commit()

        # Show success message
        messagebox.showinfo("Success", "Data submitted successfully! and Updated The Graphics")
    detailsbowler(team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)
    detailsbatter(team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)
    scoreboard()


def scoreboard():
    global window1
    global label1, label2, label3, label4, label5, label6, label8, label9, label10, label11, label13, label14
    try:
        # Simulated input data (replace this with your actual `read()` function)
        new = read()
        striker = new[1]
        strikerscore = new[2]
        nonstriker = new[3]
        nonstrikerscore = new[4]
        team1 = new[5]
        team1scoreteam2 = new[6]
        over = new[7]
        team2 = new[12]
        bowler = new[8]
        bowlerstats = new[9]
        overstats = new[13]
        note = new[10]
        
        striker, nonstriker, team1, team2, bowler = define(striker, nonstriker, team1, team2, bowler)

        # Handle player switching logic
        if note=="DEAD" or note[0:5]=="EXTRA":
            pass
        else:
            if new[11] in ["1", "3", "0"] and new[6][-1] == "6":
                k = nonstrikervalue
                p = nonstrikerscorevalue
                nonstrikervalue = strikervalue
                nonstrikerscorevalue = strikerscorevalue
                strikervalue = k
                strikerscorevalue = p

        # Update existing window if it exists
        if window1 is not None: 
            label1.config(text=striker)
            label2.config(text=strikerscore)
            label3.config(text=nonstriker)
            label4.config(text=nonstrikerscore)
            label5.config(text=team1[0:3])
            label6.config(text=team1scoreteam2)
            label8.config(text=over)
            label9.config(text="VS " + team2[0:3])
            label10.config(text=bowler)
            label11.config(text=bowlerstats)        
            label13.config(text=overstats) 
            label14.config(text=note)
            scoresentry()
            
        else:
            window1 = Tk()
            window1.geometry("930x270")
            window1.config(background="black", padx=10, pady=2)
            window1.title("SCOREBOARD OVERLAY")

            # Player details
            label1 = Label(window1, width=10, text=str(striker), font=("Arial", 17, "bold"), bg="#0277BD", fg="white")
            label1.place(x=0, y=83)

            label2 = Label(window1, width=5, text=str(strikerscore), font=("Arial", 17), bg="#0277BD", fg="white")
            label2.place(x=160, y=83)

            label3 = Label(window1, width=10, text=str(nonstriker), font=("Arial", 17, "bold"), bg="#0288D1", fg="white")
            label3.place(x=0, y=127)

            label4 = Label(window1, width=5, text=str(nonstrikerscore), font=("Arial", 17), bg="#0288D1", fg="white")
            label4.place(x=160, y=127)

            # Team details
            label5 = Label(window1, width=5, text=str(team1[0:3]), fg="yellow", bg="#2E7D32", font=("Arial", 17, "bold"))
            label5.place(x=270, y=83)

            label6 = Label(window1, width=7, text=str(team1scoreteam2), fg="yellow", bg="#2E7D32", font=("Arial", 17, "bold"))
            label6.place(x=360, y=83)

            # Overs
            label7 = Label(window1, width=5, height=1, text="OVER", pady=9, padx=2, anchor="w", font=("Arial", 17, "bold"), fg="white", bg="#757575")
            label7.place(x=270, y=127)

            label8 = Label(window1, width=4, height=1, text=str(over), pady=8, font=("Arial", 17, "bold"), fg="white", bg="#757575")
            label8.place(x=345, y=127)

            label9 = Label(window1, width=7, height=2, text="VS " + str(team2[0:3]), font=("Arial", 10), bg="gray15", fg="white")
            label9.place(x=400, y=127)

            # Bowler details
            label10 = Label(window1, width=10, text=str(bowler), font=("Arial", 17, "bold"), fg="white", bg="#C62828")
            label10.place(x=500, y=83)

            label11 = Label(window1, width=10, text=str(bowlerstats), font=("Arial", 17, "bold"), fg="white", bg="#C62828")
            label11.place(x=660, y=83)

            # This Over
            label12 = Label(window1, width=10, text="THIS OVER", font=("Arial", 17, "bold"), fg="white", bg="#6A1B9A")
            label12.place(x=500, y=127)

            label13 = Label(window1, width=10, text=str(overstats), font=("Arial", 17, "bold"), fg="white", bg="#6A1B9A")
            label13.place(x=660, y=127)

            # Notes
            label14 = Label(window1, width=25, height=1, text=note, bg="#424242", fg="white", font=("Arial", 14))
            label14.place(x=0, y=35)
            

            scoresentry()
            
    except Exception as e:
        window1 = None
        label1 = label2 = label3 = label4 = label5 = label6 = None
        label8 = label9 = label10 = label11 = label13 = label14 = None

            # Optional: Reset global variables to prevent stale state
            
            # Optionally restart the function
            # Uncomment the next line if you want to retry the function on error
        scoreboard()
        
        scoresentry()
        
def read():
    #returns latest from scoreboard 1
    p=naa()
    query=("SELECT * from scoreboard1 where matchno=%s")
    mycursor.execute(query,(p,))
    myresult=mycursor.fetchall() 
    if len(myresult)>0:
        p=naa()
        query=("SELECT * from scoreboard1 where matchno=%s")
        mycursor.execute(query,(p,))
        myresult=mycursor.fetchall()
        return myresult[-1]
    else:
        try:
            mycursor.execute("SELECT * FROM scoreboard1")
            k=mycursor.fetchall()
            M=k[-1][0]+1
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', 1)")
            mydb.commit()
            scoresentry()
        except Exception as e:
            #print(e)
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            M=0
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', 1)")
            mydb.commit()
            scoresentry()
        p=naa()
        query=("SELECT * from scoreboard1 where matchno=%s")
        mycursor.execute(query,(p,))
        myresult=mycursor.fetchall()
        return myresult[-1]

def submitfinish(matchno,winningteam,winmargin,mom,loosingteam):
    matchnov=matchno.get()
    winningteamv=winningteam.get()
    winmarginv=winmargin.get()
    momv=mom.get()
    loosingteamv=loosingteam.get()
    sqlformula = """INSERT INTO finishmatch (matchno, winningteam, winmargin, mom, loosingteam) VALUES (%s, %s, %s, %s, %s)"""
    entries1=(matchnov,winningteamv,winmarginv,momv,loosingteamv)         
    mycursor.execute(sqlformula,entries1)
    mydb.commit()
    windowlast()
    
def windowlast():
    mycursor.execute("SELECT * from finishmatch")
    myresult=mycursor.fetchall()
    graphiclast=myresult[-1]


    # Create the main window
    windowlastg = Tk()
    windowlastg.geometry("700x550")
    windowlastg.title("SUMMARY OF THE LATEST MATCH")
    windowlastg.config(background="#2E3B4E", padx=30, pady=50, border=25)  # Background changed to a dark theme

    # Header Label
    header_label = Label(
        windowlastg,
        width=30,
        text="🏏 SUMMARY OF THE LAST MATCH 🏏",
        font=("Arial", 25, "bold"),
        bg="#1B263B",  # Darker header background
        fg="#FFFFFF",  # White font for contrast
        relief=RIDGE,
        bd=10
    )
    header_label.place(relx=0.5, y=20, anchor="center")  # Centered header

    # Match Number
    label_match_no = Label(
        windowlastg,
        width=30,
        text=f"MATCH NO.: {graphiclast[0]}",
        font=("Arial", 18),
        bg="#34495E",  # Subtle contrast
        fg="#ECF0F1",  # Light font color
        relief=RIDGE,
        bd=5
    )
    label_match_no.place(relx=0.5, y=80, anchor="center")

    # Winning Team
    label_winning_team = Label(
        windowlastg,
        width=30,
        text=f"WINNING TEAM: {graphiclast[1]}",
        font=("Arial", 18),
        bg="#34495E",
        fg="#ECF0F1",
        relief=RIDGE,
        bd=5
    )
    label_winning_team.place(relx=0.5, y=160, anchor="center")

    # Win Margin
    label_win_margin = Label(
        windowlastg,
        width=30,
        text=f"WIN MARGIN: {graphiclast[2]}",
        font=("Arial", 18),
        bg="#34495E",
        fg="#ECF0F1",
        relief=RIDGE,
        bd=10
    )
    label_win_margin.place(relx=0.5, y=240, anchor="center")

    # Man of the Match
    label_motm = Label(
        windowlastg,
        width=30,
        text=f"MAN OF THE MATCH: {graphiclast[3]}",
        font=("Arial", 18),
        bg="#34495E",
        fg="#ECF0F1",
        relief=RIDGE,
        bd=10
    )
    label_motm.place(relx=0.5, y=320, anchor="center")

    # Losing Team
    label_losing_team = Label(
        windowlastg,
        width=30,
        text=f"LOSING TEAM: {graphiclast[4]}",
        font=("Arial", 18),
        bg="#34495E",
        fg="#ECF0F1",
        relief=RIDGE,
        bd=10
    )
    label_losing_team.place(relx=0.5, y=400, anchor="center")    

def detailsbowler(team1,team2,strikervalue,strikerscorevalue,nonstrikervalue,nonstrikerscorevalue,
                  team1scoreteam2value,
                  overvalue):
    (team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)=(team1,team2,strikervalue,strikerscorevalue,nonstrikervalue,nonstrikerscorevalue,
                  team1scoreteam2value,
                  overvalue)
    team1=team1.get()
    team2=team2.get()
    striker,strikerscore,nonstriker,nonstrikerscore=strikervalue.get(),strikerscorevalue.get(),nonstrikervalue.get(),nonstrikerscorevalue.get()
    team1score=team1scoreteam2value.get()
    over=overvalue.get()
    
    mycursor.execute("SELECT * from initialinfo")
    myresult=mycursor.fetchall()
    p=myresult[-1]
    global labelrunteam1bowlwin,labeloverteam1bowlwin,labelextrasteam1bowlwin
    global labelrunteam2bowlwin,labeloverteam2bowlwin,labelextrasteam2bowlwin    
    global labelteam2wicketsbowler1
    global labelteam2runsbowler1
    global labelteam2overbowler1
    global labelteam2wicketsbowler2
    global labelteam2runsbowler2
    global labelteam2overbowler2
    global labelteam2wicketsbowler3
    global labelteam2runsbowler3
    global labelteam2overbowler3
    global labelteam2wicketsbowler4
    global labelteam2runsbowler4
    global labelteam2overbowler4
    global labelteam2wicketsbowler5
    global labelteam2runsbowler5
    global labelteam2overbowler5
    global labelteam2wicketsbowler6
    global labelteam2runsbowler6
    global labelteam2overbowler6
    global labelteam2wicketsbowler7
    global labelteam2runsbowler7
    global labelteam2overbowler7
    global labelteam2wicketsbowler8
    global labelteam2runsbowler8
    global labelteam2overbowler8
    global windowbowlerteam2

    global windowbowlerteam1
    global labelteam1wicketsbowler1, labelteam1runsbowler1, labelteam1overbowler1
    global labelteam1wicketsbowler2, labelteam1runsbowler2, labelteam1overbowler2
    global labelteam1wicketsbowler3, labelteam1runsbowler3, labelteam1overbowler3
    global labelteam1wicketsbowler4, labelteam1runsbowler4, labelteam1overbowler4
    global labelteam1wicketsbowler5, labelteam1runsbowler5, labelteam1overbowler5
    global labelteam1wicketsbowler6, labelteam1runsbowler6, labelteam1overbowler6
    global labelteam1wicketsbowler7, labelteam1runsbowler7, labelteam1overbowler7
    global labelteam1wicketsbowler8, labelteam1runsbowler8, labelteam1overbowler8

    global team1wicket1bowl, team1wicket2bowl, team1wicket3bowl, team1wicket4bowl, team1wicket5bowl
    global team1wicket6bowl, team1wicket7bowl, team1wicket8bowl, team1wicket9bowl, team1wicket10bowl
    global team2wicket1bowl, team2wicket2bowl, team2wicket3bowl, team2wicket4bowl, team2wicket5bowl
    global team2wicket6bowl, team2wicket7bowl, team2wicket8bowl, team2wicket9bowl, team2wicket10bowl
    
    if team2==p[4]:
        try:   
            if windowbowlerteam1 is not None:                
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    #print(i[8])
                    if i[8] not in namelist:
                        display.append(i)
                        namelist.append(i[8])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]
                p=naa()                
                myresult=mycursor.fetchall()
                mycursor.execute(f"SELECT * from extrateam2 where matchno={p}")
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    ##print(i)
                    n+=i[1]
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]

                labelrunteam2bowlwin.config(text=showdown[6])
                labeloverteam2bowlwin.config(text=showdown[7])
                labelextrasteam2bowlwin.config(text="EXTRAS  "+str(n))
                for show in display:
                    if show[8] == shirtno[26]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler1.config(text=displaystats[0])
                        labelteam1runsbowler1.config(text=displaystats[1])
                        labelteam1overbowler1.config(text=displaystats[2])

                    elif show[8] == shirtno[24]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler2.config(text=displaystats[0])
                        labelteam1runsbowler2.config(text=displaystats[1])
                        labelteam1overbowler2.config(text=displaystats[2])

                    elif show[8] == shirtno[22]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler3.config(text=displaystats[0])
                        labelteam1runsbowler3.config(text=displaystats[1])
                        labelteam1overbowler3.config(text=displaystats[2])

                    elif show[8] == shirtno[20]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler4.config(text=displaystats[0])
                        labelteam1runsbowler4.config(text=displaystats[1])
                        labelteam1overbowler4.config(text=displaystats[2])

                    elif show[8] == shirtno[18]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler5.config(text=displaystats[0])
                        labelteam1runsbowler5.config(text=displaystats[1])
                        labelteam1overbowler5.config(text=displaystats[2])

                    elif show[8] == shirtno[16]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler6.config(text=displaystats[0])
                        labelteam1runsbowler6.config(text=displaystats[1])
                        labelteam1overbowler6.config(text=displaystats[2])

                    elif show[8] == shirtno[14]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler7.config(text=displaystats[0])
                        labelteam1runsbowler7.config(text=displaystats[1])
                        labelteam1overbowler7.config(text=displaystats[2])

                    elif show[8] == shirtno[12]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler8.config(text=displaystats[0])
                        labelteam1runsbowler8.config(text=displaystats[1])
                        labelteam1overbowler8.config(text=displaystats[2])

                    elif show[8] == shirtno[10]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler9.config(text=displaystats[0])
                        labelteam1runsbowler9.config(text=displaystats[1])
                        labelteam1overbowler9.config(text=displaystats[2])
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                        
                count=0
                for wicket in display:
                    if count==0:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket1bowl.config(text=run[0])
                            count+=1
                    elif count==1:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket2bowl.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket3bowl.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket4bowl.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket5bowl.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket6bowl.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket7bowl.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket8bowl.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket9bowl.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket10bowl.config(text=run[0])
                            count+=1
            else:
                windowbowlerteam1 = Tk()
                windowbowlerteam1.geometry("700x630")
                windowbowlerteam1.title("BOWLERS STATS")
                windowbowlerteam1.config(background="lavender", padx=10, border=20)


                label = Label(windowbowlerteam1, width=40, text=team2, font=("Arial", 17, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=0, y=0)
                label = Label(windowbowlerteam1, width=15, text="BOWLER", font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=0, y=55)
                label = Label(windowbowlerteam1, width=15, text="WICKETS", font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=150, y=55)
                label = Label(windowbowlerteam1, width=15, text="RUNS", font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=300, y=55)
                label = Label(windowbowlerteam1, width=15, text="OVER", font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=440, y=55)
                y1 = 100
                mycursor.execute("SELECT * from initialinfo")
                myresult = mycursor.fetchall()
                initialdetails = myresult[-1]
                index = 27

                # Bowler 1
                index -= 2
                labelteam1bowler1 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler1.place(x=0, y=y1)

                labelteam1wicketsbowler1 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler1.place(x=150, y=y1)

                labelteam1runsbowler1 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler1.place(x=300, y=y1)

                labelteam1overbowler1 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler1.place(x=440, y=y1)

                # Bowler 2
                y1 += 30
                index -= 2
                labelteam1bowler2 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler2.place(x=0, y=y1)

                labelteam1wicketsbowler2 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler2.place(x=150, y=y1)

                labelteam1runsbowler2 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler2.place(x=300, y=y1)

                labelteam1overbowler2 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler2.place(x=440, y=y1)

                # Bowler 3
                y1 += 30
                index -= 2
                labelteam1bowler3 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler3.place(x=0, y=y1)

                labelteam1wicketsbowler3 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler3.place(x=150, y=y1)

                labelteam1runsbowler3 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler3.place(x=300, y=y1)

                labelteam1overbowler3 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler3.place(x=440, y=y1)

                # Bowler 4
                y1 += 30
                index -= 2
                labelteam1bowler4 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler4.place(x=0, y=y1)

                labelteam1wicketsbowler4 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler4.place(x=150, y=y1)

                labelteam1runsbowler4 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler4.place(x=300, y=y1)

                labelteam1overbowler4 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler4.place(x=440, y=y1)

                # Bowler 5
                y1 += 30
                index -= 2
                labelteam1bowler5 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler5.place(x=0, y=y1)

                labelteam1wicketsbowler5 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler5.place(x=150, y=y1)

                labelteam1runsbowler5 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler5.place(x=300, y=y1)

                labelteam1overbowler5 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler5.place(x=440, y=y1)

                # Bowler 6
                y1 += 30
                index -= 2
                labelteam1bowler6 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler6.place(x=0, y=y1)

                labelteam1wicketsbowler6 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler6.place(x=150, y=y1)

                labelteam1runsbowler6 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler6.place(x=300, y=y1)

                labelteam1overbowler6 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler6.place(x=440, y=y1)

                # Bowler 7
                y1 += 30
                index -= 2
                labelteam1bowler7 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler7.place(x=0, y=y1)

                labelteam1wicketsbowler7 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler7.place(x=150, y=y1)

                labelteam1runsbowler7 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler7.place(x=300, y=y1)

                labelteam1overbowler7 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler7.place(x=440, y=y1)

                # Bowler 8
                y1 += 30
                index -= 2
                labelteam1bowler8 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler8.place(x=0, y=y1)

                labelteam1wicketsbowler8 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler8.place(x=150, y=y1)

                labelteam1runsbowler8 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler8.place(x=300, y=y1)

                labelteam1overbowler8 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler8.place(x=440, y=y1)

                # Bowler 9
                y1 += 30
                index -= 2
                labelteam1bowler9 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler9.place(x=0, y=y1)

                labelteam1wicketsbowler9 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler9.place(x=150, y=y1)

                labelteam1runsbowler9 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler9.place(x=300, y=y1)

                labelteam1overbowler9 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler9.place(x=440, y=y1)

                # Bowler 10
                y1 += 30
                index -= 2
                labelteam1bowler10 = Label(windowbowlerteam1, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1bowler10.place(x=0, y=y1)

                labelteam1wicketsbowler10 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketsbowler10.place(x=150, y=y1)

                labelteam1runsbowler10 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbowler10.place(x=300, y=y1)

                labelteam1overbowler10 = Label(windowbowlerteam1,  width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam1overbowler10.place(x=440, y=y1)



                # Repeat similar changes for the rest of the bowlers (Bowler 3, Bowler 4, Bowler 5).

                x1 = 0
                y1 += 45

                label = Label(windowbowlerteam1, width=5, text="1", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="2", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="3", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="4", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="5", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="6", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="7", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="8", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="9", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam1, width=5, text="10", font=("Arial", 10), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                # Moving to the next row
                x1 = 0
                y1 += 30

                # Team 2 wickets (empty labels)
                team2wicket1bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket1bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket2bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket2bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket3bowl= Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket3bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket4bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket4bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket5bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket5bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket6bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket6bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket7bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket7bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket8bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket8bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket9bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket9bowl.place(x=x1, y=y1)
                x1 += 58

                team2wicket10bowl = Label(windowbowlerteam1, width=5, text="", font=("Arial", 10), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team2wicket10bowl.place(x=x1, y=y1)
                x1 += 58
                p = 1
                query = ("SELECT * from extrateam2 where matchno=%s")  # Changed `extrateam2` to `extrateam1`
                mycursor.execute(query, (p,))
                myresult = mycursor.fetchall()

                # Calculating extras for team2
                l = myresult
                n = 0
                for i in l:
                    n += i[1]


                y1+=5
                labelrunteam2bowlwin = Label(windowbowlerteam1, width=20, text=team1score, font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labelrunteam2bowlwin.place(x=0, y=y1+40)

                labeloverteam2bowlwin = Label(windowbowlerteam1, width=20, text="OVER  " + over, font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labeloverteam2bowlwin.place(x=200, y=y1+40)

                labelextrasteam2bowlwin = Label(windowbowlerteam1, width=20, text="EXTRAS  " + str(n), font=("Arial", 10, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labelextrasteam2bowlwin.place(x=400, y=y1+40)
                p=naa()

                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    #print(i[8])
                    if i[8] not in namelist:
                        display.append(i)
                        namelist.append(i[8])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]

                p=naa()
                query=("SELECT * from extrateam2 where matchno=%s")
                mycursor.execute(query,(p,))

                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    ##print(i)
                    n+=i[1]
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]

                labelrunteam2bowlwin.config(text=showdown[6])
                labeloverteam2bowlwin.config(text=showdown[7])
                labelextrasteam2bowlwin.config(text="EXTRAS  "+str(n))

            
                for show in display:                    
                    if show[8] == shirtno[26]:                        
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler1.config(text=displaystats[0])
                        labelteam1runsbowler1.config(text=displaystats[1])
                        labelteam1overbowler1.config(text=displaystats[2])

                    elif show[8] == shirtno[24]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler2.config(text=displaystats[0])
                        labelteam1runsbowler2.config(text=displaystats[1])
                        labelteam1overbowler2.config(text=displaystats[2])

                    elif show[8] == shirtno[22]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler3.config(text=displaystats[0])
                        labelteam1runsbowler3.config(text=displaystats[1])
                        labelteam1overbowler3.config(text=displaystats[2])

                    elif show[8] == shirtno[20]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler4.config(text=displaystats[0])
                        labelteam1runsbowler4.config(text=displaystats[1])
                        labelteam1overbowler4.config(text=displaystats[2])

                    elif show[8] == shirtno[18]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler5.config(text=displaystats[0])
                        labelteam1runsbowler5.config(text=displaystats[1])
                        labelteam1overbowler5.config(text=displaystats[2])

                    elif show[8] == shirtno[16]:
                        displaystats = show[9].split("/")               
                        labelteam1wicketsbowler6.config(text=displaystats[0])
                        labelteam1runsbowler6.config(text=displaystats[1])
                        labelteam1overbowler6.config(text=displaystats[2])

                    elif show[8] == shirtno[14]:
                        displaystats = show[9].split("/")                        
                        labelteam1wicketsbowler7.config(text=displaystats[0])
                        labelteam1runsbowler7.config(text=displaystats[1])
                        labelteam1overbowler7.config(text=displaystats[2])

                    elif show[8] == shirtno[12]:
                        displaystats = show[9].split("/")                        
                        labelteam1wicketsbowler8.config(text=displaystats[0])
                        labelteam1runsbowler8.config(text=displaystats[1])
                        labelteam1overbowler8.config(text=displaystats[2])

                    elif show[8] == shirtno[10]:
                        displaystats = show[9].split("/")
                        labelteam1wicketsbowler9.config(text=displaystats[0])
                        labelteam1runsbowler9.config(text=displaystats[1])
                        labelteam1overbowler9.config(text=displaystats[2])
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    #print(i[8],"8888")
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])                        
                count=0
                for wicket in display:                    
                    if count==0:
                        if wicket[10]=="WICKET":                            
                            run=wicket[6].split("/")
                            team2wicket1bowl.config(text=run[0])
                            count+=1
                    elif count==1:
                        if wicket[10]=="WICKET":                            
                            run=wicket[6].split("/")
                            team2wicket2bowl.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":                            
                            run=wicket[6].split("/")
                            team2wicket3bowl.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket4bowl.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket5bowl.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket6bowl.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket7bowl.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket8bowl.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket9bowl.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team2wicket10bowl.config(text=run[0])
                            count+=1
        
        except Exception as e:
            windowbowlerteam1  = None
            # Loop for Team 1 Bowlers (bowler1 to bowler8)
            for i in range(1, 9):  # Loop from 1 to 8
    
                globals()[f"labelteam1wicketsbowler{i}"] = None
                globals()[f"labelteam1runsbowler{i}"] = None
                globals()[f"labelteam1overbowler{i}"] = None

            # Loop for Team 2 Wickets (wicket1 to wicket10)
            for i in range(1, 11):  # Loop from 1 to 10
                    globals()[f"team2wicket{i}bowl"] = None

    elif team2==p[27]:
        try:
            if windowbowlerteam2 is not None:
                p=naa()

                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    #print(i[8],"888")
                    if i[8] not in namelist:
                        display.append(i)
                        namelist.append(i[8])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]

                p=naa()
                query=("SELECT * from extrasteam1 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    n+=i[1]

                p=naa()

                query=("SELECT * from scoreboard1 where matchno=%s")
                mycursor.execute(query,(p,))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]
                labelrunteam1bowlwin.config(text=showdown[6])
                labeloverteam1bowlwin.config(text=showdown[7])
                query=("SELECT SUM(team1extras) AS total_sum FROM extrasteam1 where matchno=%s");
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                labelextrasteam1bowlwin.config(text="EXTRAS  "+str(myresult[-1][0]))                
                for show in display:                    
                    if show[8] == shirtno[49]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler1.config(text=displaystats[0])
                        labelteam2runsbowler1.config(text=displaystats[1])
                        labelteam2overbowler1.config(text=displaystats[2])

                    elif show[8] == shirtno[47]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler2.config(text=displaystats[0])
                        labelteam2runsbowler2.config(text=displaystats[1])
                        labelteam2overbowler2.config(text=displaystats[2])

                    elif show[8] == shirtno[45]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler3.config(text=displaystats[0])
                        labelteam2runsbowler3.config(text=displaystats[1])
                        labelteam2overbowler3.config(text=displaystats[2])

                    elif show[8] == shirtno[43]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler4.config(text=displaystats[0])
                        labelteam2runsbowler4.config(text=displaystats[1])
                        labelteam2overbowler4.config(text=displaystats[2])

                    elif show[8] == shirtno[41]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler5.config(text=displaystats[0])
                        labelteam2runsbowler5.config(text=displaystats[1])
                        labelteam2overbowler5.config(text=displaystats[2])

                    elif show[8] == shirtno[39]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler6.config(text=displaystats[0])
                        labelteam2runsbowler6.config(text=displaystats[1])
                        labelteam2overbowler6.config(text=displaystats[2])

                    elif show[8] == shirtno[37]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler7.config(text=displaystats[0])
                        labelteam2runsbowler7.config(text=displaystats[1])
                        labelteam2overbowler7.config(text=displaystats[2])

                    elif show[8] == shirtno[35]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler8.config(text=displaystats[0])
                        labelteam2runsbowler8.config(text=displaystats[1])
                        labelteam2overbowler8.config(text=displaystats[2])

                    elif show[8] == shirtno[33]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler9.config(text=displaystats[0])
                        labelteam2runsbowler9.config(text=displaystats[1])
                        labelteam2overbowler9.config(text=displaystats[2])
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:              
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                count=0
                for wicket in display:
                    if count==0:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket1bowl.config(text=run[0])
                            count+=1
                    elif count==1:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket2bowl.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket3bowl.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket4bowl.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket5bowl.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket6bowl.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket7bowl.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket8bowl.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket9bowl.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket10bowl.config(text=run[0])
                            count+=1
            else:
                windowbowlerteam2 = Tk()                
                windowbowlerteam2.geometry("750x630")
                windowbowlerteam2.title("BOWLERS STATS")
                windowbowlerteam2.config(background="lavender", padx=80, pady=2, border=20)
                label = Label(windowbowlerteam2, width=46,text=team2, font=("Arial", 15, "bold"), bg="dodgerblue", fg="white", relief=RIDGE, bd=10)
                label.place(x=0, y=0)
                label = Label(windowbowlerteam2, width=13, text="BOWLER", font=("Arial", 13,"bold"), bg="darkblue", fg="white", relief=RIDGE, bd=10)
                label.place(x=0, y=50)
                label = Label(windowbowlerteam2, width=13, text="WICKETS", font=("Arial", 13,"bold"), bg="darkblue", fg="white", relief=RIDGE, bd=10)
                label.place(x=150, y=50)
                label = Label(windowbowlerteam2, width=13, text="RUNS", font=("Arial", 13,"bold"), bg="darkblue", fg="white", relief=RIDGE, bd=10)
                label.place(x=300, y=50)
                label = Label(windowbowlerteam2, width=12, text="OVER", font=("Arial", 13,"bold"), bg="darkblue", fg="white", relief=RIDGE, bd=10)
                label.place(x=440, y=50)
                y1=95
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                initialdetails=myresult[-1]
                # Initial y position and index
                index = 48
                # Bowler 1
                labelteam2bowler1 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler1.place(x=0, y=y1)

                labelteam2wicketsbowler1 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler1.place(x=150, y=y1)

                labelteam2runsbowler1 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler1.place(x=300, y=y1)

                labelteam2overbowler1 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler1.place(x=440, y=y1)

                # For subsequent bowlers, increment `y1` and update the index as before
                y1 += 30
                index -= 2

                labelteam2bowler2 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler2.place(x=0, y=y1)

                labelteam2wicketsbowler2 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler2.place(x=150, y=y1)

                labelteam2runsbowler2 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler2.place(x=300, y=y1)

                labelteam2overbowler2 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler2.place(x=440, y=y1)

                # For bowler 3
                y1 += 30
                index -= 2

                labelteam2bowler3 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler3.place(x=0, y=y1)

                labelteam2wicketsbowler3 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler3.place(x=150, y=y1)

                labelteam2runsbowler3 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler3.place(x=300, y=y1)

                labelteam2overbowler3 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler3.place(x=440, y=y1)

                # For bowler 4
                y1 += 30
                index -= 2

                labelteam2bowler4 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler4.place(x=0, y=y1)

                labelteam2wicketsbowler4 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler4.place(x=150, y=y1)

                labelteam2runsbowler4 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler4.place(x=300, y=y1)

                labelteam2overbowler4 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler4.place(x=440, y=y1)

                # For bowler 5
                y1 += 30
                index -= 2

                labelteam2bowler5 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler5.place(x=0, y=y1)

                labelteam2wicketsbowler5 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler5.place(x=150, y=y1)

                labelteam2runsbowler5 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler5.place(x=300, y=y1)

                labelteam2overbowler5 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler5.place(x=440, y=y1)

                # Continue for any additional bowlers as necessary

                # For bowler 6
                y1 += 30
                index -= 2

                labelteam2bowler6 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler6.place(x=0, y=y1)

                labelteam2wicketsbowler6 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler6.place(x=150, y=y1)

                labelteam2runsbowler6 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler6.place(x=300, y=y1)

                labelteam2overbowler6 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler6.place(x=440, y=y1)

                # For bowler 7
                y1 += 30
                index -= 2

                labelteam2bowler7 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler7.place(x=0, y=y1)

                labelteam2wicketsbowler7 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler7.place(x=150, y=y1)

                labelteam2runsbowler7 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler7.place(x=300, y=y1)

                labelteam2overbowler7 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler7.place(x=440, y=y1)

                # For bowler 8
                y1 += 30
                index -= 2

                labelteam2bowler8 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler8.place(x=0, y=y1)

                labelteam2wicketsbowler8 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler8.place(x=150, y=y1)

                labelteam2runsbowler8 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler8.place(x=300, y=y1)

                labelteam2overbowler8 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler8.place(x=440, y=y1)

                # For bowler 9
                y1 += 30
                index -= 2

                labelteam2bowler9 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler9.place(x=0, y=y1)

                labelteam2wicketsbowler9 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler9.place(x=150, y=y1)

                labelteam2runsbowler9 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler9.place(x=300, y=y1)

                labelteam2overbowler9 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler9.place(x=440, y=y1)

                # For bowler 10
                y1 += 30
                index -= 2

                labelteam2bowler10 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler10.place(x=0, y=y1)

                labelteam2wicketsbowler10 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler10.place(x=150, y=y1)

                labelteam2runsbowler10 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler10.place(x=300, y=y1)

                labelteam2overbowler10 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler10.place(x=440, y=y1)


                # For bowler 11
                y1 += 27
                index -= 2

                labelteam2bowler11 = Label(windowbowlerteam2, width=15, text=initialdetails[index], font=("Arial", 10, "bold"), bg="blue", fg="white",relief=RIDGE, bd=10)
                labelteam2bowler11.place(x=0, y=y1)

                labelteam2wicketsbowler11 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2wicketsbowler11.place(x=150, y=y1)

                labelteam2runsbowler11 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="red", fg="white", relief=RIDGE, bd=10)
                labelteam2runsbowler11.place(x=300, y=y1)

                labelteam2overbowler11 = Label(windowbowlerteam2, width=15, text="  ", font=("Arial", 10), bg="green", fg="white", relief=RIDGE, bd=10)
                labelteam2overbowler11.place(x=440, y=y1)
                x1 = 0
                y1 += 45



                label = Label(windowbowlerteam2, width=5, text="1", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="2", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="3", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="4", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="5", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="6", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="7", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="8", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="9", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                label = Label(windowbowlerteam2, width=5, text="10", font=("Arial", 12), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 58

                # Moving to the next row
                x1 = 0
                y1 += 34

                # Team 1 wickets (empty labels)
                team1wicket1bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket1bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket2bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket2bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket3bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket3bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket4bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket4bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket5bowl= Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket5bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket6bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket6bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket7bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket7bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket8bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket8bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket9bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket9bowl.place(x=x1, y=y1)
                x1 += 58

                team1wicket10bowl = Label(windowbowlerteam2, width=5, text="", font=("Arial", 12), bg="darkgray", fg="white", relief=RIDGE, bd=10)
                team1wicket10bowl.place(x=x1, y=y1)
                x1 += 58
                y1+=35
                p=naa()

                query=("SELECT * from extrateam2 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:                    
                    n+=i[1]

                labelrunteam1bowlwin = Label(windowbowlerteam2, width=15, text=team1score, font=("Arial", 13, "bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labelrunteam1bowlwin.place(x=0, y=y1+10)

                labeloverteam1bowlwin = Label(windowbowlerteam2, width=15, text="OVER  "+over, font=("Arial", 13,"bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labeloverteam1bowlwin.place(x=200, y=y1+10)

                labelextrasteam1bowlwin = Label(windowbowlerteam2, width=15, text="EXTRAS  "+str(n), font=("Arial", 13,"bold"), bg="darkgreen", fg="white", relief=RIDGE, bd=10)
                labelextrasteam1bowlwin.place(x=400, y=y1+10)
                
                p=naa()
                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    if i[8] not in namelist:
                        display.append(i)
                        namelist.append(i[8])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]
                p=naa()
                query=("SELECT * from extrasteam1 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    n+=i[1]
                query=("SELECT * from scoreboard1 where matchno=%s")
                mycursor.execute(query,(p,))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]
                labelrunteam1bowlwin.config(text=showdown[6])
                labeloverteam1bowlwin.config(text=showdown[7])
                query=("SELECT SUM(team1extras) AS total_sum FROM extrasteam1 where matchno=%s");
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                labelextrasteam1bowlwin.config(text="EXTRAS  "+str(n))                    
                for show in display:                    
                    if show[8] == shirtno[49]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler1.config(text=displaystats[0])
                        labelteam2runsbowler1.config(text=displaystats[1])
                        labelteam2overbowler1.config(text=displaystats[2])

                    elif show[8] == shirtno[47]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler2.config(text=displaystats[0])
                        labelteam2runsbowler2.config(text=displaystats[1])
                        labelteam2overbowler2.config(text=displaystats[2])

                    elif show[8] == shirtno[45]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler3.config(text=displaystats[0])
                        labelteam2runsbowler3.config(text=displaystats[1])
                        labelteam2overbowler3.config(text=displaystats[2])

                    elif show[8] == shirtno[43]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler4.config(text=displaystats[0])
                        labelteam2runsbowler4.config(text=displaystats[1])
                        labelteam2overbowler4.config(text=displaystats[2])

                    elif show[8] == shirtno[41]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler5.config(text=displaystats[0])
                        labelteam2runsbowler5.config(text=displaystats[1])
                        labelteam2overbowler5.config(text=displaystats[2])

                    elif show[8] == shirtno[39]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler6.config(text=displaystats[0])
                        labelteam2runsbowler6.config(text=displaystats[1])
                        labelteam2overbowler6.config(text=displaystats[2])

                    elif show[8] == shirtno[37]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler7.config(text=displaystats[0])
                        labelteam2runsbowler7.config(text=displaystats[1])
                        labelteam2overbowler7.config(text=displaystats[2])

                    elif show[8] == shirtno[35]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler8.config(text=displaystats[0])
                        labelteam2runsbowler8.config(text=displaystats[1])
                        labelteam2overbowler8.config(text=displaystats[2])

                    elif show[8] == shirtno[33]:
                        displaystats = show[9].split("/")
                        labelteam2wicketsbowler9.config(text=displaystats[0])
                        labelteam2runsbowler9.config(text=displaystats[1])
                        labelteam2overbowler9.config(text=displaystats[2])
                
                p=naa()

                query=("SELECT * from scoreboard1 where matchno=%s and team2=%s")
                mycursor.execute(query,(p,team2))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    #print(i[8],"8888")
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                                        
                count=0
                for wicket in display:
                    if count==0:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket1bowl.config(text=run[0])
                            count+=1
                            print("execute1123")
                    elif count==1:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket2bowl.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket3bowl.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket4bowl.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket5bowl.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket6bowl.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket7bowl.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket8bowl.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":           
                            run=wicket[6].split("/")
                            team1wicket9bowl.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket10bowl.config(text=run[0])
                            count+=1
                    
    
            
                        
        except Exception as e:
        
            # Loop for Team 1 Bowlers (bowler1 to bowler8)
            for i in range(1, 9):  # Loop from 1 to 8
    
                globals()[f"labelteam2wicketsbowler{i}"] = None
                globals()[f"labelteam2runsbowler{i}"] = None
                globals()[f"labelteam2overbowler{i}"] = None

            # Loop for Team 2 Wickets (wicket1 to wicket10)
            for i in range(1, 11):  # Loop from 1 to 10
                    globals()[f"team1wicket{i}bowl"] = None
            windowbowlerteam2=None
            detailsbowler(team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)
            print("error",e)
        
def detailsbatter(team1,team2,strikervalue,strikerscorevalue,nonstrikervalue,nonstrikerscorevalue,
                  team1scoreteam2value,
                  overvalue):

    (team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)=(team1,team2,strikervalue,strikerscorevalue,nonstrikervalue,nonstrikerscorevalue,
                  team1scoreteam2value,
                  overvalue)
    team1=team1.get()
    team2=team2.get()
    striker,strikerscore,nonstriker,nonstrikerscore=strikervalue.get(),strikerscorevalue.get(),nonstrikervalue.get(),nonstrikerscorevalue.get()   
    team1score=team1scoreteam2value.get()
    over=overvalue.get()    
    mycursor.execute("SELECT * from initialinfo")
    myresult=mycursor.fetchall()
    p=myresult[-1]    
    if team1==p[4]:       
        global windowbatterteam1
        global labelrunteam1batwin,labeloverteam1batwin,labelextrasteam1batwin        
        global labelteam1runsbatter1
        global labelteam1runsbatter2
        global labelteam1runsbatter3
        global labelteam1runsbatter4
        global labelteam1runsbatter5
        global labelteam1runsbatter6
        global labelteam1runsbatter7
        global labelteam1runsbatter8
        global labelteam1runsbatter9
        global labelteam1runsbatter10
        global labelteam1runsbatter11
        global labelteam1wicketbatter1
        global labelteam1wicketbatter2
        global labelteam1wicketbatter3
        global labelteam1wicketbatter4
        global labelteam1wicketbatter5
        global labelteam1wicketbatter6
        global labelteam1wicketbatter7
        global labelteam1wicketbatter8
        global labelteam1wicketbatter9
        global labelteam1wicketbatter10
        global labelteam1wicketbatter11
        global team1wicket1_bat, team1wicket2_bat, team1wicket3_bat, team1wicket4_bat, team1wicket5_bat
        global team1wicket6_bat, team1wicket7_bat, team1wicket8_bat, team1wicket9_bat, team1wicket10_bat
        p=naa()
        #got latest match no
        query=("SELECT * from team1wickets where matchno=%s")
        mycursor.execute(query,(p,))
        myresult=mycursor.fetchall()        
        k=myresult
        try:
            if windowbatterteam1 is not None:
                query=("SELECT * from scoreboard1 where matchno=%s")
                mycursor.execute(query,(p,))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                p=naa()
                query=("SELECT * from extrasteam1 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()

                #mycursor.execute("SELECT * from extrasteam2 where matchno=k")
                #myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    ##print(i)
                    n+=i[1]
                query=("SELECT * from scoreboard1 where matchno=%s")
                mycursor.execute(query,(p,))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]
                labelrunteam1batwin.config(text=showdown[6])
                labeloverteam1batwin.config(text=showdown[7])
                query=("SELECT SUM(team1extras) AS total_sum FROM extrasteam1 where matchno=%s");
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                labelextrasteam1batwin.config(text="EXTRAS  "+str(n))

                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]

                for show in display:                            
                    if show[1] == shirtno[6]:  # Increment 18
                        labelteam1runsbatter1.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter1.config(text=bowler)
                            
                    elif show[1] == shirtno[8]:  # Increment 18
                        labelteam1runsbatter2.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter2.config(text=bowler)
                            
                    elif show[1] == shirtno[10]:  # Increment 18
                        labelteam1runsbatter3.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter3.config(text=bowler)
                                
                    elif show[1] == shirtno[12]:  # Increment 18
                        labelteam1runsbatter4.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter4.config(text=bowler)
                            
                    elif show[1] == shirtno[14]:  # Increment 18
                        labelteam1runsbatter5.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter5.config(text=bowler)
                            
                    elif show[1] == shirtno[16]:  # Increment 18
                        labelteam1runsbatter6.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter6.config(text=bowler)
                            
                    elif show[1] == shirtno[18]:  # Increment 18
                        labelteam1runsbatter7.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter7.config(text=bowler)
                            
                    elif show[1] == shirtno[20]:  # Increment 18
                        labelteam1runsbatter8.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter8.config(text=bowler)
                            
                    elif show[1] == shirtno[22]:  # Increment 18
                        labelteam1runsbatter9.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter9.config(text=bowler)
                            
                    elif show[1] == shirtno[24]:  # Increment 18
                        labelteam1runsbatter10.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter10.config(text=bowler)
                            
                    elif show[1] == shirtno[26]:  # Increment 20
                        labelteam1runsbatter11.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter11.config(text=bowler)
                
                count=0
                for wicket in display:                    
                    if count==0:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket1_bat.config(text=run[0])                    
                            count+=1
                    elif count==1:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket2_bat.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket3_bat.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket4_bat.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket5_bat.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket6_bat.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket7.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket8_bat.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket9_bat.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket10_bat.config(text=run[0])
                
            else:
                
                windowbatterteam1 = Tk()
                windowbatterteam1.geometry("700x630")
                windowbatterteam1.title("BATTERS STATS")
                windowbatterteam1.config(background="LIGHTBLUE", padx=60, pady=10, border=20)  # Dark blue background

                label=Label(windowbatterteam1,width=38,text=team1,font=("Arial",16,"bold"),bg="DARKGREEN",fg="white",relief=RIDGE,bd=10)
                label.place(x=0,y=0)
                label=Label(windowbatterteam1,width=16,text="BATTER",font=("Arial",13,"bold"),bg="LIGHTGREEN",fg="BLACK",relief=RIDGE,bd=10)
                label.place(x=0,y=50)
                label=Label(windowbatterteam1,width=14,text="RUNS(BOWLS)",font=("Arial",13,"bold"),bg="LIGHTGREEN",fg="BLACK",relief=RIDGE,bd=10)
                label.place(x=184,y=50)
                label=Label(windowbatterteam1,width=15,text="WICKET BY",font=("Arial",13,"bold"),bg="LIGHTGREEN",fg="BLACK",relief=RIDGE,bd=10)
                label.place(x=345,y=50)
                y1=90
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                initialdetails=myresult[-1]
                # Initial y position and index

                index = 5

                # Batter 1
                labelteam1batter1 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter1.place(x=0, y=y1)

                labelteam1runsbatter1 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter1.place(x=184, y=y1)

                labelteam1wicketbatter1 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter1.place(x=350, y=y1)

                # Batter 2
                y1 += 32
                index += 2

                labelteam1batter2 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter2.place(x=0, y=y1)

                labelteam1runsbatter2 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter2.place(x=184, y=y1)

                labelteam1wicketbatter2 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter2.place(x=350, y=y1)

                # Batter 3
                y1 += 32
                index += 2

                labelteam1batter3 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter3.place(x=0, y=y1)

                labelteam1runsbatter3 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter3.place(x=184, y=y1)

                labelteam1wicketbatter3 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter3.place(x=350, y=y1)

                # Batter 4
                y1 += 32
                index += 2

                labelteam1batter4 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter4.place(x=0, y=y1)

                labelteam1runsbatter4 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter4.place(x=184, y=y1)

                labelteam1wicketbatter4 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter4.place(x=350, y=y1)

                # Batter 5
                y1 += 32
                index += 2

                labelteam1batter5 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter5.place(x=0, y=y1)

                labelteam1runsbatter5 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter5.place(x=184, y=y1)

                labelteam1wicketbatter5 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter5.place(x=350, y=y1)

                # Batter 6
                y1 += 32
                index += 2

                labelteam1batter6 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter6.place(x=0, y=y1)

                labelteam1runsbatter6 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter6.place(x=184, y=y1)

                labelteam1wicketbatter6 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter6.place(x=350, y=y1)

                # Batter 7
                y1 += 32
                index += 2

                labelteam1batter7 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter7.place(x=0, y=y1)

                labelteam1runsbatter7 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter7.place(x=184, y=y1)

                labelteam1wicketbatter7 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter7.place(x=350, y=y1)

                # Batter 8
                y1 += 32
                index += 2

                labelteam1batter8 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter8.place(x=0, y=y1)

                labelteam1runsbatter8 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter8.place(x=184, y=y1)

                labelteam1wicketbatter8 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter8.place(x=350, y=y1)

                # Batter 9
                y1 += 32
                index += 2

                labelteam1batter9 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter9.place(x=0, y=y1)

                labelteam1runsbatter9 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter9.place(x=184, y=y1)

                labelteam1wicketbatter9 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter9.place(x=350, y=y1)

                # Batter 10
                y1 += 32
                index += 2

                labelteam1batter10 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter10.place(x=0, y=y1)

                labelteam1runsbatter10 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter10.place(x=184, y=y1)

                labelteam1wicketbatter10 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter10.place(x=350, y=y1)

                # Batter 11
                y1 += 32
                index += 2

                labelteam1batter11 = Label(windowbatterteam1, width=16, text=initialdetails[index], font=("Arial", 13,"bold"),bg="LIGHTYELLOW", fg="BLACK", relief=RIDGE, bd=10)
                labelteam1batter11.place(x=0, y=y1)

                labelteam1runsbatter11 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1runsbatter11.place(x=184, y=y1)

                labelteam1wicketbatter11 = Label(windowbatterteam1, width=16, text="  ", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
                labelteam1wicketbatter11.place(x=350, y=y1)
                x1=0
                y1+=50

                label = Label(windowbatterteam1, width=4, text="1", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="2", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="3", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="4", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="5", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="6", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="7", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="8", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="9", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50

                label = Label(windowbatterteam1, width=4, text="10", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                label.place(x=x1, y=y1)
                x1 += 50



                x1 = 0
                y1 += 30

                team1wicket1_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket1_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket2_bat  = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket2_bat .place(x=x1, y=y1)
                x1 += 50

                team1wicket3_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket3_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket4_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket4_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket5_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket5_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket6_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket6_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket7_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket7_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket8_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket8_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket9_bat = Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket9_bat.place(x=x1, y=y1)
                x1 += 50

                team1wicket10_bat= Label(windowbatterteam1, width=4, text="", font=("Arial", 12, "bold"), bg="#6A5ACD", fg="white", relief=RIDGE, bd=10)
                team1wicket10_bat.place(x=x1, y=y1)
                x1 += 50
                p=naa()
                #latest match no

                query=("SELECT SUM(team1extras) AS total_sum FROM extrasteam1 where matchno=%s");
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                y1+=43
                labelrunteam1batwin=Label(windowbatterteam1,width=16,text=team1score,font=("Arial",13,"bold"),bg="DARKGREEN",fg="WHITE",relief=RIDGE,bd=10)
                labelrunteam1batwin.place(x=0,y=y1)

                labeloverteam1batwin=Label(windowbatterteam1,width=16,text="OVER  "+over,font=("Arial",13,"bold"),bg="#0E2B4E",fg="WHITE",relief=RIDGE,bd=10)
                labeloverteam1batwin.place(x=180,y=y1)

                labelextrasteam1batwin=Label(windowbatterteam1,width=16,text="EXTRAS  "+str(myresult),font=("Arial",13,"bold"),bg="#0E2B4E",fg="WHITE",relief=RIDGE,bd=10)
                labelextrasteam1batwin.place(x=330,y=y1)
                #config
                query=("SELECT * from scoreboard1 where matchno=%s and team1=%s")
                mycursor.execute(query,(p,team1))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]
                p=naa()
                query=("SELECT * from extrasteam1 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    n+=i[1]
                query=("SELECT * from scoreboard1 where matchno=%s")
                mycursor.execute(query,(p,))
                showdown=mycursor.fetchall()
                showdown=showdown[-1]
                labelrunteam1batwin.config(text=team1score)
                labeloverteam1batwin.config(text=over)
                query=("SELECT SUM(team1extras) AS total_sum FROM extrasteam1 where matchno=%s");
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                labelextrasteam1batwin.config(text="EXTRAS  "+str(n))

                for show in display:
                    if show[1] == shirtno[6]:  # Increment 18
                        labelteam1runsbatter1.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter1.config(text=bowler)
                            
                    elif show[1] == shirtno[8]:  # Increment 18
                        labelteam1runsbatter2.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter2.config(text=bowler)
                            
                    elif show[1] == shirtno[10]:  # Increment 18
                        labelteam1runsbatter3.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter3.config(text=bowler)
                            
                            
                    elif show[1] == shirtno[12]:  # Increment 18
                        labelteam1runsbatter4.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter4.config(text=bowler)
                            
                    elif show[1] == shirtno[14]:  # Increment 18
                        labelteam1runsbatter5.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter5.config(text=bowler)
                            
                    elif show[1] == shirtno[16]:  # Increment 18
                        labelteam1runsbatter6.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter6.config(text=bowler)
                            
                    elif show[1] == shirtno[18]:  # Increment 18
                        labelteam1runsbatter7.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter7.config(text=bowler)
                            
                    elif show[1] == shirtno[20]:  # Increment 18
                        labelteam1runsbatter8.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter8.config(text=bowler)
                            
                    elif show[1] == shirtno[22]:  # Increment 18
                        labelteam1runsbatter9.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter9.config(text=bowler)
                            
                    elif show[1] == shirtno[24]:  # Increment 18
                        labelteam1runsbatter10.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter10.config(text=bowler)
                            
                    elif show[1] == shirtno[26]:  # Increment 20
                        labelteam1runsbatter11.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam1wicketbatter11.config(text=bowler)
                count=0
                for wicket in display:     
                    if count==0:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket1_bat.config(text=run[0])
                            
                            count+=1
                    elif count==1:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket2_bat.config(text=run[0])
                            count+=1
                    elif count==2:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket3_bat.config(text=run[0])
                            count+=1
                    elif count==3:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket4_bat.config(text=run[0])
                            count+=1
                    elif count==4:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket5_bat.config(text=run[0])
                            count+=1
                    elif count==5:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket6_bat.config(text=run[0])
                            count+=1
                    elif count==6:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket7.config(text=run[0])
                            count+=1
                    elif count==7:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket8_bat.config(text=run[0])
                            count+=1
                    elif count==8:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket9_bat.config(text=run[0])
                            count+=1
                    elif count==9:
                        if wicket[10]=="WICKET":
                            run=wicket[6].split("/")
                            team1wicket10_bat.config(text=run[0])
        except Exception as e:
            # Create a list of all the labels
            labels = [
                labelteam1runsbatter1, labelteam1wicketbatter1,
                labelteam1runsbatter2, labelteam1wicketbatter2,
                labelteam1runsbatter3, labelteam1wicketbatter3,
                labelteam1runsbatter4, labelteam1wicketbatter4,
                labelteam1runsbatter5, labelteam1wicketbatter5,
                labelteam1runsbatter6, labelteam1wicketbatter6,
                labelteam1runsbatter7, labelteam1wicketbatter7,
                labelteam1runsbatter8, labelteam1wicketbatter8,
                labelteam1runsbatter9, labelteam1wicketbatter9,
                labelteam1runsbatter10, labelteam1wicketbatter10,
                labelteam1runsbatter11, labelteam1wicketbatter11,
                team1wicket1_bat, team1wicket2_bat, team1wicket3_bat, team1wicket4_bat,
                team1wicket5_bat, team1wicket6_bat, team1wicket7_bat, team1wicket8_bat,
                team1wicket9_bat, team1wicket10_bat,
                labelrunteam1batwin, labeloverteam1batwin, labelextrasteam1batwin
            ]

            # Loop through the list and set each label to None
            for lbl in labels:
                lbl = None
            windowbatterteam1=None
            detailsbatter(team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)
                        
    elif team1==p[27]: #team means batting
        global windowbatterteam2

        global labelrunteam2batwin,labeloverteam2batwin,labelextrasteam2batwin
        global labelteam2runsbatter1
        global labelteam2runsbatter2
        global labelteam2runsbatter3
        global labelteam2runsbatter4
        global labelteam2runsbatter5
        global labelteam2runsbatter6
        global labelteam2runsbatter7
        global labelteam2runsbatter8
        global labelteam2runsbatter9
        global labelteam2runsbatter10
        global labelteam2runsbatter11
        global labelteam2wicketbatter1
        global labelteam2wicketbatter2
        global labelteam2wicketbatter3
        global labelteam2wicketbatter4
        global labelteam2wicketbatter5
        global labelteam2wicketbatter6
        global labelteam2wicketbatter7
        global labelteam2wicketbatter8
        global labelteam2wicketbatter9
        global labelteam2wicketbatter10
        global labelteam2wicketbatter11
        global team2wicket1_bat, team2wicket2_bat, team2wicket3_bat, team2wicket4_bat, team2wicket5_bat
        global team2wicket6_bat, team2wicket7_bat, team2wicket8_bat, team2wicket9_bat, team2wicket10_bat
        p=naa()
        #got latest match no
        query=("SELECT * from team2wickets where matchno=%s")
        mycursor.execute(query,(p,))
        myresult=mycursor.fetchall()        
        k=myresult
        try:
            if windowbatterteam2 is not None:
                query=("SELECT * from scoreboard1 where matchno=%s and team1=%s")
                mycursor.execute(query,(p,team1))
                scores=mycursor.fetchall()
                templist=list()
                namelist=list()
                display=list()
                #revresing for latest
                for i in scores:
                    templist.insert(0,i)
                #only once the name in list    
                for i in templist:
                    if i[1] not in namelist:
                        display.append(i)
                        namelist.append(i[1])
                mycursor.execute("SELECT * from initialinfo")
                myresult=mycursor.fetchall()
                shirtno=myresult[-1]
                p=naa()
                query=("SELECT * from extrateam2 where matchno=%s")
                mycursor.execute(query,(p,))
                myresult=mycursor.fetchall()
                l=myresult
                n=0
                for i in l:
                    ##print(i)
                    n+=i[1]
                query=("SELECT * from scoreboard1 where matchno=%s and team1=%s")
                mycursor.execute(query,(p,team1))   
                showdown=mycursor.fetchall()
                showdown=showdown[-1]
                labelrunteam2batwin.config(text=team1score)
                labeloverteam2batwin.config(text=over)
                labelextrasteam2batwin.config(text="EXTRAS  "+str(n))

                for show in display:                            
                    if show[1] == shirtno[29]:  # Increment 18
                        labelteam2runsbatter1.config(text=show[2])
                        if show[10] == "WICKET":                            
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12],(show[8]))                            
                            labelteam2wicketbatter1.config(text=bowler)
                            
                    elif show[1] == shirtno[31]:  # Increment 18
                        labelteam2runsbatter2.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter2.config(text=bowler)
                            
                    elif show[1] == shirtno[33]:  # Increment 18
                        labelteam2runsbatter3.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter3.config(text=bowler)
                            
                            
                    elif show[1] == shirtno[35]:  # Increment 18
                        labelteam2runsbatter4.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter4.config(text=bowler)
                            
                    elif show[1] == shirtno[37]:  # Increment 18
                        labelteam2runsbatter5.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter5.config(text=bowler)
                            
                    elif show[1] == shirtno[39]:  # Increment 18
                        labelteam2runsbatter6.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter6.config(text=bowler)
                            
                    elif show[1] == shirtno[41]:  # Increment 18
                        labelteam2runsbatter7.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter7.config(text=bowler)
                            
                    elif show[1] == shirtno[43]:  # Increment 18
                        labelteam2runsbatter8.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter8.config(text=bowler)
                            
                    elif show[1] == shirtno[45]:  # Increment 18
                        labelteam2runsbatter9.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter9.config(text=bowler)
                            
                    elif show[1] == shirtno[47]:  # Increment 18
                        labelteam2runsbatter10.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter10.config(text=bowler)
                            
                    elif show[1] == shirtno[49]:  # Increment 20
                        labelteam2runsbatter11.config(text=show[2])
                        if show[10] == "WICKET":
                            striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                            labelteam2wicketbatter11.config(text=bowler)
                
                
                count = 0
                for wicket in display:
                    if count == 0:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket1_bat.config(text=run[0])
                            count += 1
                    elif count == 1:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket2_bat.config(text=run[0])
                            count += 1
                    elif count == 2:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket3_bat.config(text=run[0])
                            count += 1
                    elif count == 3:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket4_bat.config(text=run[0])
                            count += 1
                    elif count == 4:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket5_bat.config(text=run[0])
                            count += 1
                    elif count == 5:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket6_bat.config(text=run[0])
                            count += 1
                    elif count == 6:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket7_bat.config(text=run[0])
                            count += 1
                    elif count == 7:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket8_bat.config(text=run[0])
                            count += 1
                    elif count == 8:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket9_bat.config(text=run[0])
                            count += 1
                    elif count == 9:
                        if wicket[10] == "WICKET":
                            run = wicket[6].split("/")
                            team2wicket10_bat.config(text=run[0])
                            count += 1
         
            elif windowbatterteam2 is None:
                    windowbatterteam2=Tk()
                    windowbatterteam2.geometry("700x630")
                    windowbatterteam2.title("BATTERS STATS")
                    windowbatterteam2.config(background="lavender",padx=60,pady=10,border=25)
                    label = Label(windowbatterteam2, width=42, text=team1, font=("Arial", 15, "bold"), bg="DODGERBLUE", fg="white", relief=RIDGE, bd=10)
                    label.place(x=0, y=0)

                    label=Label(windowbatterteam2,width=16,text="BATTER",font=("Arial",13, "bold"),bg="DARKBLUE",fg="white",relief=RIDGE,bd=10)
                    label.place(x=0,y=50)
                    label=Label(windowbatterteam2,width=16,text="RUNS(BALLS)",font=("Arial",13, "bold"),bg="DARKBLUE",fg="white",relief=RIDGE,bd=10)
                    label.place(x=180,y=50)
                    label=Label(windowbatterteam2,width=14,text="WICKET BY",font=("Arial",13, "bold"),bg="DARKBLUE",fg="white",relief=RIDGE,bd=10)
                    label.place(x=360,y=50)
                    y1=100
                    mycursor.execute("SELECT * from initialinfo")
                    myresult=mycursor.fetchall()
                    initialdetails=myresult[-1]
                    index = 28
                    # Initialize starting values for y1 and index
                    index = 28

                    # Batter 1
                    labelteam2batter1 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter1.place(x=0, y=y1)

                    labelteam2runsbatter1 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter1.place(x=190, y=y1)

                    labelteam2wicketbatter1 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter1.place(x=360, y=y1)

                    # Batter 2
                    y1 += 32
                    index += 2

                    labelteam2batter2 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter2.place(x=0, y=y1)

                    labelteam2runsbatter2 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter2.place(x=190, y=y1)

                    labelteam2wicketbatter2 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter2.place(x=360, y=y1)

                    # Batter 3
                    y1 += 32
                    index += 2

                    labelteam2batter3 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter3.place(x=0, y=y1)

                    labelteam2runsbatter3 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter3.place(x=190, y=y1)

                    labelteam2wicketbatter3 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter3.place(x=360, y=y1)

                    # Batter 4
                    y1 += 32
                    index += 2

                    labelteam2batter4 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter4.place(x=0, y=y1)

                    labelteam2runsbatter4 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter4.place(x=190, y=y1)

                    labelteam2wicketbatter4 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter4.place(x=360, y=y1)

                    # Batter 5
                    y1 += 32
                    index += 2

                    labelteam2batter5 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter5.place(x=0, y=y1)

                    labelteam2runsbatter5 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter5.place(x=190, y=y1)

                    labelteam2wicketbatter5 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter5.place(x=360, y=y1)

                    # Batter 6
                    y1 += 32
                    index += 2

                    labelteam2batter6 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter6.place(x=0, y=y1)

                    labelteam2runsbatter6 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter6.place(x=190, y=y1)

                    labelteam2wicketbatter6 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter6.place(x=360, y=y1)

                    # Batter 7
                    y1 += 32
                    index += 2

                    labelteam2batter7 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter7.place(x=0, y=y1)

                    labelteam2runsbatter7 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter7.place(x=190, y=y1)

                    labelteam2wicketbatter7 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter7.place(x=360, y=y1)

                    # Batter 8
                    y1 += 32
                    index += 2

                    labelteam2batter8 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter8.place(x=0, y=y1)

                    labelteam2runsbatter8 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter8.place(x=190, y=y1)

                    labelteam2wicketbatter8 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter8.place(x=360, y=y1)

                    # Batter 9
                    y1 += 32
                    index += 2

                    labelteam2batter9 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter9.place(x=0, y=y1)

                    labelteam2runsbatter9 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter9.place(x=190, y=y1)

                    labelteam2wicketbatter9 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter9.place(x=360, y=y1)

                    # Batter 10
                    y1 += 32
                    index += 2

                    labelteam2batter10 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter10.place(x=0, y=y1)

                    labelteam2runsbatter10 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter10.place(x=190, y=y1)

                    labelteam2wicketbatter10 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter10.place(x=360, y=y1)

                    # Batter 11
                    y1 += 32
                    index += 2

                    labelteam2batter11 = Label(windowbatterteam2, width=16, text=initialdetails[index], font=("Arial", 13, "bold"), bg="#4682B4", fg="white", relief=RIDGE, bd=10)
                    labelteam2batter11.place(x=0, y=y1)

                    labelteam2runsbatter11 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2runsbatter11.place(x=190, y=y1)

                    labelteam2wicketbatter11 = Label(windowbatterteam2, width=16, text="  ", font=("Arial", 13), bg="#2F4F4F", fg="white", relief=RIDGE, bd=10)
                    labelteam2wicketbatter11.place(x=360, y=y1)

                    x1 = 0
                    y1 += 45

                    # First row of batters (1 to 10) with bluish background for the first label
                    label = Label(windowbatterteam2, width=5, text="1", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="2", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="3", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="4", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="5", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="6", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="7", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="8", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50

                    label = Label(windowbatterteam2, width=5, text="9", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50
                    label = Label(windowbatterteam2, width=5, text="10", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    label.place(x=x1, y=y1)
                    x1 += 50


                    x1 = 0
                    y1 += 30

                    team2wicket1_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket1_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket2_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket2_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket3_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket3_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket4_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket4_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket5_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket5_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket6_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket6_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket7_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket7_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket8_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket8_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket9_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket9_bat.place(x=x1, y=y1)
                    x1 += 50

                    team2wicket10_bat = Label(windowbatterteam2, width=5, text="", font=("Arial", 13, "bold"), bg="#4112B4", fg="white", relief=RIDGE, bd=10)
                    team2wicket10_bat.place(x=x1, y=y1)
                    x1 += 50
                    query=("SELECT SUM(team2extra) AS total_sum FROM extrateam2 where matchno=%s");
                    mycursor.execute(query,(p,))
                    myresult=mycursor.fetchall()
                    p=1

                    y1+=48

                    labelrunteam2batwin=Label(windowbatterteam2,width=12,text=team1score,font=("Arial",15,"bold"),bg="gray13",fg="white",relief=RIDGE,bd=10)
                    labelrunteam2batwin.place(x=0,y=y1)

                    labeloverteam2batwin=Label(windowbatterteam2,width=12,text="OVER  "+over,font=("Arial",15,"bold"),bg="red",fg="white",relief=RIDGE,bd=10)
                    labeloverteam2batwin.place(x=165,y=y1)

                    labelextrasteam2batwin=Label(windowbatterteam2,width=14,text="EXTRAS  "+str(myresult),font=("Arial",15,"bold"),bg="darkgreen",fg="white",relief=RIDGE,bd=10)
                    labelextrasteam2batwin.place(x=330,y=y1)
                    query=("SELECT * from scoreboard1 where matchno=%s and team1=%s")
                    mycursor.execute(query,(p,team1))
                    scores=mycursor.fetchall()
                    templist=list()
                    namelist=list()
                    display=list()
                    #revresing for latest
                    for i in scores:
                        templist.insert(0,i)
                    #only once the name in list    
                    for i in templist:
                        if i[1] not in namelist:
                            display.append(i)
                            namelist.append(i[1])
                    mycursor.execute("SELECT * from initialinfo")
                    myresult=mycursor.fetchall()
                    shirtno=myresult[-1]
                    p=naa()
                    query=("SELECT * from extrateam2 where matchno=%s")
                    mycursor.execute(query,(p,))
                    myresult=mycursor.fetchall()
                    l=myresult
                    n=0
                    for i in l:
                        ##print(i)
                        n+=i[1]
                    query=("SELECT * from scoreboard1 where matchno=%s and team1=%s")
                    mycursor.execute(query,(p,team1))
                    showdown=mycursor.fetchall()
                    showdown=showdown[-1]
                    labelrunteam2batwin.config(text=team1score)
                    labeloverteam2batwin.config(text=over)
                    labelextrasteam2batwin.config(text="EXTRAS  "+str(n))
                    for show in display:                               
                        if show[1] == shirtno[29]:  # Increment 18
                            labelteam2runsbatter1.config(text=show[2])
                            if show[10] == "WICKET":                                
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12],(show[8]))                                
                                labelteam2wicketbatter1.config(text=bowler)
                                
                        elif show[1] == shirtno[31]:  # Increment 18
                            labelteam2runsbatter2.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter2.config(text=bowler)
                                
                        elif show[1] == shirtno[33]:  # Increment 18
                            labelteam2runsbatter3.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter3.config(text=bowler)
                                
                                
                        elif show[1] == shirtno[35]:  # Increment 18
                            labelteam2runsbatter4.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter4.config(text=bowler)
                                
                        elif show[1] == shirtno[37]:  # Increment 18
                            labelteam2runsbatter5.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter5.config(text=bowler)
                                
                        elif show[1] == shirtno[39]:  # Increment 18
                            labelteam2runsbatter6.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter6.config(text=bowler)
                                
                        elif show[1] == shirtno[41]:  # Increment 18
                            labelteam2runsbatter7.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter7.config(text=bowler)
                                
                        elif show[1] == shirtno[43]:  # Increment 18
                            labelteam2runsbatter8.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter8.config(text=bowler)
                                
                        elif show[1] == shirtno[45]:  # Increment 18
                            labelteam2runsbatter9.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter9.config(text=bowler)
                                
                        elif show[1] == shirtno[47]:  # Increment 18
                            labelteam2runsbatter10.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter10.config(text=bowler)
                                
                        elif show[1] == shirtno[49]:  # Increment 20
                            labelteam2runsbatter11.config(text=show[2])
                            if show[10] == "WICKET":
                                striker, nonstriker, team1, team2, bowler = define("-", "-", show[5], show[12], show[8])
                                labelteam2wicketbatter11.config(text=bowler)
                    count = 0
                    for wicket in display:
                        if count == 0:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket1_bat.config(text=run[0])
                                count += 1
                        elif count == 1:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket2_bat.config(text=run[0])
                                count += 1
                        elif count == 2:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket3_bat.config(text=run[0])
                                count += 1
                        elif count == 3:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket4_bat.config(text=run[0])
                                count += 1
                        elif count == 4:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket5_bat.config(text=run[0])
                                count += 1
                        elif count == 5:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket6_bat.config(text=run[0])
                                count += 1
                        elif count == 6:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket7_bat.config(text=run[0])
                                count += 1
                        elif count == 7:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket8_bat.config(text=run[0])
                                count += 1
                        elif count == 8:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket9_bat.config(text=run[0])
                                count += 1
                        elif count == 9:
                            if wicket[10] == "WICKET":
                                run = wicket[6].split("/")
                                team2wicket10_bat.config(text=run[0])
                                count += 1
        except Exception as e:
            # List of all the labels in your code
            windowbatterteam2=None
            labels = [
                labelteam2runsbatter1, labelteam2wicketbatter1,
                labelteam2runsbatter2, labelteam2wicketbatter2,
                labelteam2runsbatter3, labelteam2wicketbatter3,
                labelteam2runsbatter4, labelteam2wicketbatter4,
                labelteam2runsbatter5, labelteam2wicketbatter5,
                labelteam2runsbatter6, labelteam2wicketbatter6,
                labelteam2runsbatter7, labelteam2wicketbatter7,
                labelteam2runsbatter8, labelteam2wicketbatter8,
                labelteam2runsbatter9, labelteam2wicketbatter9,
                labelteam2runsbatter10, labelteam2wicketbatter10,
                labelteam2runsbatter11, labelteam2wicketbatter11,
                labelrunteam2batwin, labeloverteam2batwin, labelextrasteam2batwin
            ]

            # Assign None to all labels
            for lbl in labels:
                lbl = None
            # List of wicket labels in your code
            wicket_labels = [
                labelteam2wicketbatter1, labelteam2wicketbatter2, labelteam2wicketbatter3,
                labelteam2wicketbatter4, labelteam2wicketbatter5, labelteam2wicketbatter6,
                labelteam2wicketbatter7, labelteam2wicketbatter8, labelteam2wicketbatter9,
                labelteam2wicketbatter10, labelteam2wicketbatter11, labelrunteam2batwin,
                labeloverteam2batwin, labelextrasteam2batwin
            ]

            # Assign None to all wicket labels
            for lbl in wicket_labels:
                lbl = None
            windowbatterteam2=None
            detailsbatter(team1_pass, team2_pass, strikervalue_pass, strikerscorevalue_pass, nonstrikervalue_pass, nonstrikerscorevalue_pass, team1scoreteam2value_pass, overvalue_pass)
def submitteaminfo(
    team1name, team1player1name, team1player1shirtno,
    team1player2name, team1player2shirtno, team1player3name, team1player3shirtno,
    team1player4name, team1player4shirtno, team1player5name, team1player5shirtno,
    team1player6name, team1player6shirtno, team1player7name, team1player7shirtno,
    team1player8name, team1player8shirtno, team1player9name, team1player9shirtno,
    team1player10name, team1player10shirtno, team1player11name, team1player11shirtno,
    team2name, team2player1name, team2player1shirtno, team2player2name, team2player2shirtno,
    team2player3name, team2player3shirtno, team2player4name, team2player4shirtno,
    team2player5name, team2player5shirtno, team2player6name, team2player6shirtno,
    team2player7name, team2player7shirtno, team2player8name, team2player8shirtno,
    team2player9name, team2player9shirtno, team2player10name, team2player10shirtno,
    team2player11name, team2player11shirtno, toss, tosschoice, ground, matchno
):
    try:

        # Extract values from the input widgets
        values = (
            int(matchno.get()), ground.get(), toss.get(), tosschoice.get(),
            team1name.get(),
            team1player1name.get(), team1player1shirtno.get(),
            team1player2name.get(), team1player2shirtno.get(),
            team1player3name.get(), team1player3shirtno.get(),
            team1player4name.get(), team1player4shirtno.get(),
            team1player5name.get(), team1player5shirtno.get(),
            team1player6name.get(), team1player6shirtno.get(),
            team1player7name.get(), team1player7shirtno.get(),
            team1player8name.get(), team1player8shirtno.get(),
            team1player9name.get(), team1player9shirtno.get(),
            team1player10name.get(), team1player10shirtno.get(),
            team1player11name.get(), team1player11shirtno.get(),
            team2name.get(),
            team2player1name.get(), team2player1shirtno.get(),
            team2player2name.get(), team2player2shirtno.get(),
            team2player3name.get(), team2player3shirtno.get(),
            team2player4name.get(), team2player4shirtno.get(),
            team2player5name.get(), team2player5shirtno.get(),
            team2player6name.get(), team2player6shirtno.get(),
            team2player7name.get(), team2player7shirtno.get(),
            team2player8name.get(), team2player8shirtno.get(),
            team2player9name.get(), team2player9shirtno.get(),
            team2player10name.get(), team2player10shirtno.get(),
            team2player11name.get(), team2player11shirtno.get()
        )

        columns = (
            "matchno", "ground", "toss", "tosschoice",
            "team1", "team1player1", "team1player1shirtno", "team1player2", "team1player2shirtno",
            "team1player3", "team1player3shirtno", "team1player4", "team1player4shirtno",
            "team1player5", "team1player5shirtno", "team1player6", "team1player6shirtno",
            "team1player7", "team1player7shirtno", "team1player8", "team1player8shirtno",
            "team1player9", "team1player9shirtno", "team1player10", "team1player10shirtno",
            "team1player11", "team1player11shirtno", "team2", "team2player1", "team2player1shirtno",
            "team2player2", "team2player2shirtno", "team2player3", "team2player3shirtno",
            "team2player4", "team2player4shirtno", "team2player5", "team2player5shirtno",
            "team2player6", "team2player6shirtno", "team2player7", "team2player7shirtno",
            "team2player8", "team2player8shirtno", "team2player9", "team2player9shirtno",
            "team2player10", "team2player10shirtno", "team2player11", "team2player11shirtno"
        )
        ##print(matchno.get())

        sql_formula = f"INSERT INTO initialinfo ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(values))})"

        # Debugging: #print the SQL query and values
        ##print(f"SQL Query: {sql_formula}")
        ##print(f"Values: {values}")
        mycursor.execute(sql_formula, values)
        print("Record inserted successfully.")
        mydb.commit()

        try:
            mycursor.execute("SELECT * FROM scoreboard1")
            k=mycursor.fetchall()
            M=k[-1][0]+1
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', {matchno.get()})")
            mydb.commit()
            scoresentry()
        except Exception as e:
            #print(e)
            mycursor.execute("SELECT * FROM INITIALINFO")
            K=mycursor.fetchall()
            k=K[-1]
            p=k
            M=0
            mycursor.execute(f"INSERT INTO scoreboard1 VALUES ({M},'{p[6]}', '0(0)',{p[10]}, '0(0)','{p[4]}', '0/0', '0.0', '{p[49]}', '0/0/0', '-', '0','{p[27]}', '-', {matchno.get()})")
            mydb.commit()
            scoresentry()

    except Exception as e:
        messagebox.showinfo("WARNING","UPDATE THE MATCH NO. TO START NEW MATCH")


def startmatch():
    global windownewstart
    if windownewstart is None:
        windownewstart=Tk()
        windownewstart.geometry("1100x550")
        windownewstart.title("ENTERING DETAILS OF A NEW MATCH")
        windownewstart.config(background="skyblue",padx=60,border=25)
        label=Label(windownewstart,width=80,text="ENTER DETAILS OF NEW MATCH",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=0)

        label=Label(windownewstart,width=19,text="MATCH NO:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)     
        label.place(x=710,y=0)

        matchno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        matchno.insert(0,"1")
        matchno.place(x=900,y=0)
        label=Label(windownewstart,width=25,text="TEAM 1 NAME:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=50)
        
        
        team1name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=25)
        team1name.insert(0,"AUSTRALIA")
        team1name.place(x=250,y=50)
        
        label=Label(windownewstart,width=25,text="PLAYER1 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=80)
        team1player1name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)    
        team1player1name.place(x=250,y=80)
        team1player1name.insert(0,"T HEAD")
        team1player1shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player1shirtno.insert(0,"62")
        team1player1shirtno.place(x=404,y=80)

        label=Label(windownewstart,width=25,text="PLAYER2 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=112)
        team1player2name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player2name.insert(0,"M MARSH")
        team1player2name.place(x=250,y=112)
        team1player2shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player2shirtno.insert(0,"32")
        team1player2shirtno.place(x=404,y=112)

        label=Label(windownewstart,width=25,text="PLAYER3 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=144)
        team1player3name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player3name.insert(0,"S SMITH")
        team1player3name.place(x=250,y=144)
        team1player3shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player3shirtno.insert(0,"49")
        team1player3shirtno.place(x=404,y=144)

        label=Label(windownewstart,width=25,text="PLAYER4 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=176)
        team1player4name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player4name.insert(0,"M LABUSHANGE")
        team1player4name.place(x=250,y=176)
        team1player4shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player4shirtno.insert(0,"13")
        team1player4shirtno.place(x=404,y=176)

        label=Label(windownewstart,width=25,text="PLAYER5 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=208)
        team1player5name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player5name.insert(0,"M STONIS")
        team1player5name.place(x=250,y=208)
        team1player5shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player5shirtno.insert(0,"14")
        team1player5shirtno.place(x=404,y=208)

        label=Label(windownewstart,width=25,text="PLAYER6 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=240)
        team1player6name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player6name.insert(0,"C GREEN")
        team1player6name.place(x=250,y=240)
        team1player6shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player6shirtno.insert(0,"36")
        team1player6shirtno.place(x=404,y=240)

        label=Label(windownewstart,width=25,text="PLAYER7 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=272)
        team1player7name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player7name.insert(0,"A CAREY")
        team1player7name.place(x=250,y=272)
        team1player7shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player7shirtno.insert(0,"99")
        team1player7shirtno.place(x=404,y=272)

        label=Label(windownewstart,width=25,text="PLAYER8 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=304)
        team1player8name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player8name.insert(0,"P CUMMINS")
        team1player8name.place(x=250,y=304)
        team1player8shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player8shirtno.insert(0,"30")
        team1player8shirtno.place(x=404,y=304)

        label=Label(windownewstart,width=25,text="PLAYER9 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=336)
        team1player9name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player9name.insert(0,"M STARC")
        team1player9name.place(x=250,y=336)
        team1player9shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player9shirtno.insert(0,"56")
        team1player9shirtno.place(x=404,y=336)

        label=Label(windownewstart,width=25,text="PLAYER10 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=376)
        team1player10name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player10name.insert(0,"J HEZALWOOD")
        team1player10name.place(x=250,y=376)
        team1player10shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player10shirtno.insert(0,"35")
        team1player10shirtno.place(x=404,y=376)

        label=Label(windownewstart,width=25,text="PLAYER11 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=408)
        team1player11name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team1player11name.insert(0,"A ZAMPA")
        team1player11name.place(x=250,y=408)
        team1player11shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team1player11shirtno.insert(0,"6")
        team1player11shirtno.place(x=404,y=408)

        label=Label(windownewstart,width=25,text="TOSS:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=440)    
        toss=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=25)
        toss.insert(0,"AUSTRALIA")
        toss.place(x=250,y=440)
        #team2 entries
        label=Label(windownewstart,width=25,text="TEAM 2 NAME:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=50)
        team2name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=25)
        team2name.insert(0,"INDIA")
        team2name.place(x=710,y=50)
        
        label=Label(windownewstart,width=25,text="PLAYER1 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=80)
        team2player1name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player1name.insert(0,"ROHIT")
        team2player1name.place(x=710,y=80)
        team2player1shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player1shirtno.insert(0,"45")
        team2player1shirtno.place(x=900,y=80)

        label=Label(windownewstart,width=25,text="PLAYER2 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=112)
        team2player2name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player2name.insert(0,"SHUBMAN")
        team2player2name.place(x=710,y=112)
        team2player2shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player2shirtno.insert(0,"77")
        team2player2shirtno.place(x=900,y=112)

        label=Label(windownewstart,width=25,text="PLAYER3 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=144)
        team2player3name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player3name.insert(0,"KOHLI")
        team2player3name.place(x=710,y=144)
        team2player3shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player3shirtno.insert(0,"18")
        team2player3shirtno.place(x=900,y=144)

        label=Label(windownewstart,width=25,text="PLAYER4 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=176)
        team2player4name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player4name.insert(0,"SHREYAS")
        team2player4name.place(x=710,y=176)
        team2player4shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player4shirtno.insert(0,"23")
        team2player4shirtno.place(x=900,y=176)

        label=Label(windownewstart,width=25,text="PLAYER5 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=208)
        team2player5name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player5name.insert(0,"KL RAHUL")
        team2player5name.place(x=710,y=208)
        team2player5shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player5shirtno.insert(0,"1")
        team2player5shirtno.place(x=900,y=208)

        label=Label(windownewstart,width=25,text="PLAYER6 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=240)
        team2player6name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player6name.insert(0,"JADEJA")
        team2player6name.place(x=710,y=240)
        team2player6shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player6shirtno.insert(0,"8")
        team2player6shirtno.place(x=900,y=240)

        
        label=Label(windownewstart,width=25,text="PLAYER7 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=272)
        team2player7name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player7name.insert(0,"HARDIK")
        team2player7name.place(x=710,y=272)
        team2player7shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player7shirtno.insert(0,"12")
        team2player7shirtno.place(x=900,y=272)

        label=Label(windownewstart,width=25,text="PLAYER8 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=304)
        team2player8name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player8name.insert(0,"KULDEEP")
        team2player8name.place(x=710,y=304)
        team2player8shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player8shirtno.insert(0,"23")
        team2player8shirtno.place(x=900,y=304)

        label=Label(windownewstart,width=25,text="PLAYER9 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=336)
        team2player9name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player9name.insert(0,"BUMRAH")
        team2player9name.place(x=710,y=336)
        team2player9shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player9shirtno.insert(0,"93")
        team2player9shirtno.place(x=900,y=336)

        label=Label(windownewstart,width=25,text="PLAYER10 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=376)
        team2player10name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player10name.insert(0,"SIRAJ")
        team2player10name.place(x=710,y=376)
        team2player10shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player10shirtno.insert(0,"73")
        team2player10shirtno.place(x=900,y=376)

        label=Label(windownewstart,width=25,text="PLAYER11 NAME//SHIRT NO.:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=408)
        team2player11name=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=19)
        team2player11name.insert(0,"SHAMI")
        team2player11name.place(x=710,y=408)
        team2player11shirtno=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=4)
        team2player11shirtno.insert(0,"11")
        team2player11shirtno.place(x=900,y=408)

        label=Label(windownewstart,width=25,text="TOSS WINNER CHOICE:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=462,y=440)    
        tosschoice=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=25)
        tosschoice.insert(0,"BAT")
        tosschoice.place(x=710,y=440)

        label=Label(windownewstart,width=25,text="ENTER GROUND NAME:",font=("Arial",12),bg="black",fg="white",relief=RIDGE,bd=10)
        label.place(x=0,y=476)    
        ground=Entry(windownewstart,font=("Arial",12),fg="white",bg="red",bd=10,relief=RIDGE,width=22)
        ground.insert(0,"SCG")
        ground.place(x=250,y=476)

        submit_button=Button(windownewstart,text="SUBMIT TEAM INFORMATION",
                             command=lambda:submitteaminfo(team1name,
                                                           team1player1name,team1player1shirtno,
                                                           team1player2name,team1player2shirtno,
                                                           team1player3name,team1player3shirtno,
                                                           team1player4name,team1player4shirtno,
                                                           team1player5name,team1player5shirtno,
                                                           team1player6name,team1player6shirtno,
                                                           team1player7name,team1player7shirtno,
                                                           team1player8name,team1player8shirtno,
                                                           team1player9name,team1player9shirtno,
                                                           team1player10name,team1player10shirtno,
                                                           team1player11name,team1player11shirtno,
                                                           team2name,
                                                           team2player1name,team2player1shirtno,
                                                           team2player2name,team2player2shirtno,
                                                           team2player3name,team2player3shirtno,
                                                           team2player4name,team2player4shirtno,
                                                           team2player5name,team2player5shirtno,
                                                           team2player6name,team2player6shirtno,
                                                           team2player7name,team2player7shirtno,
                                                           team2player8name,team2player8shirtno,
                                                           team2player9name,team2player9shirtno,
                                                           team2player10name,team2player10shirtno,
                                                           team2player11name,team2player11shirtno,
                                                           toss,tosschoice,ground,matchno
                                                           ),font=("Arial",13,"bold"),bd=5,relief=RIDGE,width=40,bg="darkgreen",fg="white",padx=30)
        submit_button.place(x=470,y=476)

def startwindow():
    global windowfirst
    if windowfirst is None:
        try:
            # Initialize main window
            windowfirst = Tk()
            windowfirst.geometry("1000x500")  # Adjusted dimensions
            windowfirst.title("Cricket Match Tracker")
            windowfirst.config(background="#f5f5f5")

            # Title Label
            title_label = Label(
                windowfirst,
                text="🏏 Welcome to Cricket Match Tracker 🏏",
                font=("Arial", 22, "bold"),
                fg="#2C3E50",
                bg="#f5f5f5",
            )
            title_label.place(x=50, y=90)

            # Subtitle Label
            subtitle_label = Label(
                windowfirst,
                text="Track, Continue, or View Your Matches Effortlessly",
                font=("Arial", 13, "italic"),
                fg="#34495E",
                bg="#f5f5f5",
            )
            subtitle_label.place(x=320, y=150)

            # Button Styles
            button_style = {
                "font": ("Arial", 15, "bold"),
                "fg": "white",
                "bd": 6,
                "relief": RAISED,
                "padx": 2,
                "pady": 6,
                "highlightthickness": 0,
            }

            # Start a New Match Button
            newmatch_button = Button(
                windowfirst,
                text="🆕 START A NEW MATCH",
                command=startmatch,  # Ensure startmatch function exists
                bg="#3498DB",
                activebackground="#2980B9",
                activeforeground="white",
                **button_style,
            )
            newmatch_button.place(x=70, y=220)

            # Continue Match Button
            continue_button = Button(
                windowfirst,
                text="⏸️ CONTINUE MATCH",
                command=scoresentry,  # Ensure scoresentry function exists
                bg="#2ECC71",
                activebackground="#27AE60",
                activeforeground="white",
                **button_style,
            )
            continue_button.place(x=350, y=220)

            # View Match Details Button
            viewinfomatch_button = Button(
                windowfirst,
                text="📊 VIEW LATEST MATCH DETAILS",
                command=windowlast,  # Ensure windowlast function exists
                bg="#9B59B6",
                activebackground="#8E44AD",
                activeforeground="white",
                **button_style,
            )
            viewinfomatch_button.place(x=620, y=220)

            # Footer Label
            footer_label = Label(
                windowfirst,
                text="Developed with ❤️ for cricket enthusiasts.",
                font=("Arial", 13),
                fg="#7F8C8D",
                bg="#f5f5f5",
            )
            footer_label.place(x=350, y=420)  # Moved slightly up from the bottom

            # Run the application
            windowfirst.mainloop()

        except Exception as e:
            messagebox.showerror(
                "Unexpected Error",
                "Something went wrong while launching the application. Please try again later.",
            )
def finish():
    try:
        from tkinter import Tk, Label, Entry, Button, RIDGE, messagebox
    except ImportError:
        messagebox.showerror(
            "Error", "An essential module could not be loaded. Please ensure Python is correctly installed."
        )
        return

    try:
        # Initialize match summary window
        windowfinish = Tk()
        windowfinish.geometry("700x530")
        windowfinish.title("Match Summary")
        windowfinish.config(background="dodgerblue", padx=50, pady=50)

        # Common styling parameters
        label_font = ("Arial", 14, "bold")
        entry_font = ("Arial", 14)
        label_bg = "#2e2e2e"
        label_fg = "#ffffff"
        entry_bg = "#d9534f"
        entry_fg = "#ffffff"
        relief_style = RIDGE
        border_width = 10

        # Function to create labels and entries
        def create_label_and_entry(window, label_text, x, y):
            label = Label(
                window,
                width=22,
                text=label_text,
                font=label_font,
                bg=label_bg,
                fg=label_fg,
                relief=relief_style,
                bd=border_width,
            )
            label.place(x=x, y=y)

            entry = Entry(
                window,
                font=entry_font,
                fg=entry_fg,
                bg=entry_bg,
                bd=border_width,
                relief=relief_style,
            )
            entry.place(x=x + 290, y=y)
            return entry

        # Create labels and entries for the summary details
        matchno = create_label_and_entry(windowfinish, "MATCH NO.:", 0, 10)
        winningteam = create_label_and_entry(windowfinish, "WINNING TEAM:", 0, 80)
        winmargin = create_label_and_entry(windowfinish, "WIN MARGIN:", 0, 160)
        mom = create_label_and_entry(windowfinish, "MAN OF THE MATCH:", 0, 240)
        loosingteam = create_label_and_entry(windowfinish, "LOSING TEAM:", 0, 320)

        # Function to handle form submission
        def submitfinish(matchno, winningteam, winmargin, mom, loosingteam):
            try:
                data = {
                    "Match No": matchno.get(),
                    "Winning Team": winningteam.get(),
                    "Win Margin": winmargin.get(),
                    "Man of the Match": mom.get(),
                    "Losing Team": loosingteam.get(),
                }
                # Placeholder for processing the data
                print(data)  # Replace with actual save or process logic
                messagebox.showinfo("Success", "Match summary submitted successfully!")
                windowfinish.destroy()
            except Exception as e:
                messagebox.showerror(
                    "Error", "An error occurred while submitting the match summary. Please try again."
                )

        # Submit button with improved styling
        submit_button = Button(
            windowfinish,
            text="SUBMIT",
            command=lambda: submitfinish(matchno, winningteam, winmargin, mom, loosingteam),
            font=("Arial", 19, "bold"),
            fg="#ffffff",
            bg="#5cb85c",
            bd=10,
            relief=RIDGE,
        )
        submit_button.place(x=180, y=400)

        windowfinish.mainloop()

    except Exception as e:
        messagebox.showerror(
            "Unexpected Error",
            "Something went wrong while launching the match summary window. Please try again."
        )

def unentryupdate(strikerscorevalue_entry,impactvalue_entry,team1scoreteam2value_entry,
                  overvalue_entry,bowlerstatsvalue_entry,overstatsvalue_entry,notevalue_entry,armvalue_entry,team2value,bowlervalue):
    strikerscorevalue_edit = strikerscorevalue_entry.get()
    impactvalue_edit = impactvalue_entry.get()
    team1scoreteam2value_edit = team1scoreteam2value_entry.get()
    overvalue_edit = overvalue_entry.get()
    bowlerstatsvalue_edit = bowlerstatsvalue_entry.get()
    overstatsvalue_edit = overstatsvalue_entry.get()
    notevalue_edit = notevalue_entry.get()
    armvalue_edit = armvalue_entry.get()
    team2value_edit=team2value.get()
    bowlervalue_edit=bowlervalue.get()
    mycursor.execute("select * from initialinfo")
    myresult=mycursor.fetchall()
    myresult=myresult[-1]    
    if team2value_edit==myresult[4]:
        mycursor.execute("select * from bowlerstatsteam1")
        myresult=mycursor.fetchall()
        templist=list()
        display=list()
        namelist=list()
        for i in myresult:
            templist.insert(0,i)
        #only once the name in list    
        for i in templist:
            if i[1] not in namelist:
                display.append(i)
                namelist.append(i[1])
        mycursor.execute("select * from initialinfo")
        myresult=mycursor.fetchall()
        myresult=myresult[-1]
        index=25
        for j in display:         
            if j[1]==myresult[index]:
                bowlerstatsvalue_edit=j[2]                 
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]        
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]            
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]           
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]
            else:
                bowlerstatsvalue_edit="0/0/0"     
    elif team2value_edit==myresult[27]:
        mycursor.execute("select * from bowlerstatsteam2")
        myresult=mycursor.fetchall()
        templist=list()
        display=list()
        namelist=list()
        #print(myresult)
        for i in myresult:
            templist.insert(0,i)
        #only once the name in list    
        for i in templist:
            if i[1] not in namelist:
                display.append(i)
                namelist.append(i[1])
        mycursor.execute("select * from initialinfo")
        myresult=mycursor.fetchall()
        myresult=myresult[-1]
        index=48
        for j in display:         
            if j[1]==myresult[index]:
                bowlerstatsvalue_edit=j[2]
                 
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]        
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]            
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]          
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]           
            elif j[1]==myresult[index-2]:
                bowlerstatsvalue_edit=j[2]
            else:
                bowlerstatsvalue_edit="0/0/0"
 
    if notevalue_edit=="wicket" or notevalue_edit=="WICKET":
        team1scoreteam2value_edit1=team1scoreteam2value_edit.split("/")
        team1scoreteam2value_edit2=str(int(team1scoreteam2value_edit1[0])+int(impactvalue_edit))+"/"+str(int(team1scoreteam2value_edit1[1])+1)
    else:
        team1scoreteam2value_edit1=team1scoreteam2value_edit.split("/")
        team1scoreteam2value_edit2=str(int(team1scoreteam2value_edit1[0])+int(impactvalue_edit))+"/"+team1scoreteam2value_edit1[1]

    if notevalue_edit[0:5]=="EXTRA":
        pass
    else:
        strikerscorevalue_edit1=strikerscorevalue_edit.split("(")
        strikerscorevalue_edit12=strikerscorevalue_edit1[1][0:-1]
        strikerscorevalue_edit2=str(int(strikerscorevalue_edit1[0])+int(impactvalue_edit))+"("+str(int(strikerscorevalue_edit12)+1)+")"
        
    bowlerstatsvalue_edit1=bowlerstatsvalue_edit.split("/")
    bowlerstatsvalue_edit11=(str(bowlerstatsvalue_edit1[2]))

    if notevalue_edit[0:5]=="EXTRA":
        bowlerstatsvalue_edit1=bowlerstatsvalue_edit.split("/")
        bowlerstatsvalue_edit2=bowlerstatsvalue_edit1[0]+"/"+str(int(bowlerstatsvalue_edit1[1])+int(impactvalue_edit))+"/"+str(bowlerstatsvalue_edit1[2])

    elif notevalue_edit=="wicket" or notevalue_edit=="WICKET":
        bowlerstatsvalue_edit1=bowlerstatsvalue_edit.split("/")
        bowlerstatsvalue_edit2=str(int(bowlerstatsvalue_edit1[0])+1)+"/"+str(int(bowlerstatsvalue_edit1[1])+int(impactvalue_edit))+"/"+(str((float(bowlerstatsvalue_edit1[2])+0.1))[0:3])

    elif bowlerstatsvalue_edit11=="0.6":
        bowlerstatsvalue_edit1=bowlerstatsvalue_edit.split("/")
        bowlerstatsvalue_edit2=str(int(bowlerstatsvalue_edit1[0]))+"/"+str(int(bowlerstatsvalue_edit1[1])+int(impactvalue_edit))+"/"+str((float(bowlerstatsvalue_edit1[2])+1.0))[0:1]

    else:
        bowlerstatsvalue_edit1=bowlerstatsvalue_edit.split("/")
        bowlerstatsvalue_edit2=bowlerstatsvalue_edit1[0]+"/"+str(int(bowlerstatsvalue_edit1[1])+int(impactvalue_edit))+"/"+(str((float(bowlerstatsvalue_edit1[2])+0.1))[0:3])

    if notevalue_edit=="wicket" or notevalue_edit=="WICKET":
        overstatsvalue_edit2=overstatsvalue_edit+"W"+","
    else:
        overstatsvalue_edit2=overstatsvalue_edit+impactvalue_edit+","

    if notevalue_edit[0:5]=="EXTRA":   
        pass
    elif overvalue_edit[2]=="6":
         overvalue_edit2=str(float(overvalue_edit)+1.0)[0]
    else:
        overvalue_edit2=str(float(overvalue_edit)+0.1)[0:3]   
    return  team1scoreteam2value_edit2,   strikerscorevalue_edit2  ,bowlerstatsvalue_edit2   ,overstatsvalue_edit2,overvalue_edit2

import tkinter.messagebox as MessageBox
def scoresentry():

    global entrywindow
    global strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry
    global team1value_entry, team2value_entry, impactvalue_entry, team1scoreteam2value_entry, overvalue_entry
    global bowlervalue_entry, bowlerstatsvalue_entry, overstatsvalue_entry, notevalue_entry, armvalue_entry

    try:
        if entrywindow is None:
            new = read()  # Assuming `read()` fetches the necessary data
            
            # Assign values from the read data (e.g., striker info, non-striker info)
            strikervalue_insert = new[1]
            nonstrikervalue_insert = new[3]
            strikerscorevalue_insert = new[2]
            nonstrikerscorevalue_insert = new[4]
            
            entrywindow = Tk()
            entrywindow.geometry("920x500")
            entrywindow.title("Scoreboard Info Entry")
            entrywindow.config(background="lavender", border=25)
            if new[10]=="DEAD" or new[10][0:5]=="EXTRA":
                pass
            else:
                if new[11] == "1" or new[11] == "3" or new[11] == "0" and new[6][-1] == "6":
                    k = nonstrikervalue_insert
                    p = nonstrikerscorevalue_insert
                    nonstrikervalue_insert = strikervalue_insert
                    nonstrikerscorevalue_insert = strikerscorevalue_insert
                    strikervalue_insert = k
                    strikerscorevalue_insert = p

            # Creating labels and entry fields (as per your original code)
            labelstriker = Label(entrywindow, width=22, text="STRIKER SHIRT NO.:", font=("Arial", 13), bg="black", fg="white", relief=RIDGE, bd=10)
            labelstriker.place(x=0, y=10)
            strikervalue_entry = Entry(entrywindow, font=("Arial", 13), fg="white", bg="red", bd=10, relief=RIDGE)
            strikervalue_entry.insert(0, strikervalue_insert)
            strikervalue_entry.place(x=210, y=10)

            labelstrikerscore = Label(entrywindow, width=22, text="STRIKER SCORE:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelstrikerscore.place(x=0, y=60)
            strikerscorevalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            strikerscorevalue_entry.insert(0, strikerscorevalue_insert)
            strikerscorevalue_entry.place(x=210, y=60)

            labelnonstriker = Label(entrywindow, width=22, text="NON-STRIKER SHIRT NO.:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelnonstriker.place(x=0, y=110)
            nonstrikervalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            nonstrikervalue_entry.insert(0, nonstrikervalue_insert)
            nonstrikervalue_entry.place(x=210, y=110)

            labelnonstrikerscore = Label(entrywindow, width=22, text="NON-STRIKER SCORE:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelnonstrikerscore.place(x=0, y=160)
            nonstrikerscorevalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            nonstrikerscorevalue_entry.insert(0, nonstrikerscorevalue_insert)
            nonstrikerscorevalue_entry.place(x=210, y=160)

            labelteam1 = Label(entrywindow, width=22, text="BATTING TEAM NAME:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelteam1.place(x=0, y=210)
            team1value_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            team1value_entry.delete(0, END)
            team1value_entry.insert(0, new[5])
            team1value_entry.place(x=210, y=210)

            labelteam2 = Label(entrywindow, width=22, text="BOWLING TEAM NAME:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelteam2.place(x=0, y=260)
            team2value_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            team2value_entry.insert(0, new[12])
            team2value_entry.place(x=210, y=260)

            labelimpact = Label(entrywindow, width=22, text="IMPACT BALL BOLWED:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelimpact.place(x=0,y=310)
            impactvalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            impactvalue_entry.insert(0, new[11])
            impactvalue_entry.place(x=210,y=310)

            labelteam1score = Label(entrywindow, width=23, text="BATTING TEAM SCORE:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelteam1score.place(x=450, y=10)
            team1scoreteam2value_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            team1scoreteam2value_entry.insert(0, new[6])
            team1scoreteam2value_entry.place(x=680, y=10)

            labelover = Label(entrywindow, width=23, text="OVER     :", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelover.place(x=450, y=60)
            overvalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            overvalue_entry.insert(0, new[7])
            overvalue_entry.place(x=680, y=60)

            labelbowler = Label(entrywindow, width=23, text="BOWLER SHIRT NO.:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelbowler.place(x=450, y=110)
            bowlervalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            bowlervalue_entry.insert(0, new[8])
            bowlervalue_entry.place(x=680, y=110)

            labelbowlerstats = Label(entrywindow, width=23, text="BOWLER STATS:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelbowlerstats.place(x=450, y=160)
            bowlerstatsvalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            bowlerstatsvalue_entry.insert(0, new[9])
            bowlerstatsvalue_entry.place(x=680, y=160)

            labeloverstats = Label(entrywindow, width=23, text="OVER STATS:", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labeloverstats.place(x=450, y=210)
            overstatsvalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            overstatsvalue_entry.insert(0, new[13])
            overstatsvalue_entry.place(x=680, y=210)

            labelnote = Label(entrywindow, width=23, text="NOTE::", font=("Arial",13), fg="white", bg="black", relief=RIDGE, bd=10)
            labelnote.place(x=450, y=260)
            notevalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            notevalue_entry.insert(0, new[10])
            notevalue_entry.place(x=680, y=260)

            labelarm = Label(entrywindow, width=23, text="ARMVALUE::", font=("Arial", 13, "bold"), fg="RED", bg="black", relief=RIDGE, bd=10)
            labelarm.place(x=450,y=310)
            armvalue_entry = Entry(entrywindow, font=("Arial",13), fg="white", bg="red", bd=10, relief=RIDGE)
            armvalue_entry.insert(0, new[0])
            armvalue_entry.place(x=680,y=310)
            
            submit_button = Button(entrywindow, text="Submit", command=lambda:submit(strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1value_entry, team1scoreteam2value_entry, overvalue_entry, bowlervalue_entry, bowlerstatsvalue_entry, overstatsvalue_entry, notevalue_entry, impactvalue_entry, team2value_entry, armvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            submit_button.place(x=610, y=380)
            #print(command)

            update_button = Button(entrywindow, text="Update", command=lambda: update(strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1value_entry, team1scoreteam2value_entry, overvalue_entry, bowlervalue_entry, bowlerstatsvalue_entry, overstatsvalue_entry, notevalue_entry, impactvalue_entry, team2value_entry, armvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            update_button.place(x=425, y=380)

            delete_button = Button(entrywindow, text="Delete", command=lambda: delete(strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1value_entry, team1scoreteam2value_entry, overvalue_entry, bowlervalue_entry, bowlerstatsvalue_entry, overstatsvalue_entry, notevalue_entry, impactvalue_entry, team2value_entry, armvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            delete_button.place(x=520, y=380)

            finish_button = Button(entrywindow, text="Finish", command=finish, font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            finish_button.place(x=710, y=380)

            quite_button = Button(entrywindow, text="Exit", command=quit_idle, font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            quite_button.place(x=800, y=380)

            detailsbowler_button = Button(entrywindow, text="Bowlers Stats", command=lambda: detailsbowler(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            detailsbowler_button.place(x=110, y=380)
        

            detailsbatter_button = Button(entrywindow, text="Batters Stats", command=lambda: detailsbatter(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            detailsbatter_button.place(x=270, y=380)
            mycursor.execute("select * from initialinfo")
            myresult=mycursor.fetchall()
            matchno=myresult[-1][0]
            
            refresh_button = Button(entrywindow, text="Refresh", command=lambda: refresh(team1value_entry, team2value_entry, strikervalue_entry, strikerscorevalue_entry, nonstrikervalue_entry, nonstrikerscorevalue_entry, team1scoreteam2value_entry, overvalue_entry), font=("Arial", 15, "bold"), bd=10, relief=RIDGE)
            refresh_button.place(x=5, y=380)
            entrywindow.mainloop()
        
        else:
            new = read()
            strikervalue_insert = new[1]
            nonstrikervalue_insert = new[3]
            strikerscorevalue_insert = new[2]
            nonstrikerscorevalue_insert = new[4]
            if new[10]=="DEAD" or new[10][0:5]=="EXTRA":
                pass
            else:
                if new[11] == "1" or new[11] == "3" or new[11] == "0" and new[6][-1] == "6":
                    k = nonstrikervalue_insert
                    p = nonstrikerscorevalue_insert
                    nonstrikervalue_insert = strikervalue_insert
                    nonstrikerscorevalue_insert= strikerscorevalue_insert
                    strikervalue_insert = k
                    strikerscorevalue_insert = p
            strikervalue_entry.delete(0, END)  # Clear current value
            strikervalue_entry.insert(0, strikervalue_insert )  # Insert new value

            # Clear and update the striker's score
            strikerscorevalue_entry.delete(0, END)
            strikerscorevalue_entry.insert(0,strikerscorevalue_insert )

            # Clear and update the non-striker value
            nonstrikervalue_entry.delete(0, END)
            nonstrikervalue_entry.insert(0, nonstrikervalue_insert )

            # Clear and update the non-striker's score
            nonstrikerscorevalue_entry.delete(0, END)
            nonstrikerscorevalue_entry.insert(0, nonstrikerscorevalue_insert )

            # Clear and update the batting team name
            team1value_entry.delete(0, END)
            team1value_entry.insert(0, new[5])

            # Clear and update the bowling team name
            team2value_entry.delete(0, END)
            team2value_entry.insert(0, new[12])

            # Clear and update the impact of the ball
            impactvalue_entry.delete(0, END)
            impactvalue_entry.insert(0, new[11])

            # Clear and update the batting team's score
            team1scoreteam2value_entry.delete(0, END)
            team1scoreteam2value_entry.insert(0, new[6])

            # Clear and update the over value
            overvalue_entry.delete(0, END)
            overvalue_entry.insert(0, new[7])

            # Clear and update the bowler's shirt number
            bowlervalue_entry.delete(0, END)
            bowlervalue_entry.insert(0, new[8])

            # Clear and update the bowler's stats
            bowlerstatsvalue_entry.delete(0, END)
            bowlerstatsvalue_entry.insert(0, new[9])

            # Clear and update the over stats
            overstatsvalue_entry.delete(0, END)
            overstatsvalue_entry.insert(0, new[13])

            # Clear and update the note
            notevalue_entry.delete(0, END)
            notevalue_entry.insert(0, new[10])

            # Clear and update the arm value
            armvalue_entry.delete(0, END)
            armvalue_entry.insert(0, new[0])
    except Exception as e:
        print(e)
        entrywindow=None
        strikervalue_entry = None
        strikerscorevalue_entry = None
        nonstrikervalue_entry = None
        nonstrikerscorevalue_entry = None
        team1value_entry = None
        team2value_entry = None
        impactvalue_entry = None
        team1scoreteam2value_entry = None
        overvalue_entry = None
        bowlervalue_entry = None
        bowlerstatsvalue_entry = None
        overstatsvalue_entry = None
        notevalue_entry = None
        armvalue_entry = None
        scoresentry()
        #print(e)

import tkinter as tk
from tkinter import messagebox
def control():
    global entrywindow, windowbowlerteam2, windowbowlerteam1, windowbatterteam2, windowbatterteam1, window1, windowfirst,root1

    # Function to dynamically create windows if needed
    def yourfunction(window_name):
        if window_name == "entrywindow":
            return scoresentry()

        elif window_name == "windowfirst":
            return startwindow()
        else:
            messagebox.showinfo("Note", "Go To Enter Ball Info>>Continue Match>>Batters or Bowlers Stats or Scoreboard Strip")

    # Function to show a specific window
    def show_window(window_name):
        try:
            #windowfirst.deiconify()
            window = globals().get(window_name)

            if window is None:  # Dynamically create window if not already existing
                window = yourfunction(window_name)
                globals()[window_name] = window
                

            # Restore and bring window to the front
           
            if window.state() == "iconic":
                window.deiconify()

            hide_all_windows()  # Hide other windows
            window.deiconify()
            window.focus_set()
        except Exception:
            pass
            #messagebox.showinfo("Note", "Go To Enter Ball Info>>Continue Match>>Batters or Bowlers Stats or Scoreboard Strip")
    def hide_all_windows():
        error_occurred = False
        for window_name in [
            "entrywindow", "windowbowlerteam2", "windowbowlerteam1",
            "windowbatterteam2", "windowbatterteam1", "window1", "windowfirst"
        ]:
            try:
                window = globals().get(window_name)
                if window is not None:
                    window.withdraw()
            except Exception:
                error_occurred = True
                continue  # Skip to the next window
        if error_occurred:
            messagebox.showerror("Error", "Some windows could not be hidden.")

    if root1 is None:
        # Main control window
        root1 = tk.Tk()
        root1.title("Control Panel")
        root1.state("zoomed")  # Full-screen
        root1.configure(bg="#f5f5f5")

        # Title label
        title_label = tk.Label(
            root1, text="🏏 Cricket Match Manager", font=("Arial", 24, "bold"), fg="#2C3E50", bg="#f5f5f5"
        )
        title_label.pack(pady=20)

        title_label = tk.Label(
            root1, text="🏏 Window Controller", font=("Arial", 13, "bold"), fg="#2C3E50", bg="#f5f5f5"
        )
        title_label.pack(pady=20 ,fill="x")

        # Buttons frame on the right
        # Buttons frame on the right
        button_frame = tk.Frame(root1, bg="#ffffff", relief="raised", borderwidth=2)
        button_frame.pack(side="right", fill="y", padx=20, pady=(2, 0))  # Adjust top padding with pady=(20, 0)

        # Themed button styles
        button_style = {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "bd": 6,
            "relief": "raised",
            "padx": 10,
            "pady": 10,
            "highlightthickness": 0,
        }     
        # Themed buttons
        
        tk.Button(button_frame, text="🏆 First Window", command=lambda: show_window("windowfirst"), bg="#34495E", activebackground="#2C3E50", **button_style).pack(fill="x", pady=2)
        tk.Button(button_frame, text="🏏 Enter New Ball Info", command=lambda: show_window("entrywindow"), bg="#3498DB", activebackground="#2980B9", **button_style).pack(fill="x", pady=2)
        
        
        tk.Button(button_frame, text="📊 Scorboard Strip", command=lambda: show_window("window1"), bg="#E67E22", activebackground="#D35400", **button_style).pack(fill="x", pady=5)    
        tk.Button(button_frame, text=f"🏏 Batters Stats First Inning", command=lambda: show_window("windowbatterteam1"), bg="#2ECC71", activebackground="#8E44AD", **button_style).pack(fill="x", pady=2)
        
        tk.Button(button_frame, text=f"🎯 Bowler Stats First Inning", command=lambda: show_window("windowbowlerteam2"), bg="#9B59B6", activebackground="#27AE60", **button_style).pack(fill="x", pady=2)
        tk.Button(button_frame, text=f"🎯 Bowler Stats Second Inning", command=lambda: show_window("windowbowlerteam1"), bg="#2ECC71", activebackground="#27AE60", **button_style).pack(fill="x", pady=2)
        tk.Button(button_frame, text=f"🏏 Batters Stats Second Inning", command=lambda: show_window("windowbatterteam2"), bg="#9B59B6", activebackground="#8E44AD", **button_style).pack(fill="x", pady=2)

        tk.Button(button_frame, text="🏆 Close App", command=quit_idle, bg="#34495E", activebackground="#2C3E50", **button_style).pack(fill="x", pady=2)
        tk.Button(button_frame, text="🏆 Reset App", command=truncate_tables,bg="#34495E", activebackground="#2C3E50", **button_style).pack(fill="x", pady=2)
        
        # Footer
        footer_label = tk.Label(
            root1, text="Developed with ❤️ for cricket enthusiasts.", font=("Arial", 12), fg="#7F8C8D", bg="#f5f5f5"
        )
        footer_label.pack(side="bottom", pady=10)
        startwindow()        
#WINDOW CONTROL PANEL OPENED
control()


