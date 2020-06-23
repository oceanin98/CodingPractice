code = input()
result = "NO"
for c in code:
  if c in ['H','Q','9']:
    result = "YES"
    break
print(result)
