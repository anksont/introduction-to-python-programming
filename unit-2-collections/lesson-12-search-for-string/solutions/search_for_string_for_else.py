def search_for_string(a_list, search_term):
    for item in a_list:
        if item == search_term:
            break
    else:
        return 'string not found'
    return 'string found!'
