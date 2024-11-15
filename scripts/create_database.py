import mysql.connector
from mysql.connector import Error

# Database connection
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "bookstore_db"
DB_USER = "root"
DB_PASSWORD = "DataEngineering"

try:
    # MySQL server
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )
    if conn.is_connected():
        print("Connected to MySQL Server")

    cursor = conn.cursor()

    # Database
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' created or already exists.")

    # Use
    cursor.execute(f"USE {DB_NAME}")

    # Create the Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            subscribed TINYINT DEFAULT 0
        )
    ''')
    print("Table 'Users' created.")

    # Create the Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
    ''')
    print("Table 'Books' created.")

    # Create the Purchases table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Purchases (
            purchase_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NULL,
            email VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            book_id INT NOT NULL,
            processed TINYINT DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE SET NULL,
            FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
        )
    ''')
    print("Table 'Purchases' created.")

    # Sample Data into Books
    books = [
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell"),
        ("Pride and Prejudice", "Jane Austen"),
        ("The Catcher in the Rye", "J.D. Salinger")
    ]

    cursor.executemany('INSERT INTO Books (title, author) VALUES (%s, %s)', books)
    print("Sample data inserted into 'Books' table.")

    # Debug
    cursor.execute('SELECT * FROM Books')
    for row in cursor.fetchall():
        print(row)

    # Sample Data into Users
    users = [
        ("Daniel Brown", "daniel.brown@example.com", 1)  # Existing user
    ]
    cursor.executemany('INSERT INTO Users (name, email, subscribed) VALUES (%s, %s, %s)', users)
    print("Sample data inserted into 'Users' table.")

    # Sample Data into Purchases
    purchases = [
        (None, "b23cm1015@iitj.ac.in", "Divyansh Maheshwari", 1, 0),
        (None, "b23es1021@iitj.ac.in", "Madhav", 2, 0),
        (None, "b23cs1038@iitj.ac.in", "Mohit Meemrauth", 3, 0),
        (1, "b22ai007@iitj.ac.in", "Anushk Gupta", 4, 0),
        (None, "eryashrajchaturvedi@gmail.com", "Emily Davis", 5, 0),
        (None, "b22ai059@iitj.ac.in", "Yashraj Chaturvedi", 3, 0)
    ]

    cursor.executemany(
        'INSERT INTO Purchases (user_id, email, name, book_id, processed) VALUES (%s, %s, %s, %s, %s)', 
        purchases
    )
    print("Sample data inserted into 'Purchases' table.")

    # Commit the transaction
    conn.commit()
    print("Database setup complete.")

except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
