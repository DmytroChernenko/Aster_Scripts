import datetime
import argparse


print("Mitresko scripts for asterisk")

#possible types for users
types = {"friend","peer", "user"}


#parse args
parser = argparse.ArgumentParser(description='Info about users for sip.conf')
parser.add_argument('--start', dest='start', type=int, help='Start number for dialplan')
parser.add_argument('--count', dest='count', type=int, help='Number of users we want to add')
parser.add_argument('--type', dest='type', type=str, help='Type of user (friend, user, peer)')
#parser.add_argument('--context', dest='context', type=str, help='Context for dialplan')

args = parser.parse_args()
print(args.start)
print(args.count)
print(args.type)
#print(args.context)
#

if (args.count == None):
    count = int(input("how many users do you want to add to sip.conf?"))
else:
    count = args.count

if (args.start == None):
    start = int(input("Wich is start number?"))
else:
    start = args.start

if (args.type == None):
    type = input("Type of users (friend, user, peer)?")
else:
    type = args.type

#if (args.context == None):
#    context = input("Type of users (friend, user, peer)?")
#else:
#    context = args.context


#print prepared config
print(f"we will add {count} users, started from {start} in context")


def get_date():
    x = datetime.datetime.now()
    return f"{x.day}.{x.month}.{x.year}_{x.hour}.{x.minute}"



date = get_date()
f = open(f"sip_{date}.conf", "w")

for i in range(count):
    f.write(f"[{start + i}]\n")
    f.write(f"type={type}\n")
    f.write("secret=hello\n")
    f.write("context={context}\n")
    f.write("host=dynamic\n")
    f.write("\n\n\n")

f.close()

