import sys

input = lambda: sys.stdin.readline().rstrip()


def find(node_index, node_parent):
  while node_index != node_parent[node_index]:
    node_parent[node_index] = node_parent[node_parent[node_index]]
    node_index = node_parent[node_index]
  return node_parent[node_index]


def union(node_index, node_outer_index, node_parent):
  if find(node_index, node_parent) == find(node_outer_index, node_parent):
    return

  node_root = find(node_index, node_parent)
  node_outer_root = find(node_outer_index, node_parent)

  if node_root < node_outer_root:
    node_parent[node_outer_root] = node_parent[node_root]
  else:
    node_parent[node_root] = node_parent[node_outer_root]


def is_connect(coordinate, coordinate_outer):
  x, y, r = coordinate
  x_outer, y_outer, r_outer = coordinate_outer
  diff_x = x - x_outer
  diff_y = y - y_outer
  distance = diff_x * diff_x + diff_y * diff_y
  sum_range = (r + r_outer)
  return distance <= sum_range * sum_range


def solve_case():
  camp_count = int(input())

  node_parent = [i for i in range(camp_count)]
  node_coordinate = []

  for node in range(camp_count):
    node_coordinate.append(tuple(map(int, input().split())))
    for node_outer in range(node):
      if is_connect(node_coordinate[node], node_coordinate[node_outer]):
        union(node, node_outer, node_parent)

  camp_roots = set(find(i, node_parent) for i in node_parent)
  print(len(camp_roots))


def solve():
  test_case_count = int(input())

  for _ in range(test_case_count):
    solve_case()


if __name__ == '__main__':
  solve()
