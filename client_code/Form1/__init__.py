from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
from anvil import *
import anvil.server
import anvil.server
import random



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


        # Define the Bible verses
        bible_verses = [
            {"reference": "John 3:16", "verse": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."},
            {"reference": "Psalm 23:1", "verse": "The Lord is my shepherd, I lack nothing."},
            {"reference": "Philippians 4:13", "verse": "I can do all this through him who gives me strength."},
            # Add more verses as needed
        ]

        # Bind the bible_verses data to the DataGrid
        self.data_grid_1.items = bible_verses

