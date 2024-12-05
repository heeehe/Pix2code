from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.programming.framework import Flask
from diagrams.programming.language import Python
from diagrams.generic.database import SQL
from graphviz import Digraph


class CustomDiagram(Diagram):
    """Custom Diagram class to adjust text properties and other styling."""
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.dot = Digraph(self.name)
        self.dot.attr('node', fontname="Arial Bold", fontsize="14", color="black")

with CustomDiagram("Pix2Code Implementation UML", filename="pix2code_styled", show=False):

    # User Interface Cluster
    with Cluster("Flask Interface"):
        user = User("User")
        image_upload = Flask("Image Upload")
        process_image = Flask("Process Image")
        code_output = Flask("Code Output")
        
        user >> image_upload >> process_image >> code_output

    # Pix2Code Model Cluster
    with Cluster("Pix2Code Model"):
        image_encoder = Python("Image Encoder (CNN)")
        context_encoder = Python("Context Encoder (RNN)")
        decoder = Python("Decoder (RNN)")

        image_encoder >> context_encoder >> decoder

    # Data Preprocessing Cluster
    with Cluster("Data Preprocessing"):
        dataset = SQL("Dataset")
        vocabulary = Python("Vocabulary Class")
        dataset >> vocabulary >> image_encoder

    # Training Process Cluster
    with Cluster("Training"):
        loss_function = Python("Cross-Entropy Loss")
        optimizer = Python("SGD Optimizer")
        
        decoder >> loss_function >> optimizer
        optimizer >> image_encoder

    # Connecting Flask Interface with the Model
    image_upload >> image_encoder
    decoder >> code_output
