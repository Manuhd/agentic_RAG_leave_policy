def get_user_role(user_id: str) -> str:
    users = {
        "101": "employee",
        "102": "intern",
        "103": "manager"
    }
    return users.get(user_id, "employee")
