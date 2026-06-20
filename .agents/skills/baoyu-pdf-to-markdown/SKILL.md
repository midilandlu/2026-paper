---
name: baoyu-pdf-to-markdown
description: >-
  This skill extracts and converts PDF documents into high-quality Markdown. It extracts images from the PDF and embeds them correctly using relative links in the Markdown output. Use when the user asks to "convert PDF to markdown", "extract PDF", "parse PDF", or provides a `.pdf` file that needs to be translated or processed.
---

# PDF to Markdown Extractor

Converts PDF files to clean Markdown while accurately extracting and referencing images.

## Setup & Dependencies

This skill uses `pymupdf4llm` to process PDFs.

Before running for the first time or if the environment changes, ensure the dependency is installed:
```bash
pip install -r {baseDir}/requirements.txt
```

*(Where `{baseDir}` is the directory containing this SKILL.md)*

## Workflow

1. **Identify the Source PDF**: Ensure the target file is a `.pdf`.
2. **Determine Output Paths**:
   - `output_md`: The target markdown file (e.g., `{source_name}.md` in the same directory or a designated output folder).
   - `image_dir`: A dedicated folder to store extracted images (e.g., `{source_name}_images`).
3. **Execute Extraction Script**:
   Run the python script provided in this skill:
   ```bash
   python {baseDir}/scripts/pdf_to_md.py "<input_pdf>" "<output_md>" "<image_dir>"
   ```
4. **Verification**: 
   Check that `<output_md>` has been created and contains `![](...)` markdown links pointing correctly to the images within `<image_dir>`.

## Integration with Translation

If the user wants to **translate a PDF**, you should **always run this skill first** to generate the Markdown representation, and then pass the resulting `.md` file to the `baoyu-translate` skill.
