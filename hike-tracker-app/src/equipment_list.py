from flask import Blueprint, render_template

equipment_list_bp = Blueprint('equipment_list', __name__)

@equipment_list_bp.route('/equipment')
def equipment_list():
    # Fetch equipment list from the database
    equipment = [
        {'id': 1, 'name': 'Tent', 'type': 'Camping', 'weight': 2000, 'quantity': 1},
        {'id': 2, 'name': 'Backpack', 'type': 'Gear', 'weight': 1500, 'quantity': 1},
        {'id': 3, 'name': 'Water Bottle', 'type': 'Accessory', 'weight': 500, 'quantity': 2}
    ]
    return render_template('equipment_list.html', equipment=equipment)