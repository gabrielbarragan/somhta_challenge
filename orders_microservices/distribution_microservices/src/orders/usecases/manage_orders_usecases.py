

class ManageOrdersUseCases:
    def __init__(self, orders_repository):
        self.orders_repository = orders_repository

    async def get_orders(self,url_request, page_num ):
        
        return await self.orders_repository.get_orders(url_request, page_num)

