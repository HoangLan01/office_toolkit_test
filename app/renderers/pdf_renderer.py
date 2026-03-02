from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from app.agent.office_writer_agent import DocumentDraft

class PdfRenderer:
    def render(self, draft: DocumentDraft, output_path: str):
        """
        Renders the DocumentDraft into a PDF file using reportlab.
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        doc = SimpleDocTemplate(str(output_file), pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Custom Title Style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            alignment=TA_CENTER,
            spaceAfter=20
        )
        
        story = []
        
        # Add Title
        story.append(Paragraph(draft.title, title_style))
        story.append(Spacer(1, 12))
        
        for section in draft.sections:
            # Determine Heading Style
            if section.level == 1:
                h_style = styles['Heading1']
            elif section.level == 2:
                h_style = styles['Heading2']
            else:
                h_style = styles['Heading3']
                
            story.append(Paragraph(section.heading, h_style))
            story.append(Spacer(1, 6))
            
            for para in section.paragraphs:
                p_style = styles['Normal']
                if para.style and para.style.lower() in ["quote", "emphasis"]:
                    p_style = styles['Italic'] # Fallback
                
                story.append(Paragraph(para.text, p_style))
                story.append(Spacer(1, 6))
                
        doc.build(story)
        print(f"PDF saved to {output_file}")
