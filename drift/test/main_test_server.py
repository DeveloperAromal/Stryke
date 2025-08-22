from core.router import Router
from core.server import Server



router = Router()

@router.get("/")
def root():
    return "Hello root user"



app = Server(router)


app.run("GET", "/")
