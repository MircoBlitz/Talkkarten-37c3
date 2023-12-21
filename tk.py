import requests
import json
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape,A5
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import cm
import json
import datetime
import pytz
from HeraldTalkcards.pack.talks import Talks
from HeraldTalkcards.pack.render import Render



def genPageHeadline(infoline, canvas, font):
  genPpfFrame(
    canvas, infoline[0], 
    0.6 * cm, 13.5 * cm, 
    7.9 * cm, 1 * cm, 
    font, 14, 14, 0, 
    drawrect=False
    )
  genPpfFrame(
    canvas, infoline[1], 
    8.5 * cm, 13.5 * cm, 
    12 * cm, 1 * cm,
    font, 14, 14, 2, 
    drawrect=False
    )
  genPpfFrame(
    canvas, infoline[2], 
    0.6 * cm, 12.9 * cm, 
    8 * cm, 1 * cm, 
    font, 14, 14, 0, 
    drawrect=False
    )




def generatePDF(talk):
  # Variable preparation
  #pdf styles
  font = "Times-Roman"
  page_size = landscape(A5)
  # date 
  dt = datetime.datetime.strptime(talk["date"], "%Y-%m-%dT%H:%M:%S%z")
  printdate= dt.strftime("%d.%m.%Y")
  day = dt.strftime("%d")
  if day == "27":
    textday = "DAY1"
  if day == "28":
    textday = "DAY2"
  if day == "29":
    textday = "DAY3" 
  if day == "30":
    textday = "DAY4"
  
  
  # A5 format 21.0 cm x 14.8 cm
  # please keep a boundary of 0.2 * cm on all sides
  # the counting starts from bottom left corner of the page
  # so 0.4 * cm, 14 - lineheight/2 * cm is the top left corner of the page 
  # the lineheight of 
  # Helvetica 12 is 0.4 * cm
  # Helvetica 14 is 0.7 * cm
  canvas = Canvas("tk.pdf", pagesize=page_size)
  #concated string of Date, Room, track, type, start and duration
  infoline = ["", "", ""]
  infoline[0] = printdate + " / " + textday + "  /  " + talk["room"].upper()
  infoline[1] = "Track: " + talk["track"] + " / Type: " + talk["type"] + " / " + talk["language"].upper()
  infoline[2] = "Start: " + talk["start"] + " / Duration: " + talk["duration"] + "h"
  genPageHeadline(infoline, canvas, font)
  
  genPpfFrame(
    canvas, talk["title"],
    0.9 * cm, 10.8 * cm, 
    19 * cm, 2 * cm, 
    font, 18, 20, 1, 
    drawrect=False
    )
  if(talk["subtitle"] != "" and talk["subtitle"] != None):
    genPpfFrame(
      canvas, talk["subtitle"],
      0.9 * cm, 9.3 * cm, 
      19 * cm, 2 * cm, 
      font, 14, 14, 1, 
      drawrect=False
      )
    nextDrawPoint= 6.9
  else:
    nextDrawPoint= 9.3
  
  if( talk["abstract"] != "" and talk["abstract"] != None): 
    genPpfFrame(
      canvas, talk["abstract"],
      0.9 * cm, nextDrawPoint * cm, 
      19 * cm, 3.5 * cm, 
      font, 12, 14, 1, 
      drawrect=False
      )
    nextDrawPoint= nextDrawPoint - 3.5
  
  print(len(talk["persons"]))
  # genPpfFrame(
  #   canvas, talk["description"],
  #   0.9 * cm, 0.5 * cm, 
  #   19 * cm, 4 * cm, 
  #   font, 9, 10, 0, 
  #   drawrect=True
  #   )
  canvas.save()


talks = Talks()
ta = json.dumps(talks.byId[11993])
print(ta)

print(getSampleStyleSheet())

generatePDF(talks.byId[11993])


