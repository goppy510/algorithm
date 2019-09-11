N = int(input())
l = list(map(int, input().split()))

for i, n in enumerate(l, start=1):
  print(l)
  v = l[i]
  j = i - 1
  while j >=0 and l[j] > v:
    l[j+1] = l[j]
    j -= 1
  l[j+1] = v