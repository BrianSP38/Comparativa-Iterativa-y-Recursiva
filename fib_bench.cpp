#include <bits/stdc++.h>   // incluye todo el STL de C++
#include <chrono>          // para medir tiempos
using namespace std;
using namespace std::chrono;

// --- Fibonacci recursivo ---
long long fibRec(int n){
    if(n<=1) return n;
    return fibRec(n-1)+fibRec(n-2);
}

// --- Fibonacci iterativo ---
long long fibIter(int n){
    if(n<=1) return n;
    long long a=0, b=1, c;
    for(int i=2;i<=n;i++){
        c=a+b;   // sumamos los dos anteriores
        a=b;
        b=c;
    }
    return b;
}

// --- función para calcular la mediana de varios tiempos ---
double median_ms(const vector<double>& vals){
    if(vals.empty()) return 0.0;
    vector<double> v = vals;
    nth_element(v.begin(), v.begin()+v.size()/2, v.end());  // orden parcial
    if(v.size()%2==1){
        return v[v.size()/2];  // si es impar, el del medio
    }else{
        auto a = *max_element(v.begin(), v.begin()+v.size()/2);
        auto b = v[v.size()/2];
        return (a+b)/2.0;      // si es par, promedio
    }
}

int main(int argc, char** argv){
    // valores a probar
    vector<int> ns = {5,10,20,30,35,38,40};
    int repeats = 5;   // número de repeticiones

    // CSV header
    cout << "language,algorithm,n,median_ms" << "\n";

    // --- Benchmark recursivo ---
    for(int n: ns){
        vector<double> times_ms;
        for(int r=0;r<repeats;r++){
            auto t0 = high_resolution_clock::now();
            (void)fibRec(n); // ejecuta recursivo
            auto t1 = high_resolution_clock::now();
            double ms = duration<double, milli>(t1 - t0).count();
            times_ms.push_back(ms);
        }
        cout << "C++," << "Recursivo," << n << "," << median_ms(times_ms) << "\n";
    }

    // --- Benchmark iterativo ---
    for(int n: ns){
        vector<double> times_ms;
        for(int r=0;r<repeats;r++){
            auto t0 = high_resolution_clock::now();
            (void)fibIter(n); // ejecuta iterativo
            auto t1 = high_resolution_clock::now();
            double ms = duration<double, milli>(t1 - t0).count();
            times_ms.push_back(ms);
        }
        cout << "C++," << "Iterativo," << n << "," << median_ms(times_ms) << "\n";
    }
    return 0;
}
