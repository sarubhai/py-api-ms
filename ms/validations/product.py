from validator import Validator, validate, rules as R
import json

class ProductValidation():

    def create_update_request(request_data):
        rules = {
            'name': 'required|string',
            'uom': 'required|string',
            'quantity': 'required|integer|min:1',
            'price': 'required',
            'in_stock': 'required'
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