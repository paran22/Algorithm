def solution(wallpaper): 
    x, y = [], []
    for i, row in enumerate(wallpaper):
        for j, item in enumerate(row):
            if item == '#':
                x.append(i)
                y.append(j)
            
    return [min(x), min(y), max(x) + 1, max(y) + 1]