from fastapi import FastAPI

app = FastAPI()

'''@app.get("/") — a decorator: it wraps the function below it with extra behavior. This one tells FastAPI "when someone sends an HTTP GET request to the root path /, run this function." GET means "give me data" — different from POST, which means "here's data, save it," which we'll use later for things like creating a user.'''

@app.get("/")
def read_root():
    return {"message" : "Hello World"}