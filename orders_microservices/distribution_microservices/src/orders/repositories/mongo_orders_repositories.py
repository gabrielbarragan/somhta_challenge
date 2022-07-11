

from fastapi.responses import JSONResponse

from orders.entities.orders import  ordersEntity, serializeList


class PyMongoOrdersRepository():
    def __init__(self, mongodb_client):

        self.client = mongodb_client
        self.database = mongodb_client.db_name
        self.collection_name = mongodb_client.collection

    async def get_orders(self, url_request, page_num=1):

        page_size=20
        skips = page_size * (page_num - 1)
        orders = self.client["orders"]["orders_collection"].find().skip(skips).limit(page_size)
        orders= ordersEntity(serializeList(orders))
        total_results= len(orders)
        

        url_request = url_request
        str_url_request = str(url_request).split("=")[0]

        next_page= f'{str_url_request}={page_num+1}'
        prev_page= ""

        if page_num > 1:
            prev_page= f'{str_url_request}={page_num-1}'
        
        if page_num >1 and len(ordersEntity(serializeList(self.client["orders"]["orders_collection"].find().skip(skips+page_size).limit(page_size)))) < 1:

            next_page = ""
        if page_num >1 and len(ordersEntity(serializeList(self.client["orders"]["orders_collection"].find().skip(skips-page_size).limit(page_size)))) < 1: 

            prev_page =""
        
        page_info={
            "pageResults": total_results,
            "currentPage":str(page_num),
            "nextPage":next_page,
            "previous":prev_page,
        }
        data= { 
                "data": orders,
                "page_info": page_info}

        return JSONResponse(content=data, status_code=200)