from collections import deque
from itertools import combinations

rows = open('task_2_input.txt', 'r').readlines()
grid = [list(row.strip()) for row in rows]

# 1 - find points of interest
start_pos = []
poi = dict()
keys_set = set()
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if tile not in ('#', '.'):
            if tile == '@':
                start_pos.append((x, y))
            else:
                if tile.islower():
                    poi[tile] = (x, y)
                    keys_set.add(tile)


def BFS(start_pos, target, grid):
    cols = len(grid[0])
    rows = len(grid)

    queue = deque()
    queue.append(
        {'pos': start_pos, 'on_path': [], 'steps': 0,}
    )

    visited = {start_pos}

    while queue:
        # current point
        cp = queue.popleft()

        for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cp['pos'][0] + x, cp['pos'][1] + y
            if (nx, ny) not in visited:
                if 0 <= nx and nx < cols and 0 <= ny and ny < rows:
                    tile = grid[ny][nx]

                    if tile == target:
                        return {'pos': (nx, ny), 'on_path': cp['on_path'][:], 'steps': cp['steps'] + 1}

                    # wall found
                    if tile == '#':
                        continue

                    if tile in ('.', '@'):
                        visited.add((nx, ny))
                        np = {
                            'pos': (nx, ny),
                            'on_path': cp['on_path'][:],
                            'steps': cp['steps'] + 1,
                        }
                        queue.append(np)
                        continue

                    # key found
                    if tile.islower():
                        visited.add((nx, ny))
                        np = {
                            'pos': (nx, ny),
                            'on_path': cp['on_path'][:] + [tile],
                            'steps': cp['steps'] + 1,
                        }
                        queue.append(np)
                        continue

                    # door found
                    if tile.isupper():

                        visited.add((nx, ny))

                        np = {
                            'pos': (nx, ny),
                            'on_path': cp['on_path'][:] + [tile],
                            'steps': cp['steps'] + 1,
                        }
                        queue.append(np)
                        continue

    return None


# 2 build path lookups
parts_lkp = {}
for num, p in enumerate(start_pos):
    shortest_path_lkp = {}
    for s, e in combinations(['@'] + list(poi.keys()), 2):
        if s == '@':
            pos = p
        else:
            pos = poi[s]

        path = BFS(pos, e, grid)
        if path:

            if s not in shortest_path_lkp:
                shortest_path_lkp[s] = {}

            shortest_path_lkp[s][e] = dict(path)

            if e not in shortest_path_lkp:
                shortest_path_lkp[e] = {}

            shortest_path_lkp[e][s] = dict(path)
            shortest_path_lkp[e][s]['on_path'] = list(reversed(shortest_path_lkp[e][s]['on_path']))

    parts_lkp[num] = shortest_path_lkp


# 3 find possible routes
queue = deque()
seen = set()
queue.append((tuple([(i, '@') for i in range(len(parts_lkp))]), tuple(), 0))
seen.add((tuple([(i, '@') for i in range(len(parts_lkp))]), tuple(), 0))


min_val = None

while queue:
    cp = queue.popleft()
    parts = cp[0]
    steps = cp[2]

    if min_val:
        if steps > min_val:
            continue

    for i, part in enumerate(parts):
        if not parts_lkp[part[0]]:
            continue

        paths_lkp = parts_lkp[part[0]][part[1]]
        for path in paths_lkp:
            keys = set(cp[1])

            # ignore start pos / entry and already visited keys
            if path != '@' and path not in keys:
                on_path = paths_lkp[path]['on_path']
                unobstructed = True

                for poi in on_path:
                    if poi.islower():
                        keys.add(poi)
                    if poi.isupper() and poi.lower() not in keys:
                        unobstructed = False
                        break

                if unobstructed:
                    keys.add(path)
                    if keys == keys_set:
                        s = steps + paths_lkp[path]['steps']
                        if not min_val:
                            min_val = s
                            print(min_val)
                        else:
                            if s < min_val:
                                min_val = s
                                print(min_val)

                    else:
                        np = tuple(list(parts[:i]) + [(part[0], path)] + list(parts[i + 1 :]))
                        pq = (np, tuple(sorted(list(keys))), steps + paths_lkp[path]['steps'])
                        if pq not in seen:
                            queue.appendleft(pq)
                            seen.add(pq)
