def jml_kuadrad_ganjil(n):
    return sum(x*x for x in range(1,n) if x%2==1)


print(jml_kuadrad_ganjil(5))