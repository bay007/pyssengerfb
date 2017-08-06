import requests
import os
from basic_elements import Message
import logging
import json
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


API_VERSION = 2.6


class Page(object):
    def __init__(self, access_token=None):

        self.BASE_URL = "https://graph.facebook.com/v2.6/me/messages?access_token={}"
        if access_token is None:
            raise Exception(
                "Debe especificarse un Page Access Token de FB")

        if not isinstance(access_token, str):
            raise Exception(
                "El page Access Token debe ser una cadena de texto")
        self.access_token = access_token.strip()

        if len(self.access_token) < 184:
            raise Exception(
                "Parece que este no es un token de longitud valida")

        self.BASE_URL = self.BASE_URL.format(self.access_token)

    def send(self, sender_id=None, mensaje=None):
        try:
            if mensaje is None:
                raise Exception("Se debe especificar un mensaje para enviar")

            if not isinstance(sender_id, str) or not isinstance(mensaje, dict):
                raise Exception(
                    "El sender ID debe ser una cadena de texto, el mensaje debe ser en formato json")

            self.sender_id = sender_id.strip()
            if len(self.sender_id) < 1:
                raise Exception("Sender ID debe no puede ser uan cadena vacia")

            _data = {}

            _data.update({"recipient": {"id": self.sender_id}})
            _data.update(mensaje)
            data = json.dumps(_data)

            headers = {"Content-Type": "application/json"}
            response = requests.post(self.BASE_URL,
                                     data=data, headers=headers)
            logger.info(response.text)
            logger.info(response.status_code)
        except Exception as error:
            logging.critical(error, exc_info=True)


"""
# Ejemplo para mandar un mensaje 
page = Page(os.getenv("PAGE_ACCESS_TOKEN"))
mensaje = Message.to_json("Hola Mundo")
page.send("1757084327651562", mensaje)
"""