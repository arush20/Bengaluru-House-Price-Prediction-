from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    respose = jsonify({
        'locations' :util.get_location_names()

    })
    response.headers.add

if __name__ == "__main__":
    print("starting pyhton flask server")
    app.run()