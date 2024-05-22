import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import pandas as pd
import random
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.callable
def get_verse_by_id(identifier):
    # Check if there is an existing mapping for this identifier
    mapping = app_tables.identifier_to_verse.get(identifier=identifier)
    
    if mapping:
        # If there's a mapping, fetch the verse
        verse_row = mapping['verse']
    else:
        # If there's no mapping, assign a new verse randomly
        verse_row = random.choice(list(app_tables.bibleverses.search()))
        app_tables.identifier_to_verse.add_row(identifier=identifier, verse=verse_row)
    
    return {
        "reference": verse_row['reference'],
        "verse": verse_row['verse']
    }

@anvil.server.callable
def initialize_device():
    # Generate a new unique identifier for the device
    import uuid
    new_identifier = str(uuid.uuid4())
    
    # Return the new identifier
    return new_identifier