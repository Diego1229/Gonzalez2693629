for j in range (1,1001):
    print(j)

    def j (num):
        divisores = [i for i in range(1,num) if num % i == 0] 
        return sum(divisores) == num  

y =  [num for num in range(1, 1001) if j (num)]
print(f"hay {len(y)} numeros perfectos entre 1 y 1000:(j)")

