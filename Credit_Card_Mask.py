def maskify(cc):
    masked = len(cc)-4
    if len(cc) > 4:
        result = '#' * masked + cc[-4:]
        return result
    else:
        return cc