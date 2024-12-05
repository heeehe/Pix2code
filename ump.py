from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.onprem.compute import Server
from diagrams.programming.framework import Flask
from diagrams.programming.language import Python
from diagrams.generic.database import SQL

with Diagram("Pix2Code Implementation UML", show=False):

    with Cluster("Pix2Code Model"):
        image_encoder = Python("Image Encoder (CNN)")
        context_encoder = Python("Context Encoder (RNN)")
        decoder = Python("Decoder (RNN)")
        
        image_encoder >> context_encoder >> decoder

    with Cluster("Data Preprocessing"):
        dataset = SQL("Dataset")
        vocabulary = Python("Vocabulary Class")
        dataset >> vocabulary >> image_encoder

    with Cluster("Flask Interface"):
        user = Flask("User Interface")
        user_upload = Flask("Image Upload")
        code_output = Flask("Code Output")
        
        user >> user_upload >> image_encoder
        decoder >> code_output >> user

    with Cluster("Training"):
        loss_function = Python("Cross-Entropy Loss")
        optimizer = Python("SGD Optimizer")
        decoder >> loss_function >> optimizer
        optimizer >> image_encoder

