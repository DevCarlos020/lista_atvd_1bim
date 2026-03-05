import psutil, time, os
while 1:
 time.sleep(3)
 os.system('cls' if os.name=='nt' else 'clear')
 m, c = psutil.virtual_memory(), psutil.cpu_percent()
 d = psutil.disk_usage('/')
 r1, s1 = psutil.net_io_counters()[:2]
 r2, s2 = psutil.net_io_counters()[:2]
 print(f"--- MONITOR XGH ---\nRAM: {m.percent}% ({m.used/2**20:.0f}MB)\nCPU: {c}%\nDISCO: {d.free/2**30:.1f}GB Livre\nNET: D:{(r2-r1)/1024:.1f}kB/s | U:{(s2-s1)/1024:.1f}kB/s")