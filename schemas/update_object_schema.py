update_object_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "price": {"type": "number"},
                "CPU model": {"type": "string"},
                "Hard disk size": {"type": "string"},
                "color": {"type": "string"}
            },
            "required": ["year", "price", "CPU model", "Hard disk size"]
        },
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["id", "name", "data", "updatedAt"]
}
