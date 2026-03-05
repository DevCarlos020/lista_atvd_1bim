import psutil, platform, subprocess

c = psutil.cpu_freq()
print(f"Modelo: {platform.processor()}")
print(f"Núcleos: {psutil.cpu_count(0)} Fis / {psutil.cpu_count()} Log")
print(f"Freq: {c.current/1000:.2f}GHz (Max: {c.max/1000:.2f}GHz)")

try:
 s = subprocess.check_output("wmic cpu get serialnumber", shell=True).decode().split()[1]
 print(f"Serial: {s}")
except:
 print("Serial: Nao permitido no SO atual")