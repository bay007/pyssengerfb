# https://wiki.python.org/moin/PyUnit
import unittest
import pyssengerfb as p


class Test_message_text(unittest.TestCase):

    def test_mensaje_texto(self):
        texto = "Hola mundo"
        m = p.Message.text(texto)
        self.assertEqual(m, {"message": {"text": texto}})

    def test_mensaje_texto_vacio(self):
        self.texto = ""
        self.assertRaises(Exception, p.Message.text(self.texto))

    def test_mensaje_texto_no_cadena(self):
        self.texto = 232
        self.assertRaises(Exception, p.Message.text(self.texto))

    def test_mensaje_texto_nulo(self):
        self.assertRaises(Exception, p.Message.text())


class Test_message_image(unittest.TestCase):
    def test_message_image(self):
        image_url = "https://ep00.epimg.net/elpais/imagenes/2015/12/28/paco_nadal/1451287800_145128_1451287800_noticia_normal.jpg"
        m = p.Message.image(image_url)
        self.assertEqual(
            m, {"message": {"attachment": {"type": "image", "payload": {"url": image_url}}}})

    def test_message_image_vacio(self):
        image_url = ""
        self.assertRaises(Exception, p.Message.image(image_url))

    def test_message_image_no_cadena(self):
        image_url = 123
        self.assertRaises(Exception, p.Message.image(image_url))

    def test_message_image_nulo(self):
        self.assertRaises(Exception, p.Message.image())


class Test_message_quick_reply(unittest.TestCase):
    def test_quick_reply(self):
        message = "¿Deseas algo mas?"
        quick_reply = ["Si"]
        m = p.Message.quick_reply(mensaje=message, titles=quick_reply)
        self.assertEqual(m, {"message": {"text": message, "quick_replies": [
                         {"content_type": "text", "title": "Si", "payload": "Si"}]}})

    def test_quick_reply_vacios(self):
        message = ""
        quick_reply = []
        self.assertRaises(Exception, p.Message.quick_reply(
            mensaje=message, titles=quick_reply))

        message = ""
        quick_reply = ["Si"]
        self.assertRaises(Exception, p.Message.quick_reply(
            mensaje=message, titles=quick_reply))

        message = "¿Necesitas algo mas?"
        quick_reply = []
        self.assertRaises(Exception, p.Message.quick_reply(
            mensaje=message, titles=quick_reply))

    def test_quick_reply_nulos(self):
        self.assertRaises(Exception, p.Message.quick_reply())
        self.assertRaises(Exception, p.Message.quick_reply(mensaje="Hey"))
        self.assertRaises(Exception, p.Message.quick_reply(titles=["Si"]))


class Test_sender_action(unittest.TestCase):
    def test_sender_action(self):
        m = p.Message.sender_action(True)
        self.assertEqual(m, {"sender_action": "typing_on"})

        m2 = p.Message.sender_action(False)
        self.assertEqual(m2, {"sender_action": "typing_off"})

        m3 = p.Message.sender_action()
        self.assertEqual(m3, {"sender_action": "typing_off"})

    def test_sender_action_no_boleano(self):
        self.assertRaises(Exception, p.Message.sender_action(12))
        self.assertRaises(Exception, p.Message.sender_action([]))
        self.assertRaises(Exception, p.Message.sender_action({}))
        self.assertRaises(Exception, p.Message.sender_action(()))


if __name__ == '__main__':
    unittest.main()
