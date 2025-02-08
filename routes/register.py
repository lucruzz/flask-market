from flask import Blueprint, render_template


register_route = Blueprint('register', __name__)

@register_route.route('/')
def register():
    return render_template('register.html')