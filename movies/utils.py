def filter_movie_details(details, key, value):
    if key not in details:
        return False

    if value[0] in details[key]:
        return True
