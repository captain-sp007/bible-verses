import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import random
import anvil.email
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
def get_random_verse():
    # Fetch all rows from the BibleVerses table
    rows = app_tables.bibleverses.search()
    
    # Convert to a list
    rows_list = list(rows)
    
    # Select a random row
    random_row = random.choice(rows_list)
    
    return {
        "reference": random_row['reference'],
        "verse": random_row['verse']
    }

@anvil.server.callable
def send_verse_to_email(email, verse_data):
    
    anvil.email.send(
        to=email,
        from_name="Le Réveil des Mères Sentinelles",       
        subject="Ma carte prophétique",
        html=f"<b>{verse_data['reference']}</b>: {verse_data['verse']}",
       
    )