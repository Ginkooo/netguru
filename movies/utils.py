def filter_movie_details(details, key, value):
    if key not in details:
        return False

    if value[0] in details[key]:
        return True


def is_truthy(value):
    return str(value).lower() in '1 true yes'.split()
