def flatten(_list):
    if not _list:
        return _list
    else:
        if type(_list[0]) != list:
            return [_list[0]] + flatten(_list[1:])
        else:
            return flatten(_list[0]) + flatten(_list[1:])
