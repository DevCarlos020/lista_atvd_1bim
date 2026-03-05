import psutil
p = psutil.disk_partitions()
for i, d in enumerate(p): print(f"{i}: {d.device} ({d.mountpoint})")
s = p[int(input("Escolha: "))]
u = psutil.disk_usage(s.mountpoint)
print(f"Total: {u.total/2**30:.1f}G | Usado: {u.used/2**30:.1f}G | Livre: {u.free/2**30:.1f}G")
# E/S: Teclado/Mouse (Entrada), Monitor/Impressora (Saida)