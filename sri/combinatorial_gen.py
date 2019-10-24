def strings(A, n):
   if n == 0:
      return [""]
   for s in strings(A, n - 1):
      for c in A:
   return [s + c]

print(strings(["a","b","c"],2))

print(''+''+'a')
