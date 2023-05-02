#uantos números perfectos hay entre 1 y 1000 y cuales son los numeros comprendidos 
def is_perfect(num): #def es una palabra reservada 
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

perfect_numbers = [num for num in range(1, 1001) if is_perfect(num)]

print(f"Hay {len(perfect_numbers)} numeros perfectos entre 1 y 1000: {perfect_numbers}")