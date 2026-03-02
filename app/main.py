from dotenv import load_dotenv
import sys
import os

# Ensure the root folder is in sys.path if run directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.document_service import DocumentService

def main():
    # Load environment variables
    load_dotenv()
    
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is not set. Please create a .env file.")
        return

    # Initialize Service
    service = DocumentService()
    
    # Sample Request
    request = (
        "Write a 2-page project proposal for a new AI-based Automated Office Toolkit. "
        "Include an executive summary, project goals, timeline, and proposed tech stack. "
        "Ensure the formatting is highly professional as per the design guidelines and use clear structural hierarchy."
    )
    
    print("Starting Document Generation...")
    service.generate_document(user_request=request, formats=["docx", "pdf"])

if __name__ == "__main__":
    main()
