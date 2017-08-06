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
                raise Exception("La URL debe ser una cadena de texto")
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

    @staticmethod
    def quick_reply(mensaje=None, titles=[]):
        try:
            if not isinstance(titles, list) or len(titles) == 0:
                raise Exception(
                    "Los botones deben estar contenidos en una lista no vacia")

            if not isinstance(mensaje, str):
                raise Exception("El mensaje debe ser una cadena de texto")
            mensaje = mensaje.strip()

            if len(mensaje) == 0:
                raise Exception("El mensaje no debe ser vacio")

            elementos = []
            for title in titles:
                if not isinstance(title, str) or len(title.strip()) == 0:
                    raise Exception(
                        "El boton a mostrar debe ser una cadena no vacía")
                elementos.append({
                    "content_type": "text",
                    "title": title.strip(),
                    "payload": title.strip()
                })

            return {"message": {
                "text": mensaje,
                "quick_replies": elementos}}
        except Exception as error:
            logging.critical(error, exc_info=True)

    @staticmethod
    def sender_action(isON=False):
        if not isinstance(isON, bool):
            raise Exception("El valor debe ser de tipo boleano")
        return {
            "sender_action": "typing_on" if isON else "typing_off"
        }
