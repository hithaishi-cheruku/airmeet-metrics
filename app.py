from flask import Flask, request, jsonify
# from flask_caching import Cache

# config = {
#     "DEBUG": True,          # some Flask specific configs
#     "CACHE_TYPE": "simple", # Flask-Caching related configs, we can use Redis if available 
#     "CACHE_DEFAULT_TIMEOUT": 300
# }

app = Flask(__name__)

# tell Flask to use the above defined config
# app.config.from_mapping(config)
# cache = Cache(app)

metrics_all = []
@app.route('/')
def hello_world():
    """
    Health check for the system
    """
    return 'Hello, World!'


@app.route('/metrics', methods=['POST'])

def metrics():
    """
    Updates the metrics in system
    """
    remote_add = request.remote_addr
    if not request.is_json:
        # Check valid payload
        return "Not a valid payload"
    metrics_json = request.get_json()
    metrics_json.update({"ip": remote_add})

    # if cache is needed
    # cache_all = cache.get('metrics')
    # if cache_all is None:
    #     cache.set('metrics', metrics_json)
    # cache.set('metrics', cache_all)
    metrics_all.append(metrics_json)
    return "Updated the system metrics"

@app.route('/report')
def get_report():
    """
    returns report of all records in system
    """
    return jsonify(metrics_all)

def main():
    """

    """
    app.run(debug=True)