import time
import pickle

coins = [1, 5, 10, 25, 50, 100]
target = int(1e20)
step = int(1e8)
# coins = [1,2, 10]
# target = 3

def iter(table, coins, target, start, end):
  t_start = time.time()
  L = max(coins)
  n_coins = len(coins)
  end = min(target+coins[1], end)
  for i in range(start, end, coins[1]):
    row = i % L
    for j in range(1, n_coins):
      shift = (i-coins[j])%L
      table[row][j] = table[row][j-1] + table[shift][j]

  i = end - coins[1]
  fname = "coins.p".format(i)
  pickle.dump({"i": i, "table": table}, open( fname, "wb" ) )
  duration = time.time() - t_start
  print(i, ":", table[i%L][-1], round(10*duration)/10, flush=True)
  return table

def initialize(coins, target):
  L = max(coins)
  n_coins = len(coins)
  table = []
  for i in range(L+1):
    curr = [0]*n_coins
    curr[0] = 1
    table.append(curr)
  for i in range(n_coins):
    table[0][i] = 1
  return table

def method(coins, target, pickle_file=None):
  coins = sorted(coins)
  if pickle_file:
    p = pickle.load( open( pickle_file, "rb" ) )
    table = p['table']
    i = p['i'] + coins[1]
  else:
    table = initialize(coins, target)
    i = coins[1]

  while i < target + 1:
    table = iter(table, coins, target, i, i+step)
    i += step

  L = max(coins)
  print(table[target % L][-1])

# method(coins, target)
method(coins, target, "coins.p")
