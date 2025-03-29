
def string_proces(response):
    response = response.replace("\n", "")
    first_bracket = response.find("{")
    last_bracket = response.rfind("}")
    return response[first_bracket:last_bracket+1]
