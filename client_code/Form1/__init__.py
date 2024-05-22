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
  #Search the table with client code authorization to search into it
        self.item = app_tables.bibleverses.search()[1]

    #Test code for 1 verse
        #self.item = {
        #  'reference': 'Proverbes 3:5-6',
        #   'verse': 'Confie-toi en l’Éternel de tout ton cœur, Et ne t’appuie pas sur ta sagesse ; Reconnais-le dans toutes tes voies, Et il aplanira tes sentiers',
        # }
      # Set Form properties and Data Bindings.
        self.init_components(**properties)

    # Any code you write here will run before the form opens.


