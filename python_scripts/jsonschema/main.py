from jsonschema import Draft7Validator, FormatChecker

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "actionId": {
            "type": "string",
            "format": "date-time"
        },
        "status": {
            "type": "integer",
            "enum": [1, 4, 5]
        }
    },
    "required": ["actionId", "status"],
    "additionalProperties": False
}


def validate_request_body(body, schema):
    validator = Draft7Validator(schema, format_checker=FormatChecker)
    import pdb; pdb.set_trace()
    errors = list(validator.iter_errors(body, format=FormatChecker))

    if errors:
        return False, errors

    return True, list()


if __name__ == "__main__":
    body = {'actionId': '123123', 'status': False}
    response = validate_request_body(body, SCHEMA)
    print(response)
    # import pdb; pdb.set_trace()


####################
class JSONSchemaValidator():
    def __init__(self):
        self._schema = {}

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = Draft7Validator(value, format_checker=FormatChecker())

    def validate(self, data):
        errors = list(self.schema.iter_errors(data))

        if not errors:
            return True, []

        return False, self.__errors_to_list(errors)

    def __errors_to_list(self, errors):
        return list(map(lambda e: e.message, errors))
