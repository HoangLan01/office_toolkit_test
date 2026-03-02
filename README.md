# AI Office Toolkit

An AI-driven automated document generation service using Google Generative AI (Gemini).

## Features
- Integrates the "Office Design Toolkit" skill as a behavioral prompt.
- Uses Gemini structured generation (Pydantic schemas) to produce a document draft according to the required workflow.
- Renders high-quality `.docx` and `.pdf` documents deterministically via `python-docx` and `reportlab`.

## Architecture
1. **Skill Loader**: Retrieves and concatenates rules from the `.agents/skills/office-design-toolkit` folder.
2. **Prompt Loader**: Formats `app/prompts/office_writer.txt` template with the skill context and user request.
3. **AI Agent**: Uses the Gemini API with structured outputs (`response_schema`).
4. **Document Renderers**: Translates the generated JSON/Pydantic draft array into actual files using `docx` and `reportlab`.
5. **Document Service**: Coordinates the overall pipeline ensuring the strict workflow is followed (draft content -> define structure -> apply polish -> perform QA).

## Setup
1. `pip install -r requirements.txt`
2. Create a `.env` file and set your `GEMINI_API_KEY=your_key_here`.
3. `python app/main.py`
