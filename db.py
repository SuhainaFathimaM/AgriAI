import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("market.db")
cursor = conn.cursor()

# Load Market Data
# market_df = pd.read_csv("market_researcher_dataset.csv")
# market_df.to_sql("MarketData", conn, if_exists="replace", index=False)

# # Load Farm Data
farm_df = pd.read_csv("farmer_advisor_dataset.csv")
farm_df.to_sql("FarmData", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Data successfully stored in SQLite!")


# import sqlite3

# # Create a connection to a new SQLite database file
# conn = sqlite3.connect("mydatabase.db")

# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()

# # Create a sample table
# cursor.execute('''
#         CREATE TABLE FarmData (
#     Farm_ID INTEGER PRIMARY KEY,
#     Soil_pH REAL,
#     Soil_Moisture REAL,
#     Temperature_C REAL,
#     Rainfall_mm REAL,
#     Crop_Type TEXT,
#     Fertilizer_Usage_kg REAL,
#     Pesticide_Usage_kg REAL,
#     Crop_Yield_ton REAL,
#     Sustainability_Score REAL
# )

               

# ''')

# # Commit and close
# conn.commit()
# conn.close()

# print("Database and table created successfully!")
