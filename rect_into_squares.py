def sqInRect(l, w):
    sq = []
    max_area = l * w
    total = 0
    if l == w:
        return None
    while max_area - total > 3:
      sq.append(min(l, w))
      if l > w:
        l = l - w
        total += w * w
      else:
        w = w - l
        total += l * l

    if total!=max_area:
        if (max_area-total)%3 == 0:
          sq.append(1)
          sq.append(1)
          sq.append(1)
        if (max_area-total)%2 == 0:
          sq.append(1)
          sq.append(1)
    return sq
