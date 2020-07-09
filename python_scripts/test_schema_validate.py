from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "quote": {
            "type": "string"
        },
        "status": {
            "type": "integer"
        },
        "extra": {
            "type": "integer"
        }
    },
    "oneOf": [
        {"required": ["extra", "status"]},
        {"required": ["extra", "quote"]}
    ]
}
alert = {
    "quote": '2',
    "adicionar": "oi"
}
response = validate(alert, schema)
# import pdb; pdb.set_trace()
print(response)
