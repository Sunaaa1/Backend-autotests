create_object_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "createdAt": {"type": ["string", "null"]},  # если поле может отсутствовать
        "data": {"type": ["object", "null"]},
    },
    "required": ["id", "name"]
}