import time
import pickle

coins = [1, 5, 10, 25, 50, 100]
target = int(1e20)
step = int(1e7)
# coins = [1,2, 10]
# target = 3

def iter(table, coins, target, start, end):
  t_start = time.time()
  L = max(coins)
  n_coins = len(coins)
  end = min(target+1, end)
  for i in range(start, end):
    row = i % L
    curr = [0] * n_coins
    for j, coin in enumerate(coins):
      if i >= coin:
        curr[j] = table[(i-coin) % L][j]

    table[row][n_coins-1] = curr[n_coins-1]
    for j in range(n_coins-2, -1, -1):
      table[row][j] = table[row][j+1] + curr[j]

  i = end - 1
  fname = "coins.p".format(i)
  pickle.dump({"i": i, "table": table}, open( fname, "wb" ) )
  duration = time.time() - t_start
  print(i, ":", table[(i)%L][0], round(10*duration)/10, flush=True)

  return table

def initialize(coins, target):
  L = max(coins)
  n_coins = len(coins)
  table = []
  for i in range(L+1):
    curr = [0]*n_coins
    table.append(curr)
  for i in range(n_coins):
    table[0][i] = 1
  return table

def method(coins, target, pickle_file=None):
  if pickle_file:
    p = pickle.load( open( pickle_file, "rb" ) )
    table = p['table']
    i = p['i'] + 1
  else:
    table = initialize(coins, target)
    i = 1

  while i < target + 1:
    table = iter(table, coins, target, i, i+step)
    i += step

  L = max(coins)
  print(table[target % L][0])

# method(coins, target)
method(coins, target, "coins.p")
