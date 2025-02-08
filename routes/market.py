from flask import Blueprint, render_template
from database.market import PRODUCTS, GITHUB_PAGE


market_route = Blueprint('market', __name__)

@market_route.route('/')
def market():
    return render_template('market.html', products=PRODUCTS, github_page=GITHUB_PAGE)
