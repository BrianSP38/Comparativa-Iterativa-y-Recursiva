import time, statistics

# --- Fibonacci recursivo ---
def fib_rec(n: int) -> int:
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

# --- Fibonacci iterativo ---
def fib_iter(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def median_ms(vals):
    return statistics.median(vals) if vals else 0.0

def main():
    ns = [5,10,20,30,35,38,40]  # valores de prueba
    repeats = 5

    print("language,algorithm,n,median_ms")

    # --- Benchmark recursivo ---
    for n in ns:
        times = []
        for _ in range(repeats):
            t0 = time.perf_counter()
            fib_rec(n)
            t1 = time.perf_counter()
            times.append((t1-t0)*1000)  # en ms
        print(f"Python,Recursivo,{n},{median_ms(times)}")

    # --- Benchmark iterativo ---
    for n in ns:
        times = []
        for _ in range(repeats):
            t0 = time.perf_counter()
            fib_iter(n)
            t1 = time.perf_counter()
            times.append((t1-t0)*1000)
        print(f"Python,Iterativo,{n},{median_ms(times)}")

if __name__ == "__main__":
    main()
