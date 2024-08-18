def solution(wallpaper): 
    min_x, min_y, max_x, max_y = 51, 51, 0, 0
    for i, row in enumerate(wallpaper):
        for j, item in enumerate(row):
            if item == '#':
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i + 1)
                max_y = max(max_y, j + 1)
            
    return [min_x, min_y, max_x, max_y]