import sqlite3 as db


with db.connect('base.db', check_same_thread=False) as connection:
    cursor = connection.cursor()

    # создаю таблицу в БД
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
        type TEXT NOT NULL,
        base_costs_per_month INTEGER DEFAULT NULL,
        consumption_costs INTEGER DEFAULT NULL,
        tariff_price INTEGER DEFAULT NULL,
        tariff_consumption INTEGER DEFAULT NULL,
        additional_costs INTEGER DEFAULT NULL
    )""")

    # вношу в таблицу три записи тарифа basic
    cursor.execute('INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ("basic", 4, 22)')
    cursor.execute('INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ("basic", 5, 25)')
    cursor.execute('INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ("basic", 3, 20)')
    # вношу в таблицу три записи тарифа basic
    cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                      VALUES ("package", 800, 4000, 30)""")
    cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                      VALUES ("package", 900, 4500, 23)""")
    cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                      VALUES ("package", 850, 5000, 27)""")
