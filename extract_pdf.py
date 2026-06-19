import sys
import pymupdf4llm

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf.py <input.pdf> <output.md>")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_md = sys.argv[2]
    
    print(f"Extracting {input_pdf} to {output_md}...")
    md_text = pymupdf4llm.to_markdown(input_pdf)
    
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(md_text)
        
    print("Done!")

if __name__ == "__main__":
    main()
