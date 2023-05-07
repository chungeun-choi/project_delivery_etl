import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")
import uvicorn
from app.core.server import app
from app.core.config import Settings


def main():
    uvicorn.run(
        app="core.server:app",
        host=Settings.SERVER_HOST,
        port=Settings.SERVER_PORT,
        loop="auto",
        # workers=2,
    )


if __name__ == "__main__":
    main()
