from multi_label_pigeon import multi_label_annotate
from IPython.display import display, Image

annotations = multi_label_annotate(
    ['assets/altera.jpg', 'assets/chibi_gil.jpg', 'assets/chibi_saber.jpg'],
    options={'cute': ['yes', 'no'], 'saber': ['yes', 'no'],
             'colors': ['blue', 'gold', 'white', 'red']},
    display_fn=lambda filename: display(Image(filename))
)

dict(annotations)
