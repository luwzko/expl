#0. step - setup
import re
import requests
import subprocess

gtfo_bins = []
bins = []

#1. step - find suid binaries
pattr_suid = re.compile("(\/[0-9A-Za-z_.\-]+)+")
find_output = str(subprocess.run("find / -type f -perm -04000 -ls 2>/dev/null", shell=True, capture_output=True).stdout)

bins = pattr_suid.findall(find_output)
#2. step - goto gtfo bins and find binaries that are on gtfo
for b in bins:
    _b = b[1:]
    r = requests.get(f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{_b}.md")
    if r.status_code == 200:
        gtfo_bins.append(_b)
#3. step - print found binaries
print(gtfo_bins)