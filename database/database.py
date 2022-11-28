import sqlite3 as sl
from datetime import datetime


def initialize_db():
    con = sl.connect('orders-executed.db')
    with con:
        con.execute(f"""
                            CREATE TABLE IF NOT EXISTS ARBITRAGE_MAIN_THREADS_EXCEPTION (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                Symbol TEXT,
                                Exception TEXT,
                                CancelOrder TEXT,
                                Time TEXT
                            );
                        """)

    con = sl.connect('orders-executed.db')
    with con:
        con.execute(f"""
                                CREATE TABLE IF NOT EXISTS ARBITRAGE_PROCESS_THREADS_EXCEPTION (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    Symbol TEXT,
                                    Exception TEXT,
                                    CancelOrder TEXT,
                                    Time TEXT
                                );
                            """)


def threads_exception_data(symbol, exception, order):
    con = sl.connect('orders-executed.db')
    sql = f'INSERT INTO ARBITRAGE_MAIN_THREADS_EXCEPTION (Symbol, Exception, CancelOrder, Time) values(?,?,?,?) '
    data = [
        (str(symbol)), (str(exception)), (str(order)), (str(datetime.now()))
    ]
    with con:
        con.execute(sql, data)
        con.commit()
