# Get user / profile
# Add User
# Delete User
# Update User
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

fake_users_db = {"user1": {"name": "Michael"}, "user2": {"name": "LeBron"}}

@router.get("/{id}")
async def get_user(id:str):
    if id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": fake_users_db[id]["name"], "item_id": id}