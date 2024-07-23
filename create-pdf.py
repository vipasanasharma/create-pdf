import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Load the JSON data from a file
with open('path_to_your_json_file.json', 'r') as file:
    data = json.load(file)

# Create a PDF document
pdf = SimpleDocTemplate("output.pdf", pagesize=letter)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SectionTitle', fontSize=14, leading=16, spaceAfter=10, bold=True))
styles.add(ParagraphStyle(name='SectionText', fontSize=12, leading=14, spaceAfter=10))

story = []

def add_section(title, text):
    story.append(Paragraph(title, styles['SectionTitle']))
    story.append(Paragraph(text, styles['SectionText']))
    story.append(Spacer(1, 12))  # Add space between sections

def parse_json(data, level=0):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                add_section(key, "")
                parse_json(value, level + 1)
            else:
                add_section(key, str(value))
    elif isinstance(data, list):
        for item in data:
            parse_json(item, level)

# Parse and add data to the PDF
parse_json(data)

# Build the PDF
pdf.build(story)

print("PDF created successfully!")
