from db_connection import get_connection

def fetch_new_purchases():
    """Fetch unprocessed purchases from the database."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Purchases WHERE processed = 0")
        purchases = cursor.fetchall()
        conn.close()
        return purchases
    return []

def mark_purchase_processed(purchase_id):
    """Mark a purchase as processed."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Purchases SET processed = 1 WHERE purchase_id = %s", (purchase_id,))
        conn.commit()
        conn.close()

def add_user(name, email):
    """Add a new user to the Users table."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (name, email, subscribed) VALUES (%s, %s, 0)", (name, email))
        conn.commit()
        conn.close()