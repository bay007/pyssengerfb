import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Message(object):
    def __init__(self):
        pass

    @staticmethod
    def text(mensaje):
        try:

            if not isinstance(mensaje, str):
                raise Exception("El mensaje debe ser una cadena de texto")
            mensaje = mensaje.strip()

            if mensaje.__len__() < 1:
                raise Exception("El mensaje no debe ser vacio")

            return {
                "message": {
                    "text": mensaje
                }
            }
        except Exception as error:
            logging.critical(error, exc_info=True)

    @staticmethod
    def image(url):
        try:

            if not isinstance(url, str):
                raise Exception("la URL debe ser una cadena de texto")
            url = url.strip()

            if url.__len__() < 1:
                raise Exception("La URL no debe ser vacia")

            return {
                "message": {
                    "attachment": {
                        "type": "image",
                        "payload": {
                            "url": url
                        }
                    }
                }
            }
        except Exception as error:
            logging.critical(error, exc_info=True)
