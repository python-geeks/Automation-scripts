# Color Palette Generator

## Short Description
This is a simple web application built with Flask that generates a random color palette. Users can specify the number of colors in the palette (between 1 and 10), and the app will display the corresponding colors in a visually appealing way.

## Functionality
- Generate random color palettes with customizable color count.
- Display color hex codes for each generated color.
- Interactive UI to adjust the number of colors displayed.

## Folder Structure
    
    color_palette_generator/
    │
    ├── app.py               # Main Flask application file
    ├── templates/
    │   └── index.html       # HTML template for the app
    ├── requirements.txt     # Python dependencies file
    └── README.md            # Instructions for the program
    

## Instructions for Each File:
1. app.py:
The main Flask application script, which generates random color palettes and serves them via a web interface.

2. templates/index.html:
HTML file that displays the color palette on the front end and allows the user to input the number of colors.

3. requirements.txt:
List of dependencies required to run the project.

## Setup Instructions
1. Clone the repository or download the project files.
2. Navigate to the project folder in your terminal:
   ```bash
   cd color_palette_generator
   ```
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```
5. Open your browser and go to http://127.0.0.1:5000/ to use the app.


## Detailed Explanation
- The app.py script creates a Flask web server that serves an HTML page (index.html) where users can generate color palettes.
- The generate_color_palette() function in app.py generates a list of random hexadecimal colors using the random module.
- The front-end (index.html) uses a form to capture the user's input for the number of colors, and the results are displayed using a simple CSS grid for visualization.
- Each color is displayed as a square with its corresponding hex code.

## Output

![Output](image.png)

## Author(s)
explooit
https://github.com/ExPl0iT-29

## Disclaimers
- The project uses random color generation and does not guarantee aesthetically balanced palettes.