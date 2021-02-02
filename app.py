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
metrics_store = dict()
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
    
    cur_cpu = metrics_json.get('percentage_cpu_used')
    cur_mem = metrics_json.get('percentage_memory_used')
    metrics_json.update({"ip": remote_add})
    new_metrics = {'ip': remote_add,'max_cpu': cur_cpu,'max_memory': cur_mem }

    if metrics_store.get(remote_add) is not None:

        old_cpu = metrics_json.get('percentage_cpu_used')
        old_mem = metrics_json.get('percentage_memory_used')

        new_metrics = {'ip': remote_add, 'max_cpu': max(cur_cpu, old_cpu),'max_memory': max(cur_mem, old_mem)}
        
        metrics_store.pop(remote_add)
        
    metrics_store.update({remote_add: new_metrics})
    metrics_all.append(metrics_json)
    
    return "updated"

@app.route('/report')
def get_report():
    """
    returns report of all records in system
    """
    remote_add = request.remote_addr
    if metrics_store.get(remote_add) is None:
        return "invalid"
    metrics_list = []
    for metric in metrics_store.values():
        metrics_list.append(metric)

    return jsonify(metrics_list)

def main():
    """

    """
    app.run(debug=True)
