from flask import Flask, render_template
from app.routes import weather_bp

app = Flask(__name__, template_folder="app/templates")  # Explicitly set template path
app.register_blueprint(weather_bp)

if __name__ == "__main__":
    app.run(debug=True)
