from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.js



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
  
      # Set Form properties and Data Bindings.
      self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
      # Retrieve or initialize the unique identifier for the device
      self.identifier = self.get_device_identifier()
        
      # Fetch and display the verse
      self.display_persistent_verse()

  def get_device_identifier(self):
      # Try to get the identifier from the cookies
      identifier = anvil.js.window.document.cookie.split('; ').find(lambda x: x.startswith('device_identifier='))
        
      if identifier:
          identifier = identifier.split('=')[1]
      else:
          # If no identifier is found, initialize a new one
          identifier = anvil.server.call('initialize_device')
          # Set the identifier as a cookie with an expiration date far in the future
          anvil.js.window.document.cookie = f'device_identifier={identifier}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/'
        
      return identifier

  def display_persistent_verse(self):
      # Call the server function to get the verse for this identifier
      verse_data = anvil.server.call('get_verse_by_id', self.identifier)
        
      # Clear the current components in the column panel
      self.column_panel_1.clear()
        
      # Create Labels for the reference and verse
      reference_label = Label(text=verse_data["reference"], bold=True)
      verse_label = Label(text=verse_data["verse"], wrap_on='anywhere')
        
      # Add the labels to the ColumnPanel
      self.column_panel_1.add_component(reference_label)
      self.column_panel_1.add_component(verse_label)