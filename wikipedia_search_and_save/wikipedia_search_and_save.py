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
    print("Successfully saved!")


def main():
    user_input = input("Input here to search: ")
    wikipedia_search(user_input)


if __name__ == "__main__":
    main()
