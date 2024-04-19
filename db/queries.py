class Queries:
    CREATE_FEEDBACK_TABLE = """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            date INTEGER,
            food TEXT,
            cleanliess INTEGER,
            comments TEXT
        )
    """