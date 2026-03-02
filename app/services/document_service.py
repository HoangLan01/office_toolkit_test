from pathlib import Path
from .skill_service import SkillService
from app.agent.prompt_loader import PromptLoader
from app.agent.office_writer_agent import OfficeWriterAgent
from app.renderers.docx_renderer import DocxRenderer
from app.renderers.pdf_renderer import PdfRenderer

class DocumentService:
    def __init__(self):
        self.skill_service = SkillService()
        self.prompt_loader = PromptLoader()
        self.agent = OfficeWriterAgent()
        self.docx_renderer = DocxRenderer()
        self.pdf_renderer = PdfRenderer()
        
    def generate_document(self, user_request: str, formats: list[str] = None, output_dir: str = "output/documents"):
        """
        Orchestrates the document generation process.
        """
        if formats is None:
            formats = ["docx", "pdf"]
            
        print("1. Loading Office Design Toolkit skill...")
        skill_content = self.skill_service.load_skill_content()
        
        print("2. Preparing Prompt...")
        prompt = self.prompt_loader.load_prompt(
            "office_writer",
            skill_content=skill_content,
            user_request=user_request
        )
        
        print("3. Generating content with AI Agent...")
        draft = self.agent.generate_document(prompt)
        
        print(f"Agent successfully generated document draft: '{draft.title}' with {len(draft.sections)} sections.")
        
        print("4. Rendering Documents...")
        # Create output filename base
        safe_title = "".join([c if c.isalnum() else "_" for c in draft.title]).strip("_")
        if not safe_title:
            safe_title = "generated_document"
            
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        if "docx" in formats:
            docx_path = f"{output_dir}/{safe_title}.docx"
            self.docx_renderer.render(draft, docx_path)
            
        if "pdf" in formats:
            pdf_path = f"{output_dir}/{safe_title}.pdf"
            self.pdf_renderer.render(draft, pdf_path)
            
        print("Done!")
