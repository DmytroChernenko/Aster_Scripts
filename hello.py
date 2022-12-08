import subprocess

x = subprocess.check_output("cat sip_sections.conf | grep 00000", shell=True);
print()