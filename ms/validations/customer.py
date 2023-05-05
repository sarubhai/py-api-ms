from validator import Validator, validate, rules as R
import json

class CustomerValidation():

    def create_update_request(request_data):
        rules = {
            'name': 'required|string',
            'dob': 'required|date',
            'address': 'required|string'
        }

        # validation
        result, validated_data, errors = validate(request_data, rules, True)

        # Result
        if result:
            invalid = False
            data = validated_data
        else:
            invalid = True
            data = errors

        return json.dumps({'invalid':invalid, 'data':data})