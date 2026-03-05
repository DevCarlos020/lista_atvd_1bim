import psutil
print("Ponto\tTotal\tUsado\tLivre\t%")
for p in psutil.disk_partitions():
 try:
  u = psutil.disk_usage(p.mountpoint)
  print(f"{p.mountpoint}\t{u.total/2**30:.1f}G\t{u.used/2**30:.1f}G\t{u.free/2**30:.1f}G\t{u.percent}%")
 except:pass