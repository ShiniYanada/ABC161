n, k = list(map(int, input().split()))
if n >= k:
  n = n % k
  if n >= k // 2 + 1:
    n = k - n
else:
  while(True):
    if n > abs(n-k):
      n = abs(n-k)
    else:
      break
print(n)
