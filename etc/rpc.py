from pypresence import Presence
import subprocess as sp
from time import sleep

def run(cmd):
    return sp.run(cmd, capture_output=True).stdout.decode("utf-8").strip()

while True:
    try:
        rpc = Presence("1133070138602700810")
        details = run(["whoami"]) + "@" + run(["uname", "-n"])
        rpc.connect()
        while True:
            rpc.update(
                state=run(["uptime", "-p"]),
                details=details,
                large_image="arch",
                small_image="linux"
            )
            sleep(10)
    except Exception as e:
        print(e)
    sleep(10)
