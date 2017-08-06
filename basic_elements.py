import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Message(object):
    def __init__(self):
        pass

    @staticmethod
    def to_json(mensaje):
        try:

            if not isinstance(mensaje, str):
                raise Exception("El mensaje debe ser una cadena de texto")
            mensaje = mensaje.strip()

            if mensaje.__len__() < 1:
                raise Exception("La cadena no debe ser vacia")

            return {
                "message": {
                    "text": mensaje
                }
            }
        except Exception as error:
            logging.critical(error, exc_info=True)
