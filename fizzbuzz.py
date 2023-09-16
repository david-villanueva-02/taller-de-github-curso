for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("ola")
        continue
    elif fizzbuzz % 3 == 0:
        print("como")
        continue
    elif fizzbuzz % 5 == 0:
        print("estas")
        continue
    print(fizzbuzz)
