from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()


class App():
    @staticmethod
    def get_jobs():
        return {"data": "Hello World"}


router = APIRouter()
router.add_api_route('/api/v2/jobs',
                     endpoint = App().get_jobs, methods=["GET"])
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)