import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4

# Load resume data
with open("data.json", "r") as f:
    data = json.load(f)

# Output file
file_path = "resume.pdf"

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Header', fontSize=16, leading=20, spaceAfter=10))
styles.add(ParagraphStyle(name='SubHeader', fontSize=12, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='Body', fontSize=10, leading=14))

story = []

name = data["name"]
contact = data["contact"]
summary = data["summary"]
skills = data["skills"]

# -----------------------
# BUILD DOCUMENT
# -----------------------

story.append(Paragraph(name, styles['Header']))
story.append(Paragraph(contact, styles['Body']))
story.append(Spacer(1, 12))

story.append(Paragraph("Professional Summary", styles['SubHeader']))
story.append(Paragraph(summary, styles['Body']))
story.append(Spacer(1, 12))

story.append(Paragraph("Technical Skills", styles['SubHeader']))
story.append(ListFlowable([Paragraph(s, styles['Body']) for s in skills], bulletType='bullet'))
story.append(Spacer(1, 12))

story.append(Paragraph("Professional Experience", styles['SubHeader']))

for job in data["experience"]:
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"<b>{job['title']}</b>", styles['Body']))
    story.append(ListFlowable([Paragraph(p, styles['Body']) for p in job["points"]], bulletType='bullet'))

# -----------------------
# GENERATE PDF
# -----------------------
doc = SimpleDocTemplate(file_path, pagesize=A4)
doc.build(story)

print("Resume generated:", file_path)