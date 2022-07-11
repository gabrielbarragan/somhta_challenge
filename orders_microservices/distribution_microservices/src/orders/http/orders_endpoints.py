

from fastapi import APIRouter, Request

from fastapi.responses import JSONResponse

from orders.entities.orders import OrdersModel


def create_orders_endpoints(manage_orders_usecases):
    """Endpoints para orders Sólo se encarga de recibir las llamadas HTTP y le entrega los datos relevantes a los casos de uso correspondientes. Esta capa no contiene lógica de negocio, sólo lo necesario para recibir y entregar respuestas válidas al mundo exterior."""

    orders = APIRouter(prefix="/api/v1")
    url_orders = "/orders/"
    
    @orders.get(url_orders, response_description="List all movies", response_model=OrdersModel, )
    async def get_orders(request: Request, page_num: int=1 ):
        #si la petición solicita la página 0 se le retorna esto
        if page_num < 1: 
            message = f"Page does not exists"
            http_code = 404

            response= {
                "detail": 
                {
                    "page_num":page_num,
                    "message": message
                }
            }
            return JSONResponse(content= response, status_code=http_code)
        else:
            url_request = request.url

            data = manage_orders_usecases.get_orders(url_request, page_num)
            
            return await data

    return orders

