from helpers.application import app
from controller.GalinaceoController import galinaceos_bp


app.register_blueprint(galinaceos_bp)

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200

@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)