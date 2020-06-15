n, m = list(map(int, input().split()))
goods = list(map(int, input().split()))
flag = 1
limit = float(sum(goods)) / (4 * m)
for i in range(n - 1):
  for j in range(n - i - 1):
    if goods[j] <= goods[j+1]:
      tmp = goods[j]
      goods[j] = goods[j+1]
      goods[j+1] = tmp
for i in range(1, m):
  if goods[i] < limit:
    flag = 0
    break
if flag:
  print('Yes')
else:
  print('No')
