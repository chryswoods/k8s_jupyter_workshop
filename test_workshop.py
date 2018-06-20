
import sys
import os

nfailed = 0

sys.write("Tesing git... ")

if os.system("git help > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing jupyter... ")

try:
    import jupyter
    sys.write(" PASS\n")
except:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing docker... ")

if os.system("docker images > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing az... ")

if os.system("az help > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing kubectl... ")

if os.system("kubectl help > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing kubectl... ")
 
if os.system("kubectl help > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

sys.write("Testing helm... ")

if os.system("helm help > /dev/null 2>&1") == 0:
    sys.write(" PASS\n")
else:
    sys.write(" FAIL\n")
    nfailed += 1

if nfailed > 0:
    sys.write("\nThere have been some failures - please review.\n")
    sys.write("Email chryswoods@gmail.com if you have any questions.\n")
else:
    sys.write("Success. Looks like everything has installed correctly :-)\n")
