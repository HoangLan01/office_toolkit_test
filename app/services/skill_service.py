import os
from pathlib import Path

class SkillService:
    def __init__(self, skill_dir: str = ".agents/skills/office-design-toolkit"):
        self.skill_dir = Path(skill_dir)

    def load_skill_content(self) -> str:
        """
        Loads the main SKILL.md and all references into a single string.
        """
        content_parts = []
        
        # Load main SKILL.md
        main_skill_path = self.skill_dir / "SKILL.md"
        if main_skill_path.exists():
            with open(main_skill_path, "r", encoding="utf-8") as f:
                content_parts.append("=== MAIN SKILL ===")
                content_parts.append(f.read())
        else:
            print(f"Warning: Main skill file not found at {main_skill_path}")

        # Load references
        references_dir = self.skill_dir / "references"
        if references_dir.exists() and references_dir.is_dir():
            content_parts.append("\n=== SKILL REFERENCES ===")
            for ref_file in sorted(references_dir.glob("*.md")):
                with open(ref_file, "r", encoding="utf-8") as f:
                    content_parts.append(f"\n--- Reference: {ref_file.name} ---")
                    content_parts.append(f.read())
        
        return "\n".join(content_parts)
