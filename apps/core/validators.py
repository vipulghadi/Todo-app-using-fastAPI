def handle_validation_errors(e):
    errors_list = []
    for err in e.errors():
        if "," in err["msg"]:
            errors_list.append(err["msg"].split(",")[1].strip())
        else:
            errors_list.append(err["msg"])
    return errors_list
