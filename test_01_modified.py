
import queue
from datetime import datetime, timedelta
import time
import uuid
import random
from collections import deque
from threading import Thread

class OrdersManager(Thread):
    __orders = queue.LifoQueue()
    __orders_processed = 0
    __last_printed_log = datetime.now()
    __orders_quantity = 0

    def __init__(self) -> None:
        Thread.__init__(self)
        self.__generate_fake_orders(quantity=1_000)

    def __generate_fake_orders(self, quantity):
        self.__log(f"Generating fake orders")
        [self.__orders.put((uuid.uuid4(), x)) for x in range(quantity)]
        
        self.__orders_quantity = (self.__orders).qsize()
        self.__log(f"{self.__orders_quantity} generated...")


    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order
        
        self.__log(
            message=f"Order [{id}] {number} was successfully prosecuted."
        )

        time.sleep(random.uniform(0, 1))

    def process_orders(self):
        
        
        self.__fake_save_on_db(order= self.__orders.get())
        

    def run(self):
        """"""
        
        while self.__orders_processed < self.__orders_quantity:
            t1 = Thread(target=self.process_orders)
            
            self.__orders_processed+=1
            t1.start()
            
            if datetime.now() > self.__last_printed_log or self.__orders_processed == self.__orders_quantity:
                self.__last_printed_log = datetime.now() + timedelta(seconds=0.01)
                self.__log(
                    message=f"Total orders executed: {self.__orders_processed}/{self.__orders_quantity}")

        t1.join()
#
#
# ---

orders_manager = OrdersManager()

start_time = time.time()

orders_manager.run()

delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")