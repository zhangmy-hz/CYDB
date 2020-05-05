def wrap_json_response(data=None, code=None, message=None):
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data is not None:
        response['data'] = data
    response['result_code'] = code
    response['message'] = message
    return response