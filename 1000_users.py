import datetime
import argparse


print("Mitresko scripts for asterisk")

#possible types for users
types = {"friend","peer", "user"}


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



date = get_date()
f = open(f"sip_{date}.conf", "w")

for i in range(count):
    f.write(f"[{start + i}]")
    if (len(args.sections) > 0):
        f.write("(")
        for s in args.sections:
            if s != args.sections[-1]:
                f.write(f"{s},")
            else:
                f.write(f"{s})\n")
    else:
        f.write("\n")

    f.write("secret=hello\n")
    f.write("\n\n")

f.close()

