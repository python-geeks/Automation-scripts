from PIL import Image, ImageFont, ImageDraw
from app import app
import os

def generate_certificate(name, pr_num):
    template_dir = os.path.join(app.root_path, "static/certificates/template")
    template_filename = "template.png"
    
    output_dir = os.path.join(app.root_path, "static",
                              "certificates/generated/")
    output_filename = f"{name}.png"
    
    img = Image.open(os.path.join(template_dir, template_filename))
    draw = ImageDraw.Draw(img)
    
    event_name = "Hacktoberfest"
    contributed_at = "Automation scripts"
    msg = f"""for taking part in {event_name} and
contribution in #{pr_num} at {contributed_at}.
"""
    
    name_font = ImageFont.truetype(os.path.join(template_dir, "Sanchez-Regular.ttf"), 150)
    msg_font = ImageFont.truetype(os.path.join(template_dir, "Sanchez-Regular.ttf"), 70)
    
    draw.text((1000, 1390), name, (51, 213, 172), font=name_font)
    draw.text((1000, 1650), msg, (14, 69, 115), font=msg_font)
    
    twidth, theight = draw.textsize(contributed_at, font=msg_font)
    prwidth, prheight = draw.textsize(pr_num, font=msg_font)
    
    lx = 1560 + prwidth + 120
    ly = 1810
    draw.line((lx, ly, lx + twidth, ly), fill=(14, 69, 115), width=5)
    
    img.save(os.path.join(output_dir, output_filename))
    
    return output_filename
