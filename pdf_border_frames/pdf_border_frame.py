import fitz  # PyMuPDF
import argparse
import sys
import os


def add_frame(input_pdf_path, left=20, right=20, top=20, bottom=20, thickness=2):
    try:
        doc = fitz.open(input_pdf_path)

        for page in doc:
            page_rect = page.rect
            frame_rect = fitz.Rect(
                left,                         # left
                top,                          # top
                page_rect.width - right,      # right
                page_rect.height - bottom     # bottom
            )

            page.draw_rect(
                frame_rect,
                width=thickness
            )

        base, _ = os.path.splitext(input_pdf_path)
        output_pdf_path = f"{base}_framed.pdf"
        doc.save(output_pdf_path)
        print(f"PDF with rectangle frame saved to {output_pdf_path}")

    except UnicodeDecodeError:
        print(
            "Error: Input file path encoding issue. "
            "Please ensure the file path is UTF-8 encoded."
        )
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'doc' in locals():
            doc.close()


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Add a rectangle frame to each page of a PDF document.\n"
            "Flags: --l (left), --r (right), --t (top), --b (bottom), "
            "--th (thickness)"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("--l", type=float, default=20, help="Left margin")
    parser.add_argument("--r", type=float, default=20, help="Right margin")
    parser.add_argument("--t", type=float, default=20, help="Top margin")
    parser.add_argument("--b", type=float, default=20, help="Bottom margin")
    parser.add_argument("--th", type=float, default=2, help="Frame thickness")

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


if __name__ == "__main__":
    main()
