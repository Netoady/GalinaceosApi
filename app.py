from helpers.application import app, api
from controller.IndexController import IndexController, HealthController
from controller.AvicultorController import AvicultoresController, AvicultorController
from controller.AviculaController import AviculasController, AviculaController
from controller.EnderecoController import EnderecosController, EnderecoController
from controller.GalpaoController import GalpoesController, GalpaoController
from controller.GalinaceoController import GalinaceosController

# Health / Index
api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')

# Endpoints Unificados
api.add_resource(AvicultoresController, '/avicultores')
api.add_resource(AvicultorController, '/avicultores/<int:avicultor_id>')

api.add_resource(AviculasController, '/aviculas')
api.add_resource(AviculaController, '/aviculas/<int:avicula_id>')

api.add_resource(EnderecoController, '/enderecos')

api.add_resource(GalpoesController, '/galpoes')
api.add_resource(GalpaoController, '/galpoes/<int:galpao_id>')

api.add_resource(GalinaceosController, '/galinaceos')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)