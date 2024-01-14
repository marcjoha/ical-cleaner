import os
from flask import Flask, Response
from ics import Calendar
import requests

ICS_URL = '__REPLACE__'

app = Flask(__name__)

@app.route('/')
def main():

    cal = Calendar(requests.get(ICS_URL).text)

    # Remove all events which names start with 'Check', i.e. Check-in or Check-out
    cal.events = [event for event in cal.events if not event.name.startswith('Check') ]

    # The trip names used in the full day events are suffixed by month a year which is unnecessary
    for event in cal.events:
        if event.all_day:
            event.name = event.name[0:event.name.rfind(',')]

    return Response(cal.serialize(), mimetype='text/calendar', headers={'Content-disposition': 'attachment; filename=tripit.ics'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
