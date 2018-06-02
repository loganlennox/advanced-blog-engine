from app import app

# Error handling
@app.errorhandler(404)
def not_found(error):
    return "<h1>Page not found</h1>"
