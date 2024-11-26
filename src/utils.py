def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token in "*/+-"
