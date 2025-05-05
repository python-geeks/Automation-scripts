import fitz
import argparse
import sys
import os

def add_frame(input_pdf_path, left=20, right=20, top=20, bottom=20, thickness=2):
    try:
        doc = fitz.open(input_pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            page_rect = page.rect

            frame_rect = fitz.Rect(
                left,                        # left
                top,                         # top
                page_rect.width - right,     # right
                page_rect.height - bottom    # bottom
            )
            
            page.draw_rect(
                frame_rect,           # rectangle coordinates
                width=thickness       # frame thickness
            )
        
        # Set output filename if not provided

        base, ext = os.path.splitext(input_pdf_path)
        output_pdf_path = f"{base}_framed.pdf"
        
        doc.save(output_pdf_path)
        print(f"PDF with rectangle frame saved to {output_pdf_path}")
        
    except UnicodeDecodeError as e:
        print("Error: Input file path encoding issue. Please ensure the file path is UTF-8 encoded.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'doc' in locals():
            doc.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add a rectangle frame to each page of a PDF document.\n"
                    "Flags: --l (left), --r (right), --t (top), --b (bottom), --th (thickness)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("--l", type=float, default=20, help="Left")
    parser.add_argument("--r", type=float, default=20, help="Right")
    parser.add_argument("--t", type=float, default=20, help="Top")
    parser.add_argument("--b", type=float, default=20, help="Bottom")
    parser.add_argument("--th", type=float, default=2, help="Thickness")
    try:
        args = parser.parse_args()
        add_frame(
            args.input_pdf,
            left=args.l,
            right=args.r,
            top=args.t,
            bottom=args.b,
            thickness=args.th
        )
    except Exception as e:
        print(f"Error: {e}\n")
        parser.print_usage()
        sys.exit(1)