# Why the empty __init__.py files? 
# They tell Python "this folder is an importable package." Without them, a line like from app.core import config can fail with a confusing error later.
