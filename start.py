import uvicorn
from os import getenv
open_port = getenv("PORT")

if open_port is None:
    open_port = 8000

open_port = int(open_port)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=open_port,
        # env_file="./.env",/
        reload=True
    )
