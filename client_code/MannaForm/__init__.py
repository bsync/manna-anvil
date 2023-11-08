from ._anvil_designer import MannaFormTemplate
from anvil import *
import anvil.server

class MannaForm(MannaFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    result = anvil.server.call('load_vids')

