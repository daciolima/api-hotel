from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('username', type=str, required=True, help="Informe username")
argumentos.add_argument('password', type=str, required=True, help="Informe password")


class UserRegister(Resource):

    def post(self):
        dados = argumentos.parse_args()

        if UserModel.find_user_by_usename(dados['username']):
            return {"message": f"Usuário {dados['username']} já existe."}, 200

        try:
            user = UserModel(**dados)
            user.save_user()
            return {"message": f"Usuario {dados['username']} criado com sucesso."}, 201
        except:
            return {"message": "Erro ao salvar user."}, 500


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = argumentos.parse_args()

        user = UserModel.find_user_by_usename(dados['username'])

        if user and safe_str_cmp(user.password, dados['password']):
            token_access = create_access_token(identity=user.user_id)
            return {'access_token': token_access}, 200
        return {"message": "Username ou password estão incorretos"}


class UserLogout(Resource):

    @jwt_required
    def post(cls):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {"message": "Usuário deslogado com sucesso."}, 200


class UserAll(Resource):
    def get(self):
        users_encontrados = UserModel.user_all()
        if users_encontrados:
            return {"users": [user.json() for user in users_encontrados]}
        return {"message": "Nenhum usuário cadastrado"}


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user_by_id(user_id)
        if user:
            return user.json()
        return {'mensagem': 'User não encontrado.'}, 404

    @jwt_required
    def put(self, user_id):
        dados = argumentos.parse_args()
        user_encontrado = UserModel.find_user_by_id(user_id=user_id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            try:
                user_encontrado.save_user()
                return user_encontrado.json(), 200
            except:
                return {"message": "Erro ao salvar user."}, 500
        return {"message": "User não encontrado."}, 404

    @jwt_required
    def delete(self, user_id):
        user_encontrado = UserModel.find_user_by_id(user_id=user_id)
        usuario = user_encontrado.username
        if user_encontrado:
            try:
                user_encontrado.delete_user()
                return {"message": f"Usuário {usuario} deletado."}
            except:
                return {"message": "Erro ao deletar user."}, 500
        return {"message": "User não encontrado."}, 404

