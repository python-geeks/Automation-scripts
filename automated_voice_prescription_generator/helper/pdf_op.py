from fpdf import FPDF


class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


def save_pdf(medicines):
    pdf = PDF()

    try:
        # Add a page
        pdf.add_page()

        # setting style and size of font for the pdf
        pdf.set_font("Arial", size=12)
        pdf.set_title("Generated Prescription")
        pdf.set_author("by Dr. Smith")
        for medicine in medicines:
            print(medicines[medicine]["Medicine Name"])
            # create a cell
            pdf.cell(
                200, 10,
                txt=medicine,
                ln=1, align='C'
            )
            pdf.cell(
                200, 10,
                txt="Medicine Name: " + medicines[medicine]["Medicine Name"],
                ln=2,
            )
            pdf.cell(
                200, 10,
                txt="Instruction to use: " +
                medicines[medicine]["Medicine Instruction"],
                ln=2,
            )

        # save the pdf with name .pdf
        pdf.output("Prescription.pdf")
    except Exception as e:
        print("OOPS!! Error e: ", e)
