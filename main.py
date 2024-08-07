from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def main_page(name: str):
    return f'Hello {name}'
