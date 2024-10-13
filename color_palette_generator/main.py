from flask import Flask, render_template, request
import random

app = Flask(__name__)


# Function to generate random color palette
def generate_color_palette(num_colors=5):
    """Generate a list of random hex color codes."""
    colors = []
    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors


# Home route to display the color palette generator
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_colors = int(request.form.get('num_colors', 5))
        color_palette = generate_color_palette(num_colors)
    else:
        color_palette = generate_color_palette()
    return render_template('index.html', color_palette=color_palette)


if __name__ == '__main__':
    app.run(debug=True)
