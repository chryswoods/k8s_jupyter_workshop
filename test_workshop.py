
import sys
import os

nfailed = 0

sys.stdout.write("Tesing git... ")

if os.system("git help > /dev/null 2>&1") == 0:
    sys.stdout.write(" PASS\n")
else:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

sys.stdout.write("Testing jupyter... ")

try:
    import jupyter
    sys.stdout.write(" PASS\n")
except:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

sys.stdout.write("Testing docker... ")

if os.system("docker images > /dev/null 2>&1") == 0:
    sys.stdout.write(" PASS\n")
else:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

sys.stdout.write("Testing az... ")

if os.system("az help > /dev/null 2>&1") == 0:
    sys.stdout.write(" PASS\n")
else:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

sys.stdout.write("Testing kubectl... ")

if os.system("kubectl help > /dev/null 2>&1") == 0:
    sys.stdout.write(" PASS\n")
else:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

sys.stdout.write("Testing helm... ")

if os.system("helm help > /dev/null 2>&1") == 0:
    sys.stdout.write(" PASS\n")
else:
    sys.stdout.write(" FAIL\n")
    nfailed += 1

if nfailed > 0:
    sys.stdout.write("\nThere have been some failures - please review.\n")
    sys.stdout.write("Email chryswoods@gmail.com if you have any questions.\n")
else:
    sys.stdout.write("Success. Looks like everything has installed correctly :-)\n")
