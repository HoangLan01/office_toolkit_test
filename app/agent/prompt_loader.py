import os
from pathlib import Path

class PromptLoader:
    def __init__(self, prompts_dir: str = "app/prompts"):
        self.prompts_dir = Path(prompts_dir)

    def load_prompt(self, prompt_name: str, **kwargs) -> str:
        """
        Loads a prompt template from the prompts directory and formats it with kwargs.
        """
        prompt_path = self.prompts_dir / f"{prompt_name}.txt"
        
        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt file not found at {prompt_path}")
            
        with open(prompt_path, "r", encoding="utf-8") as f:
            template = f.read()
            
        try:
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required format variable in prompt {prompt_name}: {e}")
