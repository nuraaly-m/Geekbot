class Queries:
    CREATE_FEEDBACK_TABLE = """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            date INTEGER,
            food TEXT,
            cleanliness INTEGER,
            comments TEXT
        )
    """

    CREATE_KINDS_TABLE = """
        CREATE TABLE IF NOT EXISTS kinds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """

    CREATE_PRODUCTS_TABLE = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            picture TEXT,
            kind_id INTEGER,
            FOREIGN KEY (kind_id) REFERENCES kinds(id)
        )
    """

    DROP_KINDS_TABLE = "DROP TABLE IF EXISTS kinds"
    DROP_PRODUCTS_TABLE = "DROP TABLE IF EXISTS products"
    POPULATE_KINDS = """
        INSERT INTO kinds (name) VALUES ('горячие блюда'),
         ('холодные блюда'), ('салаты'), ('напитки')
    """
    POPULATE_PRODUCTS = """
        INSERT INTO products (name, price, picture, kind_id) 
        VALUES ('lagman', 320, 'images/food1.jpeg', 1),
        ('holodec', 320, 'images/food2.jpeg', 2),
        ('salad', 320, 'images/food3.jpeg', 3),
        ('watermelon', 320, 'images/food4.jpeg', 4)
    """


