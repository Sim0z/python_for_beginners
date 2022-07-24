fromm os import popen

while 1:
    outp = popen("protonvpn-cli c -r").read()
    print(outp)
    if "Successfully" in outp:
        break
