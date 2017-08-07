![estado](https://travis-ci.org/bay007/pyssengerfb.svg?branch=master)
# pyssengerfb
pyssengerfb es una opción para manejar la API de Facebook Messenger en Python.
 - Envío de mensajes de [texto].
 - Envío de [imagenes].
 - Envío de estados [escribiendo].
 - Envío de botones de [rápida respuesta].
 - Envío de botones [agrupados].
 - Envío de [cuadros] con imágenes informativas.

## Uso
```python
import pyssengerfb as pfb
import os
import time

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "-")
CLIENT_ID = os.getenv("CLIENT_ID", "-")

# Declaramos el Elemento base
page = pfb.Page(ACCESS_TOKEN)

# Uso de mensaje basico
message = pfb.Message.text("Hola Mundo")
page.send(sender_id=CLIENT_ID, mensaje=message)

# Envio de imagen
image_URL = "https://lh3.googleusercontent.com/Yh6ZlCb8dQIDIwAWbwd2jboFCyTqq8wc2xbLMs9ykYemOX3vjOTtT6Npfbk-jFkCciwY=w300"
message_imagen = pfb.Message.image(image_URL)
page.send(sender_id=CLIENT_ID, mensaje=message_imagen)

# Button Template
button_1 = pfb.Message.button_postback(
    title="El texto que se muestra en el boton")
button_2 = pfb.Message.button_web(
    title="Buscador...", url="https://www.google.com")
button_template = pfb.Template.button_template(
    title="Este es un grupo de botones", buttons=[button_1, button_2])
page.send(sender_id=CLIENT_ID, mensaje=button_template)

# Button Generic Template
avion_imagen = "https://ep00.epimg.net/elpais/imagenes/2015/12/28/paco_nadal/1451287800_145128_1451287800_noticia_normal.jpg"
button_3 = pfb.Message.button_postback(title="Elemento 3")
generic_template_element_a = pfb.Message.generic_template_element(
    title="Elemento1", subtitle="Subtitulo", image_url=image_URL, url="https://www.google.com", buttons=[button_1, button_2])
generic_template_element_b = pfb.Message.generic_template_element(
    title="A volar", subtitle="Vuelo comercial", image_url=avion_imagen, buttons=[button_3, button_2])

generic_template = pfb.Template.generic_template(
    [generic_template_element_a, generic_template_element_b])
page.send(sender_id=CLIENT_ID, mensaje=generic_template)

# Quick reply
quick_reply = pfb.Message.quick_reply(
    "¿Desea mas informacion?", ["Si", "No", "Mas tarde"])
page.send(sender_id=CLIENT_ID, mensaje=quick_reply)

# Sender actions
sender_Action = pfb.Message.sender_action(True)
page.send(sender_id=CLIENT_ID, mensaje=sender_Action)
time.sleep(4)
sender_Action = pfb.Message.sender_action()
page.send(sender_id=CLIENT_ID, mensaje=sender_Action)

```

[rápida respuesta]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies
[imagenes]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
[texto]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
[escribiendo]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions
[agrupados]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
[cuadros]:https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template

Version
----

0.1.0
