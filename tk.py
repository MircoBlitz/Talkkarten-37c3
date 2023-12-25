from pack.talks import Talks
from pack.render import Render
import argparse

parser = argparse.ArgumentParser(description='Prints or lists 37c3 Talkcards')
parser.add_argument('-l', '--list', action='store_true', help='list all printable talks')
parser.add_argument('-f', '--file', type=str, default="nA", help='Output file, default is ./out/talks.pdf')
parser.add_argument('-a', '--all', action='store_true', help='print all cards')
parser.add_argument('-i', '--id', type=int, default=0, help='print card with Talk id (get with list)')
args = parser.parse_args()

talks = Talks()

if args.file != "nA":
  pdf = Render(args.file)
else:
  pdf = Render()

if args.list:
  talks.printTalks()
  exit(0)

if args.id > 0:
  pdf.genPdfPage(talks.byId[args.id])
  pdf.savePdf()
  exit(0)

if args.all:
  for talk in talks.byId:
    pdf.genPdfPage(talks.byId[talk])
    pdf.nextPage()
  pdf.savePdf()
  exit(0)