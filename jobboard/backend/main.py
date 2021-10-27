from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
from apis.version1.route_users import router


def create_tables():

    Base.metadata.create_all(bind=engine)


def start_application():

    app1 = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    app1.include_router(router)
    return app1


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
