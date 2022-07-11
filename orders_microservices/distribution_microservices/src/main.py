from frameworks.http.fastapi import create_fastapi_app
from frameworks.db.mongo import PymongoClient
from orders.http.orders_endpoints import create_orders_endpoints
from orders.repositories.mongo_orders_repositories import PyMongoOrdersRepository


from orders.usecases.manage_orders_usecases import ManageOrdersUseCases

mongo_client = PymongoClient().client

py_mongo_orders_repository = PyMongoOrdersRepository(mongo_client)

manage_orders_usecase = ManageOrdersUseCases(py_mongo_orders_repository)

#crea los endpoints de las ordenes
orders = [
    create_orders_endpoints(manage_orders_usecase)
    ]

app= create_fastapi_app(orders)