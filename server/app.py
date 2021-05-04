from flask import Flask,jsonify

app = Flask(__name__)

malwares = [
  {
    'name': 'some name'
  }
]

#get /malware
@app.route('/get_malware')
def get_malware():
  return jsonify({'malwares': malwares})

app.run(port=5000)