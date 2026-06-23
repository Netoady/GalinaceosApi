from helpers.application import app
from controller.ClasseCbcaGalController import classcbcagal_bp
from controller.CodigoTerritorialController import codigoterritorial_bp
from controller.NivelTerritorialController import nivelterritorial_bp
from controller.NomeTerritorioController import nometerritorio_bp
from controller.SistemaCriacaoController import sistemacriacao_bp
from controller.GalinaceoController import galinaceos_bp

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200

if __name__ == "__main__":
    # Mudamos explicitamente para a porta 5001 e ativamos o modo debug
    app.run(debug=True, port=5001)

app.register_blueprint(classcbcagal_bp)
app.register_blueprint(codigoterritorial_bp)
app.register_blueprint(nivelterritorial_bp)
app.register_blueprint(nometerritorio_bp)
app.register_blueprint(sistemacriacao_bp)
app.register_blueprint(galinaceos_bp)

