counter1 = counter2 = counter3 = 0
memo = [None] * 100

# Fib 
def fib1(n):
    global counter1
    counter1 += 1
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Fib recursivo (con memoization usar listas o diccionarios) - Top Down method
def fib2(n):
    global counter2
    counter2 += 1   
    if memo[n]:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


# Fib iterativo - Bottom Up method
def fib3(n):
    global counter3
    counter3 += 1   
    fib_list = [0, 1]
    for index in range(2, n + 1):
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]

if __name__ == "__main__":
    n = 10
    print(f"Termino {n}: {fib1(n)}")
    print(f"Se hicieron: {} llamados a la función recursiva")
    print("*"*10)
    print(f"Termino {n}: {fib2(n)}")
    print(f"Se hicieron: {} llamados a la función recursiva optimizada")
    print("*"*10)
    print(f"Termino {n}: {fib3(n)}")
    print(f"Se hicieron: {} llamados a la función iterativa")