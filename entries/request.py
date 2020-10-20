from .models.entry import Entry
import sqlite3
import json


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            entry = Entry(row['id'], row['concept'], row['entry'],
                            row['date'], row['moodId'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
         SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                            data['date'], data['moodId'])

        return json.dumps(entry.__dict__)


def get_entry_by_word(word):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
         SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.entry LIKE ?
        """, ( '%' + word + '%', ))

        entries = []
        # Load the single result into memory
        dataset = db_cursor.fetchall()

        # Create an animal instance from the current row
        for row in dataset:

            entry = Entry(row['id'], row['concept'], row['entry'],
                            row['date'], row['moodId'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
