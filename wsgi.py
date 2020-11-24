"""Entry point for gunicorn runner."""
from app import create_app
from dotenv import load_dotenv

load_dotenv()
app = create_app()
