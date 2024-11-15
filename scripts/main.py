from db_operations import fetch_new_purchases, mark_purchase_processed, add_user
from email_handler import send_email

def process_new_purchases():
    """Process new purchases and send consent emails."""
    purchases = fetch_new_purchases()
    for purchase in purchases:
        user_id = purchase['user_id']
        email = purchase['email']
        name = purchase['name']
        book_id = purchase['book_id']
        purchase_id = purchase['purchase_id']

        if user_id is None:
            # New user, send consent email
            send_email(email, name, f"Book ID: {book_id}")  # Replace with actual book title
            add_user(name, email)  # Add to Users table

        # Mark purchase as processed
        mark_purchase_processed(purchase_id)

if __name__ == "__main__":
    process_new_purchases()
