import time

from arbitrage.arbitrage import arbitrage as main_function
from database.database import initialize_db, threads_exception_data

if __name__ == "__main__":
    initialize_db()
    # counters_obj = Counters()
    # indicators_obj = Indicator()
    # trading_bot_obj = TradingBot()
    # symbol_obj = Symbols(current_index_symbol=0, current_index_time_frame=0)
    # db = DB()
    while True:
        try:
            main_function()
        except Exception as e:
            print("Main Thread 1st Level", e)
            threads_exception_data(symbol="Main Thread 1st Level", exception=e, order="null")
            try:
                time.sleep(20)
            except Exception as e:
                print("Main Thread 2nd Level", e)
                threads_exception_data(symbol="Main Thread 2nd Level", exception=e, order="null")
