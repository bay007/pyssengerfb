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

            if len(titles) > 11:
                raise Exception(
                    "No se pueden mostrar mas de 11 botones a la vez de tipo quick reply")

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

    @staticmethod
    def button_web(url=None, title=None):
        try:
            if not isinstance(title, str) or len(title.strip()) == 0:
                raise Exception(
                    "El boton a mostrar debe ser una cadena no vacía")

            if not isinstance(url, str) or len(url.strip()) == 0:
                raise Exception(
                    "LA URL debe ser una cadena no vacía")

            return {
                "type": "web_url",
                "url": url.strip(),
                "title": title.strip()
            }

        except Exception as error:
            logging.critical(error, exc_info=True)

    @staticmethod
    def button_postback(title=None):
        try:
            if not isinstance(title, str) or len(title.strip()) == 0:
                raise Exception(
                    "El boton a mostrar debe ser una cadena no vacía")

            return {
                "type": "postback",
                "title": title.strip(),
                "payload": title.strip()
            }

        except Exception as error:
            logging.critical(error, exc_info=True)

    @staticmethod
    def generic_template_element(title="", subtitle="", image_url="", url="", buttons=[]):

        if not isinstance(title, str):
            raise Exception("El titulo debe ser una cadena")
        title = title.strip()
        if 0 >= len(title) or len(title) >= 81:
            raise Exception(
                "El titulo debe tener entre 1 y 80 caracteres, hay {}".format(len(title)))

        if not isinstance(subtitle, str):
            raise Exception("El subtitle debe ser una cadena")
        subtitle = subtitle.strip()
        if 0 >= len(subtitle) or len(subtitle) >= 81:
            raise Exception(
                "El subtitle debe tener entre 1 y 80 caracteres, hay {}".format(len(subtitle)))

        if not isinstance(image_url, str):
            raise Exception("La image_url debe ser una cadena")
        image_url = image_url.strip()
        if len(image_url) == 0:
            raise Exception("La image_url debe ser una cadena no vacia")

        if not isinstance(url, str):
            raise Exception("La url debe ser una cadena")
        url = url.strip()

        if not isinstance(buttons, list):
            raise Exception("Los botones deben estar contenidos en una lista")

        if 0 >= len(buttons) or len(buttons) >= 4:
            raise Exception(
                "La lista de botones puede tener solo de 1 a 3 elementos, hay {}".format(len(buttons)))

        element = {
            "title": title,
            "subtitle": subtitle,
            "image_url": image_url,
            "buttons": buttons
        }

        if len(url) > 0:
            element.update({"default_action": {
                "type": "web_url",
                "url": url,
            }})

        return element
