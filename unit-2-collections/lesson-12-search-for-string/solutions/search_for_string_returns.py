def search_for_string(a_list, search_term):
    for item in a_list:
        if item == search_term:
            return 'string found!'
    return 'string not found'
