# Find the minimal nucleotide from a range of sequence DNA
# Medium

```
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, 
which correspond to the types of successive nucleotides in the sequence. 

Each nucleotide has an impact factor, which is an integer.
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: 

What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained 
in the DNA sequence between positions P[K] and Q[K] (inclusive).

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
```
# Iterating << "in" operation
def solution(S, P, Q):
    
    impacts = []
    
    for i in range(len(P)):
        scope = S[P[i]:Q[i] + 1]
        if 'A' in scope:
            impacts.append(1)
            continue
        elif 'C' in scope:
            impacts.append(2)
            continue
        elif 'G' in scope:
            impacts.append(3)
            continue
        else:
            impacts.append(4)
        
    return impacts
