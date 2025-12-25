"""
Database initialization script for Link Tracker application.
Reads schema.sql and creates the database with the defined schema.
"""

import sqlite3
import os


def init_database(db_path='link_tracker.db', schema_path='schema.sql'):
    """
    Initialize the SQLite database using the schema file.
    
    Args:
        db_path (str): Path to the database file
        schema_path (str): Path to the schema SQL file
    """
    # Check if schema file exists
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    
    # Read the schema file
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Execute the schema SQL
    cursor.executescript(schema_sql)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print(f"Database initialized successfully: {db_path}")


if __name__ == '__main__':
    # Get database path from environment or use default
    db_path = os.environ.get('DATABASE', 'link_tracker.db')
    
    # Initialize the database
    init_database(db_path)
