from app import app
import sys, os

sys.path.insert(0, os.path.dirname(__file__))

app.run(debug=True)
