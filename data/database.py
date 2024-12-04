import sqlite3

class Database:
  def __init__(self, db_name):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()

  def create_tables(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Flight (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Starship (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT,
        altitude REAL,
        speed REAL,
        flight_id INTEGER,
        FOREIGN KEY (flight_id) REFERENCES Flight(id)
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Superheavy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT,
        altitude REAL,
        speed REAL,
        flight_id INTEGER,
        FOREIGN KEY (flight_id) REFERENCES Flight(id)
      )
    """)
    self.conn.commit()

  def insert_flight(self, name):
    self.cursor.execute("""
      INSERT INTO Flight (name)
      VALUES (?)
    """, (name,))
    self.conn.commit()
    return self.cursor.lastrowid

  def insert_starship_data(self, data):
    self.cursor.execute("""
      INSERT INTO Starship (time, altitude, speed, flight_id)
      VALUES (?, ?, ?, ?)
    """, (data["time"], data["altitude"], data["speed"], data["flight_id"]))
    self.conn.commit()

  def insert_superheavy_data(self, data):
    self.cursor.execute("""
      INSERT INTO Superheavy (time, altitude, speed, flight_id)
      VALUES (?, ?, ?, ?)
    """, (data["time"], data["altitude"], data["speed"], data["flight_id"]))
    self.conn.commit()

  def close(self):
    self.conn.close()
