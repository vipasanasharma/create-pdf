import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Load the JSON data from a file
with open(r"C:\Users\vipas\aws-pptx\test.json", 'r') as file:
    data = json.load(file)

# Create a PDF document
pdf = SimpleDocTemplate("output.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Add sections to the PDF
for key, value in data.items():
    section_title = Paragraph(f'<b>{key}</b>', styles['Heading1'])
    section_text = Paragraph(value, styles['BodyText'])
    story.append(section_title)
    story.append(section_text)

# Build the PDF
pdf.build(story)

print("PDF created successfully!")
