import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "Batmin",
    "password": "Admin123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    

    db = mysql.connector.connect(**config)

    cursor = db.cursor()


    cursor.execute("SELECT team_id, team_name, mascot FROM team")

   
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
  
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

   
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

   
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

  
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally: 
    db.close()