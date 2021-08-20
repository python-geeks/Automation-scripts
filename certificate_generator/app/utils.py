from PIL import Image, ImageFont, ImageDraw
from app import app
import os

def generate_certificate(name):
    template_dir = os.path.join(app.root_path, "static/certificates/template")
    template_filename = "template.png"
    
    output_dir = os.path.join(app.root_path, "static",
                              "certificates/generated/")
    output_filename = f"{name}.png"
    
    img = Image.open(os.path.join(template_dir, template_filename))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join(template_dir, "DroidSansMono.ttf"), 150)
    draw.text((1000, 1390), name, (0, 0, 0), font=font)
    
    img.save(os.path.join(output_dir, output_filename))
    
    return output_filename
