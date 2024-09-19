import sqlite3
from datetime import datetime


def create_table():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user1_id INTEGER,
                user2_id INTEGER,
                sender_id INTEGER,
                message TEXT,
                timestamp DATETIME
                )''')
    conn.commit()
    conn.close()


def load_chat_history(user1_id, user2_id):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''SELECT sender_id, message, timestamp 
                 FROM chat_history 
                 WHERE (user1_id = ? AND user2_id = ?) OR (user1_id = ? AND user2_id = ?) 
                 ORDER BY timestamp''',
              (user1_id, user2_id, user2_id, user1_id))
    chats = c.fetchall()
    conn.close()
    return chats


def send_message(user1_id, user2_id, sender_id, message):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    timestamp = datetime.now()
    c.execute('''INSERT INTO chat_history (user1_id, user2_id, sender_id, message, timestamp) 
                 VALUES (?, ?, ?, ?, ?)''',
              (user1_id, user2_id, sender_id, message, timestamp))
    conn.commit()
    conn.close()


def display_chat_history(chats, current_user_id):
    for chat in chats:
        sender = "אתה" if chat[0] == current_user_id else f"משתמש {chat[0]}"
        print(f"{sender} ({chat[2]}): {chat[1]}")


def handle_chat(user1_id, user2_id):
    create_table()

    chats = load_chat_history(user1_id, user2_id)

    print("\nשיחות קודמות בין המשתמשים:")
    display_chat_history(chats, user1_id)

    print("\nהתחל/י לשוחח עם משתמש", user2_id)
    while True:
        message = input("הזן הודעה (או 'יציאה' כדי לצאת): ")
        if message.lower() == 'יציאה':
            break
        send_message(user1_id, user2_id, user1_id, message)
        chats = load_chat_history(user1_id, user2_id)
        print("\nשיחה מעודכנת:")
        display_chat_history(chats, user1_id)


if __name__ == "__main__":
    current_user_id = int(input("הזן את ה-ID שלך: "))
    other_user_id = int(input("הזן את ה-ID של המשתמש האחר: "))

    handle_chat(current_user_id, other_user_id)
