import sys
import os
import pymupdf4llm

def main():
    if len(sys.argv) < 4:
        print("Usage: python pdf_to_md.py <input.pdf> <output.md> <image_dir>")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_md = sys.argv[2]
    image_dir = sys.argv[3]
    
    # Ensure image directory exists
    os.makedirs(image_dir, exist_ok=True)
    
    print(f"Extracting '{input_pdf}'...")
    print(f"Output markdown: '{output_md}'")
    print(f"Image directory: '{image_dir}'")
    
    try:
        # Convert PDF to Markdown and extract images into image_dir
        # write_images=True instructs it to output the image files
        md_text = pymupdf4llm.to_markdown(input_pdf, write_images=True, image_path=image_dir)
        
        # When pymupdf4llm writes images, it replaces spaces in the image_path with underscores
        # during the generation of markdown tags. So we need to correct the paths inside md_text
        # if the user provided an image_dir with spaces, or we just rely on pymupdf4llm behavior.
        # Actually, it's safer to let pymupdf4llm do its thing, but we should make sure the md_text
        # points to the right relative path from output_md.
        
        # By default, pymupdf4llm uses image_path as a prefix. 
        # If output_md is "out/file.md" and image_dir is "out/images",
        # the markdown will contain "![](out/images/...)".
        # We need to make the links relative to the markdown file's directory.
        
        md_dir = os.path.dirname(os.path.abspath(output_md))
        abs_image_dir = os.path.abspath(image_dir)
        
        try:
            rel_image_dir = os.path.relpath(abs_image_dir, md_dir)
            # Normalize path for markdown (forward slashes)
            rel_image_dir = rel_image_dir.replace('\\', '/')
        except ValueError:
            # Fallback if on different drives
            rel_image_dir = image_dir.replace('\\', '/')
            
        # pymupdf4llm replaces spaces with underscores in its path insertion.
        # It literally uses the string passed to image_path but replaces spaces with _.
        original_prefix = image_dir.replace(' ', '_')
        
        if original_prefix != rel_image_dir:
            # We need to replace the absolute/wrong prefix with the correct relative prefix
            md_text = md_text.replace(f"({original_prefix}/", f"({rel_image_dir}/")
            md_text = md_text.replace(f"({original_prefix}\\", f"({rel_image_dir}/")
        
        # Write the finalized markdown text
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(md_text)
            
        print("\nExtraction completed successfully!")
        
    except Exception as e:
        print(f"\nError extracting PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
