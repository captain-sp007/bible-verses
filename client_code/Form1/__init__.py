from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

        # Get the random verse from the server
        verse_data = anvil.server.call('get_random_verse')
        
        # Set the labels with the verse and reference
        self.verse_label.text = verse_data['verse']
        self.reference_label.text = verse_data['reference']

