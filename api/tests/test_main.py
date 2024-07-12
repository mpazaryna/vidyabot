# File: api/src/main.py

from fastapi import FastAPI, HTTPException

from .data.user_data import get_user_data

app = FastAPI()


@app.get("/")
async def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the User API"}


@app.get("/users")
async def read_users():
    """Retrieve all users."""
    try:
        users = get_user_data()
        return users
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while retrieving user data"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
