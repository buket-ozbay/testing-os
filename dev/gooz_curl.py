import urequests

def get(url,_type="text"):
    response = urequests.get(url)
    if _type == "text":
        return response.text
    elif _type == "json":
        return response.json()