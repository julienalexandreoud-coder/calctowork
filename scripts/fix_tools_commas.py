import re

with open(r"C:\Microsaas\obra\scripts\tools_config.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add comma to any TOOLS entry line that lacks one
content = re.sub(r'^(\s+\{\"id\": \"\d+\", .*\}\})(?!,)$', r'\1,', content, flags=re.MULTILINE)

with open(r"C:\Microsaas\obra\scripts\tools_config.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed commas")
