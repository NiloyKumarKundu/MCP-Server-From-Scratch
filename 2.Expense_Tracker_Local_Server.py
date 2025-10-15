from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'expense.db')
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), 'categories.json')

mcp = FastMCP(name="Expense Tracker")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT  DEFAULT ''
            )
        ''')
        
init_db()


@mcp.tool
def add_expense(date: str, amount: float, category: str, subcategory: str = '', note: str = '') -> dict:
    """Add a new expense to the database"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('''
            INSERT INTO expenses (date, amount, category, subcategory, note)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, amount, category, subcategory, note))
        conn.commit()
        return {"status": "success", "id": cursor.lastrowid}
    

@mcp.tool
def list_expenses(start_date: str, end_date: str):
    """List all expenses"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('''
            SELECT * FROM expenses 
            WHERE date BETWEEN ? AND ? 
            ORDER BY id ASC
        ''', (start_date, end_date))
        cols = [column[0] for column in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]
    

@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    # Read fresh each time so you can edit the file without restarting the server
    with open(CATEGORIES_PATH, "r") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run()