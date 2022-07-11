from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_fastapi_app(endpoints):

    # Función para crear una aplicación de fastapi
    
    app = FastAPI(app = FastAPI(
        title="Orders distribution API",
        description="a REST API using python and MongoDB",
        version="1.0",
        root_path="/api/v1",
        debug=True
))

    #configurar según se requiera
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    
    for endpoint in endpoints:
        app.include_router(endpoint)

    return app