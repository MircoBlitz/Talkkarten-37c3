from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape,A5
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame, PageBreak
from reportlab.lib.units import cm
import datetime
class Render:
    # Initializer / Instance Attributes
    def __init__(self, filename="output/talks.pdf"):
        self.talk = {}
        self.font = "Times-Roman"
        self.pagesize = landscape(A5)
        self.style = getSampleStyleSheet()
        self.canvas = Canvas(filename, pagesize=self.pagesize)
    
    def nextPage(self):
      self.canvas.showPage()
    
    def genPpfFrame(self, text, x, y, textbox_width, textbox_height, fontsize, leading, align=0, drawrect=False):
      text_style = ParagraphStyle("Text", parent=self.style["Normal"], fontName=self.font, fontSize=fontsize, leading=leading, alignment=align)
      if drawrect == True:
        boundary=1
      else:
        boundary=0
      frame = Frame(x, y, textbox_width, textbox_height, showBoundary=boundary)
      paragraph = Paragraph(text, style=text_style)
      frame.addFromList([paragraph], self.canvas)

    def genPdfPage(self, talk):
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
      
      infoline = ["", "", ""]
      infoline[0] = printdate + " / " + textday + "  /  " + talk["room"].upper()
      infoline[1] = "Track: " + talk["track"] + " / Type: " + talk["type"] + " / " + talk["language"].upper()
      infoline[2] = "Start: " + talk["start"] + " / Duration: " + talk["duration"] + "h"
      self.genPageHeadline(infoline)
      nextDrawPoint = self.genTitle(talk["title"], talk["subtitle"])
      if( talk["abstract"] != "" and talk["abstract"] != None): 
        abstract = talk["abstract"] + talk["abstract"] + talk["abstract"] + talk["abstract"]
        self.genPpfFrame(
          abstract[:400],
          0.9 * cm, nextDrawPoint * cm, 
          19 * cm, 3.5 * cm, 
          12, 14, 1, 
          drawrect=False
          )
        nextDrawPoint= nextDrawPoint - 0.5

      self.genPersonBoxes(talk["persons"], nextDrawPoint)
      self.nextPage()
      self.genPageHeadline(infoline)
      nextDrawPoint = self.genTitle(talk["title"], talk["subtitle"])
      if(talk["description"] != "" and talk["description"] != None):
        description = talk["description"][:2050]
        self.genPpfFrame(
          description,
          0.9 * cm, 1 * cm, 
          19 * cm, 9 * cm, 
          12, 14, 1, 
          drawrect=False
          )
      
    def genTitle(self, title, subtitle):
      if(len(title) > 110):
        size = 10
      elif (len(title) > 70):
        size = 14
      else:
        size = 16
      self.genPpfFrame(title,
        0.9 * cm, 11.2 * cm, 
        19 * cm, 1.2 * cm, 
        size, 20, 1, 
        drawrect=True
        )
      if(subtitle != "" and subtitle != None):
        self.genPpfFrame(
          subtitle,
          0.9 * cm, 9.3 * cm, 
          19 * cm, 2 * cm, 
          14, 14, 1, 
          drawrect=False
          )
        nextDrawPoint= 6.6
      else:
        nextDrawPoint= 7.3
      
      return nextDrawPoint
    
      
    def savePdf(self):
      self.canvas.save()  
      
    def genPageHeadline(self, infoline):
      self.genPpfFrame(
        infoline[0], 
        0.6 * cm, 13.5 * cm, 
        7.9 * cm, 1 * cm,
        14, 14, 0, 
        drawrect=False
        )
      self.genPpfFrame(
        infoline[1], 
        8.5 * cm, 13.5 * cm, 
        12 * cm, 1 * cm,
        14, 14, 2, 
        drawrect=False
        )
      self.genPpfFrame(
        infoline[2], 
        0.6 * cm, 12.9 * cm, 
        8 * cm, 1 * cm, 
        14, 14, 0, 
        drawrect=False
        )
    
    def genPersonBoxes(self, persons, nextDrawPoint):
      if(len(persons) == 1):
        self.genPpfFrame(
          persons[0]["name"], 
          2.1 * cm, 6.7 * cm, 
          15 * cm, 1 * cm, 
          16, 14, 1, 
          drawrect=False
          )
        biography = self.formBiography(persons[0]["biography"], 1020)
        self.genPpfFrame(
          biography, 
          2.6 * cm, 1.2 * cm, 
          15 * cm, 5.4 * cm, 
          11, 14, 1, 
          drawrect=False
          )
      
      if(len(persons) == 2):
        self.genPpfFrame(
          persons[0]["name"], 
          0.6 * cm, 6.7 * cm, 
          9.4 * cm, 1 * cm, 
          16, 14, 1, 
          drawrect=False
          )
        biography = self.formBiography(persons[0]["biography"], 450)
        self.genPpfFrame(
          biography, 
          0.6 * cm, 1.2 * cm, 
          9.4 * cm, 5.4 * cm, 
          11, 14, 1, 
          drawrect=False
          )
        self.genPpfFrame(
          persons[1]["name"], 
          10.4 * cm, 6.7 * cm, 
          9.4 * cm, 1 * cm, 
          16, 14, 1, 
          drawrect=False
          )
        biography = self.formBiography(persons[1]["biography"], 450)
        self.genPpfFrame(
          biography, 
          10.4 * cm, 1.2 * cm, 
          9.4 * cm, 5.4 * cm, 
          11, 14, 1, 
          drawrect=False
          )
        
      if(len(persons) > 2):
        draw = 6.7
        for person in persons:
          self.genPpfFrame(
            person["name"], 
            0.6 * cm, draw * cm, 
            20 * cm, 1 * cm, 
            16, 14, 1, 
            drawrect=False
            )
          draw = draw - 1.5
          
    def formBiography(self, biography, maxlength):
      if biography != None:
        if len(biography) > maxlength:
          return biography[:maxlength] + "..."
        else:
          return biography
      else:
        return ""

      
