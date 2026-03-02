import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class ParagraphDraft(BaseModel):
    text: str = Field(description="Content of the paragraph")
    style: str = Field(description="Optional style hint (e.g., 'Normal', 'Quote', 'Emphasis')")

class SectionDraft(BaseModel):
    heading: str = Field(description="Heading of the section")
    level: int = Field(description="Heading level (1, 2, 3)")
    paragraphs: List[ParagraphDraft] = Field(description="Paragraphs under this section")

class DocumentDraft(BaseModel):
    title: str = Field(description="Title of the document")
    sections: List[SectionDraft] = Field(description="Sections of the document")

class OfficeWriterAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def generate_document(self, prompt: str) -> DocumentDraft:
        """
        Calls Gemini to generate a structured document draft using Pydantic schema.
        """
        print("Calling Gemini API to generate document...")
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=DocumentDraft,
                temperature=0.4
            )
        )
        
        try:
            draft_dict = json.loads(response.text)
            return DocumentDraft.model_validate(draft_dict)
        except json.JSONDecodeError as e:
            print(f"Failed to decode Gemini response: {response.text}")
            raise e
