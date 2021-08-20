# External Imports
from PIL import Image, ImageFont, ImageDraw
import os

# Internal Imports
from app import app


def generate_certificate(name, pr_num):
    '''generate_certificate Generates certificate using base template

    Args:
        name (string): Name to be displayed on certificate
        pr_num (integer): PR number to be displayed on certificate
    '''
    # Path to template certificate
    template_dir = os.path.join(app.root_path, "static/certificates/template")
    template_filename = "template.png"

    # Path to save the certificate
    output_dir = os.path.join(app.root_path, "static",
                              "certificates/generated/")
    output_filename = f"{name}.png"

    # Load the template file
    img = Image.open(os.path.join(template_dir, template_filename))
    draw = ImageDraw.Draw(img)

    # Text to put on the certificate
    event_name = "Hacktoberfest"
    contributed_at = "Automation scripts"
    msg = f"""for taking part in {event_name} and
contribution in #{pr_num} at {contributed_at}.
"""
    # Load fonts
    name_font = ImageFont.truetype(os.path.join(
        template_dir, "Sanchez-Regular.ttf"), 150)
    msg_font = ImageFont.truetype(os.path.join(
        template_dir, "Sanchez-Regular.ttf"), 70)

    # Insert text (Name)
    draw.text((1000, 1390), name, (51, 213, 172), font=name_font)
    # Insert text (Message)
    draw.text((1000, 1650), msg, (14, 69, 115), font=msg_font)

    # Calculate the width of the texts. We will need it to
    # draw the underline. As the pr number width can vary we cannot
    # hardcode the coordinates of the text to be underlined.
    # So we find the width of the pr_num and then calculate
    # the starting position of the underlined text.
    twidth, theight = draw.textsize(contributed_at, font=msg_font)
    prwidth, prheight = draw.textsize(pr_num, font=msg_font)

    lx = 1560 + prwidth + 120
    ly = 1810
    draw.line((lx, ly, lx + twidth, ly), fill=(14, 69, 115), width=5)

    # Save certificate
    img.save(os.path.join(output_dir, output_filename))
    # Return filename, required for rendering the certificate
    return output_filename
