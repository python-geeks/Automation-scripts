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

    # Add a page
    pdf.add_page()

    # setting style and size of font for the pdf
    pdf.set_font("Arial", size=12)
    pdf.cell(
        200, 10,
        txt="Generated Prscription",
        ln=1, align='C'
    )

    for medic in medicines:
        if ('Medicine Name' in medicines[medic]):
            # create a cell
            pdf.cell(
                200, 10,
                ln=1, align='C',
                txt=medic
            )
            pdf.cell(
                200, 10,
                ln=2,
                txt="Medicine Name: " + medicines[medic]["Medicine Name"],
            )
            if "Instruction" in medicines[medic]:
                pdf.cell(
                    200, 10,
                    ln=2,
                    txt="Instructions: " + medicines[medic]["Instruction"]
                )
            else:
                pdf.cell(
                    200, 10,
                    ln=2,
                    txt="Instructions*: No Instructions given"
                )

    # save the pdf with name .pdf
    pdf.output("Prescription.pdf")
