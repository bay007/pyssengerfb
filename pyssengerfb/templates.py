
class Template(object):
    @staticmethod
    def button_template(title=None, buttons=[]):
        elements = []

        if not isinstance(buttons, list) or len(buttons) == 0:
            raise Exception(
                "Los botones deben ser contenidos en una lista no vacia")

        if len(buttons) > 3:
            raise Exception("El numero de botones no puede exceder de 3")

        if not isinstance(title, str):
            raise Exception(
                "El titulo de los botones debe ser una cadena de texto")
        title = title.strip()

        if len(title) == 0:
            raise Exception("El titulo de los botones no debe ser vacio")

        for button in buttons:
            if not isinstance(button, dict):
                raise Exception(
                    "Parece ser un boton no valido_")
            elements.append(button)

        return {
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                            "template_type": "button",
                            "text": title,
                            "buttons": elements
                    }
                }
            }
        }

    @staticmethod
    def generic_template(elements=[]):
        if not isinstance(elements, list):
            raise Exception("Los elementos deben ser contenidos en una lista")

        if 0 >= len(elements) or len(elements) >= 11:
            raise Exception(
                "Solo puede haber entre 1 y 10 elementos, hay {}".format(len(elements)))

        return {
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
            }
        }
