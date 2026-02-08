import subprocess
#uses systemctl to see if services are running and start/stop them
#the functions' purposes are pretty obvious
def is_service_running(service:str):
    return subprocess.run(f"systemctl is-active {service}".split(" ")).returncode==0
def start_service(service:str):
    subprocess.run(["systemctl","start",service])
def stop_service(service:str):
    subprocess.run(["systemctl","stop",service])
