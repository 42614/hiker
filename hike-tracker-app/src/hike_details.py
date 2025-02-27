from flask import Blueprint, render_template

hike_details_bp = Blueprint('hike_details', __name__)

@hike_details_bp.route('/hike/<int:hike_id>')
def hike_details(hike_id):
    # Fetch hike details from the database
    hike = {
        'id': hike_id,
        'date': '2025-02-27',
        'location': 'Mountain Trail',
        'distance': 10,
        'duration': 120,
        'equipment': ['Tent', 'Backpack', 'Water Bottle']
    }
    return render_template('hike_details.html', hike=hike)