import sys

input = lambda: sys.stdin.readline().rstrip()


class Node:

  def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    self.parent = self

  def find(self):
    if self == self.parent:
      return self

    root = self

    while root != root.parent:
      root.parent = root.parent.parent
      root = root.parent

    self.parent = root
    return root

  def union(self, node):
    node.find().parent = self.find()

  def is_connect(self, node):
    diff_x = self.x - node.x
    diff_y = self.y - node.y
    distance = diff_x * diff_x + diff_y * diff_y
    sum_range = (self.r + node.r) ** 2
    return distance <= sum_range

  def is_group(self, node):
    return self.find() == node.find()


def solve_case():
  camp_count = int(input())

  camps = []

  for i in range(camp_count):
    x, y, r = map(int, input().split())
    camp = Node(x, y, r)
    camps.append(camp)
    for j in range(i):
      camp_outer = camps[j]
      if camp.is_connect(camp_outer):
        camp.union(camp_outer)

  camp_roots = set(camp.find() for camp in camps)
  print(len(camp_roots))


def solve():
  test_case_count = int(input())

  for _ in range(test_case_count):
    solve_case()


if __name__ == '__main__':
  solve()
