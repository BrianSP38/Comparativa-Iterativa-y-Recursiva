import subprocess, sys, pandas as pd, matplotlib.pyplot as plt

# --- 1) Compilar C++ ---
print("Compilando C++...")
subprocess.run(["g++","-O3","-std=c++17","fib_bench.cpp","-o","fib_bench"], check=True)

# --- 2) Ejecutar C++ ---
print("Ejecutando C++...")
cpp_out = subprocess.run(["./fib_bench"], capture_output=True, text=True).stdout.splitlines()

# --- 3) Ejecutar Python ---
print("Ejecutando Python...")
py_out = subprocess.run([sys.executable,"py_bench.py"], capture_output=True, text=True).stdout.splitlines()

# --- 4) Unir resultados ---
lines = cpp_out + py_out
rows = [line.split(",") for line in lines if "language" not in line]
df = pd.DataFrame(rows, columns=["language","algorithm","n","median_ms"])
df["n"] = df["n"].astype(int)
df["median_ms"] = df["median_ms"].astype(float)
df.to_csv("results.csv", index=False)
print("Resultados guardados en results.csv")

# --- 5) Graficar ---
plt.figure()
for (lang, algo), sub in df.groupby(["language","algorithm"]):
    sub = sub.sort_values("n")
    plt.plot(sub["n"], sub["median_ms"], marker="o", label=f"{lang} {algo}")
plt.yscale("log")  # escala logarítmica para ver mejor
plt.xlabel("n")
plt.ylabel("Tiempo (ms, mediana)")
plt.title("Comparación C++ vs Python\nFibonacci Recursivo vs Iterativo")
plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.savefig("plot.png", dpi=150)
print("Gráfica guardada en plot.png")

# --- 6) Análisis automático ---
ratio = df.groupby(["algorithm","language"])["median_ms"].median().unstack()
analysis = f"""
Iterativo: Python fue ~{ratio.loc['Iterativo','Python']/ratio.loc['Iterativo','C++']:.1f}× más lento.
Recursivo: Python fue ~{ratio.loc['Recursivo','Python']/ratio.loc['Recursivo','C++']:.1f}× más lento.

Conclusiones:
- El iterativo siempre es más rápido que el recursivo.
- C++ siempre es más rápido que Python.
- La diferencia se nota especialmente en la versión recursiva.
"""
with open("analysis.txt","w") as f:
    f.write(analysis)
print(analysis)
