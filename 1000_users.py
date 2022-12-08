import datetime
import argparse
import random
import string
import os

print("Mitresko scripts for asterisk")

#possible types for users
types = {"friend","peer", "user"}
PASSWORD_LENGTH = 30

#parse args
parser = argparse.ArgumentParser(description='Info about users for sip.conf')
parser.add_argument('-s','--start', dest='start', type=int, help='Start number for dialplan')
parser.add_argument('-c','--count', dest='count', type=int, help='Number of users we want to add')
parser.add_argument('-S','--sections', dest='sections', nargs='+', help='Sections with general parameters', default=[])

args = parser.parse_args()
print(args.start)
print(args.count)
#print(args.sections[0])
#

if (args.count == None):
    count = int(input("how many users do you want to add to sip.conf?"))
else:
    count = args.count

if (args.start == None):
    start = int(input("Wich is start number?"))
else:
    start = args.start

#print prepared config
print(f"we will add {count} users, started from {start} with sections {args.sections}")


def get_date():
    x = datetime.datetime.now()
    return f"{x.day}.{x.month}.{x.year}_{x.hour}.{x.minute}"


def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(30))

date = get_date()
result_filename = f"sip_{date}.conf"
file_sip_phones = open(result_filename, "w")

for i in range(count):
    file_sip_phones.write(f"[{start + i}]")
    if (len(args.sections) > 0):
        file_sip_phones.write("(")
        for s in args.sections:
            if s != args.sections[-1]:
                file_sip_phones.write(f"{s},")
            else:
                file_sip_phones.write(f"{s})\n")
    else:
        file_sip_phones.write("\n")

    password = generate_password()
    file_sip_phones.write(f"secret={password}\n")
    file_sip_phones.write("\n\n")

file_sip_phones.close()

os.system(f"chown asterisk:asterisk {result_filename}")
os.system(f"chmod 750 {result_filename}")

file_sip_conf = open('sip.conf', 'a')
file_sip_conf.write(f"\n#include {result_filename}\n")
file_sip_conf.close()



