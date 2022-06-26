from psycopg2 import Error, connect
from os import environ


try:
    user = environ.get('DB_USER')
    password = environ.get('DB_PASS')

    # подключаюсь к существующей БД
    with connect(user=user,
                 password=password,
                 host='127.0.0.1',
                 port='5432',
                 database='postgres_db') as connection:

        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS products")
        cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                   type TEXT NOT NULL,
                   base_costs_per_month INTEGER DEFAULT NULL,
                   consumption_costs INTEGER DEFAULT NULL,
                   tariff_price INTEGER DEFAULT NULL,
                   tariff_consumption INTEGER DEFAULT NULL,
                   additional_costs INTEGER DEFAULT NULL)""")

        print("Таблица успешно создана в PostgreSQL")

        # вношу в таблицу три записи тарифа basic
        cursor.execute("INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ('basic', 4, 22)")
        cursor.execute("INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ('basic', 5, 25)")
        cursor.execute("INSERT INTO products (type, base_costs_per_month, consumption_costs) VALUES ('basic', 3, 20)")

        # вношу в таблицу три записи тарифа package
        cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                                         VALUES ('package', 800, 4000, 30)""")
        cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                                         VALUES ('package', 900, 4500, 23)""")
        cursor.execute("""INSERT INTO products (type, tariff_price, tariff_consumption, additional_costs)
                                         VALUES ('package', 850, 5500, 29)""")

        connection.commit()
        print('Изменения в таблицу успешно внесены')

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
