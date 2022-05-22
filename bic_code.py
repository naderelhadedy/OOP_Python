
def create_bic_code(name, number, year=0):
    return f"{name[:2]}.{number}.{year}"
