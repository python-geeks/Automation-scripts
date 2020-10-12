import argparse
import wikipedia
from fpdf import FPDF


class PDF(FPDF):
    def chapter_title(self, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, '%s' % (label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, file_name):
        # Read text file
        with open(file_name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()

    def print_chapter(self, title, file_name):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(file_name)


def wikipedia_search(user_input):
    query = wikipedia.page(user_input)

    # Writing the search result in a temp file
    file = open('temp.txt', 'w')
    # write() - it used to write direct text to the file
    file.write(query.summary)
    # closing the file
    file.close()

    # variable pdf
    pdf = PDF()
    # declaring our file name
    pdf_file_name = user_input + ".pdf"
    # writing the content to a pdf file
    pdf.print_chapter(query.original_title, 'temp.txt')
    # saving the file in our computer
    pdf.output(pdf_file_name, 'F')

    # Clearing our temp file
    open("temp.txt", "w").close()


def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-s", "--search",
                        help="search your query")
    # parser.add_argument("-m", "--message", help="insert your message here")

    # Read arguments from command line
    args = parser.parse_args()
    if args.search is None:
        print("[-] No arguments were provided.")
        print("[x] For help: 'python wikipedia_search_and_save.py --help'")

    if args.search:
        wikipedia_search(args.search)
        print("[+] Your file was successfully saved.")


if __name__ == "__main__":
    main()
