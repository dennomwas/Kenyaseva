from flask import Blueprint

donor = Blueprint('donor', __name__)

from app.donors import views