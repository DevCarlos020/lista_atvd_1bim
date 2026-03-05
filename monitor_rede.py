import psutil, time
while 1:
 r1, s1 = psutil.net_io_counters()[:2]
 time.sleep(1)
 r2, s2 = psutil.net_io_counters()[:2]
 print(f"D: {(r2-r1)/1024:.1f}kB/s | U: {(s2-s1)/1024:.1f}kB/s")