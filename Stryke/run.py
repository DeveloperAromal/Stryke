from core.router import Router
from core.server import Server
from middleware.reject_malicious_scripts import safe
import json

router = Router()

@safe
@router.get("/")
def root():
    return "Hello root user"

@router.get("/about")
def about():
    return "This is the about page"



@router.post("/hack")
def hack(target):
    print(target)
    return f"Hacking {target} was successful!"


app = Server(router)

app.run()