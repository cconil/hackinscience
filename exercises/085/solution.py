def sort_a_list(list):
    return(sorted(list, reverse=True))


def sort_by_mark(list):
    return(sorted(list, reverse=True))


def sort_by_name(list):
    from operator import itemgetter
    return(sorted(list, key=itemgetter(1)))
