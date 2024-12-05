from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.programming.framework import Flask
from diagrams.programming.language import Python
from diagrams.generic.database import SQL

with Diagram("Pix2Code Implementation UML", filename="pix2code_detailed", show=False):

    # User Interface Cluster
    with Cluster("Flask Interface"):
        user = User("User")
        image_upload = Flask("Image Upload")
        code_output = Flask("Code Output")
        
        user >> image_upload >> code_output

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
