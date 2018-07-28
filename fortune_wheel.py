def winner(candidates):
    if len(candidates) != 3:
        return False
    for k in candidates:
        if len(k) < 2:
            return False
        if len(k['scores']) < 1 or len(k['scores']) > 2:
            return False
        if len(k['scores']) == 2:
            if k['scores'][0] > 100 or k['scores'][1] > 100:
                return False
    big = 0
    winner = False
    for c in candidates:
        current_total = sum(c['scores'])
        if current_total % 5 != 0:
            return False
        if current_total > big and current_total <= 100:
            big = current_total
            winner = c['name']
    return winner
