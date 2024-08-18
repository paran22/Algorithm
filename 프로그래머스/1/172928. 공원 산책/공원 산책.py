def solution(park, routes):
    W, H = len(park), len(park[0])
    directions = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}
    location = [0, 0]
    
    for i in range(W):
        for j in range(H):
            if park[i][j] == 'S':
                location = [i, j]
                break
            
    for route in routes:
        direction, length_str = route.split(' ')
        length = int(length_str)
        dx, dy = directions[direction]
        x, y = location
        temp_x, temp_y = x, y
        for _ in range(length):            
            nx, ny = dx + temp_x, dy + temp_y
            if  0 <= nx < W and 0 <= ny < H and park[nx][ny] != 'X':
                temp_x, temp_y = nx, ny
        if temp_x == x + length * dx and temp_y ==  y + length * dy:
            location = [temp_x, temp_y]
        
    return location