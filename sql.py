import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("Karnataka_District_Crop_Details.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE Karnataka_District_Crop_Details (
    District_ID INT PRIMARY KEY,            
    District_Name VARCHAR(100),     
    Crop_Year INT,                  
    Crop_Name VARCHAR(100),         
    Area_Cultivated DECIMAL(10, 2), 
    Production_Tons DECIMAL(10, 2), 
    Irrigation_Type VARCHAR(50)     
);
"""
cursor.execute(table_info)

## Insert Some more records

# Insert records
records = [
    (1, 'Shimoga', 2023, 'Arecanut', 250.00, 300.00, 'Well'),
    (2, 'Dakshina Kannada', 2023, 'Coconut', 350.00, 800.00, 'Well'),
    (3, 'Mysore', 2023, 'Sugarcane', 700.00, 5000.00, 'Drip'),
    (4, 'Mandya', 2023, 'Cotton', 400.00, 1500.00, 'Canal'),
    (5, 'Hassan', 2023, 'Coffee', 600.00, 1100.00, 'Drip'),
    (6, 'Udupi', 2023, 'Rice', 450.00, 900.00, 'Canal'),
    (7, 'Bangalore Urban', 2023, 'Rice', 500.00, 1200.50, 'Canal'),
    (8, 'Tumkur', 2023, 'Groundnut', 350.00, 700.00, 'Drip'),
    (9, 'Chikmagalur', 2023, 'Tea', 150.00, 200.00, 'Drip'),
    (10, 'Chitradurga', 2023, 'Maize', 500.00, 1000.00, 'Canal'),
    (11, 'Davanagere', 2023, 'Paddy', 400.00, 950.00, 'Canal'),
    (12, 'Kodagu', 2023, 'Pepper', 100.00, 50.00, 'Drip'),
    (13, 'Bangalore Rural', 2023, 'Wheat', 300.00, 800.00, 'Well'),
    (14, 'Uttara Kannada', 2023, 'Cashew', 200.00, 300.00, 'Well'),
    (15, 'Raichur', 2023, 'Millet', 600.00, 1100.00, 'Canal'),
    (16, 'Koppal', 2023, 'Jowar', 450.00, 850.00, 'Canal'),
    (17, 'Gadag', 2023, 'Sunflower', 300.00, 500.00, 'Well'),
    (18, 'Belgaum', 2023, 'Sugarcane', 700.00, 5000.00, 'Drip'),
    (19, 'Bijapur', 2023, 'Grapes', 250.00, 900.00, 'Drip'),
    (20, 'Bagalkot', 2023, 'Onion', 350.00, 1200.00, 'Well'),
    (21, 'Bidar', 2023, 'Turmeric', 200.00, 600.00, 'Drip'),
    (22, 'Bellary', 2023, 'Chili', 450.00, 800.00, 'Canal'),
    (23, 'Dharwad', 2023, 'Tomato', 500.00, 1000.00, 'Well'),
    (24, 'Gulbarga', 2023, 'Bajra', 600.00, 1100.00, 'Canal'),
    (25, 'Kolar', 2023, 'Ragi', 350.00, 700.00, 'Well'),
    (26, 'Chikkaballapur', 2023, 'Mango', 150.00, 300.00, 'Drip'),
    (27, 'Yadgir', 2023, 'Banana', 400.00, 1200.00, 'Canal'),
    (28, 'Ramanagara', 2023, 'Papaya', 250.00, 500.00, 'Well'),
    (29, 'Haveri', 2023, 'Peanut', 300.00, 600.00, 'Drip'),
    (30, 'Karnataka Coastal', 2023, 'Coconut', 200.00, 400.00, 'Well')
]

# Insert each record
cursor.executemany('''INSERT INTO Karnataka_District_Crop_Details 
(District_ID, District_Name, Crop_Year, Crop_Name, Area_Cultivated, Production_Tons, Irrigation_Type) 
VALUES (?, ?, ?, ?, ?, ?, ?)''', records)

## Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from Karnataka_District_Crop_Details''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()