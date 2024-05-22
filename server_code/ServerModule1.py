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

# Load the CSV file
@anvil.server.callable
def get_random_verse():
    df = pd.read_csv(anvil.server.get_app_origin() + "/_/anvil/media/bible_verses.csv")
    
    # Use the device's unique ID for a consistent "random" verse
    device_id = anvil.server.get_current_device()['id']
    random.seed(device_id)
    
    random_verse = df.sample(1).iloc[0]
    
    return {
        'reference': random_verse['reference'],
        'verse': random_verse['verse']
    }
