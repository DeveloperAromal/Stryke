from core.router import Router
from core.server import Server
from middleware.reject_malicious_scripts import safe

router = Router()

@safe
@router.get("/")
def root():
    return "Hello root user"

@router.get("/about")
def about():
    return "This is the about page"

app = Server(router)

app.run()