def read_ints():
  temp = input().split()
  temp = [int(i) for i in temp]
  return temp

def satisfiable(clauses):
  # if clauses is an empty list, all satisfied
  #print("CLAUSES:",clauses)
  if not clauses:
    return "YES"
  # if there is an empty clause, failure 
  for clause in clauses:
    if not clause:
      return "NO"
  # choose a literal amongst remaining literals 
  literal = abs(clauses[0][0])
  #print("LITERAL: {}".format(literal))
  pclauses = [clause[:] for clause in clauses if literal not in clause]
  for clause in pclauses:
    to_pop = []
    for i,c in enumerate(clause):
      if c == -literal:
        to_pop.append(i)
    for i in to_pop:
      clause.pop(i)
  #print("PCLAUSE:", pclauses)
  if "YES" == satisfiable(pclauses):
    return "YES"


  #print("Going over to Negative checking...")  
  #print("CLAUSES:",clauses)
  #print("LITERAL: {}".format(-literal))
  nclauses = [clause[:] for clause in clauses if -literal not in clause]
  for clause in nclauses:
    to_pop = []
    for i,c in enumerate(clause):
      if c == literal:
        to_pop.append(i)
    for i in to_pop:
      clause.pop(i)
  #print("NCLAUSE:", nclauses)
  if "YES" == satisfiable(nclauses):
    return "YES"
  return "NO"
  

tests = int(input())

for _ in range(tests):
  n,k = read_ints()
  
  clauses = []
  for _ in range(k):
    clauses.append(read_ints())
  
  result = satisfiable(clauses)
  print(result)
