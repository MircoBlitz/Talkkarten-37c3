import json
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape,A5
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import cm
import datetime
import pytz
class Render:
    # Initializer / Instance Attributes
    def __init__(self):
        self.talk = {}
        self.font = "Times-Roman"
        self.pagesize = landscape(A5)

    
    def genPdf(self, talk):
        
        
    def genPpfFrame(
        canvas, text, 
  x, y, 
  textbox_width, textbox_height, 
  font, fontsize, leading, align=0, 
  drawrect=False
  ):
  style = getSampleStyleSheet()
  text_style = ParagraphStyle("Text", parent=style["Normal"], fontName=font, fontSize=fontsize, leading=leading, alignment=align)
  if drawrect == True:
    boundary=1
  else:
    boundary=0
  frame = Frame(x, y, textbox_width, textbox_height, showBoundary=boundary)
  paragraph = Paragraph(text, style=text_style)
  frame.addFromList([paragraph], canvas)