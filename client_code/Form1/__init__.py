
from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import anvil.server
import random



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.

  #Test code to search the table with client code authorization OK to search into it
        # self.item = app_tables.bibleverses.search()[1]

    #Test code for 1 verse
        #self.item = {
        #  'reference': 'Proverbes 3:5-6',
        #   'verse': 'Confie-toi en l’Éternel de tout ton cœur, Et ne t’appuie pas sur ta sagesse ; Reconnais-le dans toutes tes voies, Et il aplanira tes sentiers',
        # }
      # Set Form properties and Data Bindings.
        self.init_components(**properties)




    # Any code you write here will run before the form opens.

        # Fetch a random verse when the form initializes
        self.display_random_verse()

  def display_random_verse(self):
        # Call the server function to get a random verse
        random_verse = anvil.server.call('get_random_verse')
        
        # Clear the current components in the column panel
        self.column_panel_1.clear()
        
        # Create Labels for the reference and verse
        reference_label = Label(text=random_verse["reference"], bold=True)
        verse_label = Label(text=random_verse["verse"])
        
        # Add the labels to the ColumnPanel
        self.column_panel_1.add_component(reference_label)
        self.column_panel_1.add_component(verse_label)
