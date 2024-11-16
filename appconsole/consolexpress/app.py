from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections
import time
from fuzzywuzzy import fuzz  # Importar fuzzywuzzy para coincidencia aproximada

# Definición de pares de preguntas y respuestas
pairs = [
    # Saludos
    (r"hola|buenas|buenos dias|buenas tardes|buenas noches|hey|que hondas|hi|hello", ["¡Hola! ¿En qué puedo ayudarte hoy?"]),
    # presentaciones y especificaciones
    (r"Hay presentacion?|presentacion|presentacion hay|presentacion tienen", [
    "Sí, tenemos presentaciones completas de cada consola. Si quieres saber las presentaciones de cada una, elige la opción que deseas ver:\n"
    "1 - Switch v1\n"
    "2 - Switch v2\n"
    "3 - Switch Oled\n"
    "4 - Switch Lite"
]),
(r"quienes crearon esta aplicacion?", ["nahun,cindy,yaritza "]),
   #categorias
    (r"categorias|hay categorias?|tienen categorias?|que categorias hay", [ "si hay categorias tenemos consolas especiales Normales y con acsesorios"]),

    (r"1", ["Cuando compras una Nintendo Switch V1, el paquete incluye la consola, dos Joy-Con (izquierdo y derecho), un dock para conectar a la TV, un soporte para los Joy-Con, dos correas para los Joy-Con, un cable HDMI y un adaptador de corriente. Este modelo fue el primero en lanzarse y tiene una duración de batería de aproximadamente 2.5 a 6.5 horas, dependiendo del juego."]),
    (r"2", ["La Nintendo Switch V2 es una versión mejorada de la V1 y viene con los mismos componentes: consola, dos Joy-Con, dock, soporte para los Joy-Con, dos correas, cable HDMI y adaptador de corriente. La diferencia principal es su duración de batería, que se ha mejorado para durar entre 4.5 y 9 horas."]),
    (r"3", ["En el caso de la Nintendo Switch OLED, el paquete incluye la consola con una pantalla OLED de 7 pulgadas, los dos Joy-Con, el dock (que además incluye un puerto LAN para conexión a Internet por cable), el soporte para los Joy-Con, dos correas para los Joy-Con, el cable HDMI y el adaptador de corriente. Este modelo ofrece colores más vibrantes y un almacenamiento interno de 64 GB en lugar de los 32 GB de las versiones anteriores."]),
    (r"4", ["Nintendo Switch Lite, que es un modelo exclusivamente portátil, incluye solo la consola con controles integrados y el adaptador de corriente, ya que no necesita dock ni accesorios adicionales."]),
    # Consultas sobre consolas
    (r"tienen consolas Nintendo Switch?|tienen consolas Nintendo Switch", ["Sí, tenemos consolas Nintendo Switch disponibles. ¿Te gustaría saber los precios?"]),
    (r"puedo comprar una consola Nintendo Switch?|puedo comprar una consola Nintendo Switch", ["Por supuesto, puedes comprarla directamente en nuestro sitio."]),
    (r"que modelos de Nintendo Switch tienen?|que modelos de Nintendo Switch tienen", ["Disponemos de varios modelos, incluyendo Nintendo Switch estándar, Nintendo Switch Lite, y Nintendo Switch OLED."]),
    
    # Ayuda general
    (r"ayuda|ayudame|necesito ayuda", [
        "¡Claro! Estoy aquí para ayudarte. La Nintendo Switch es una consola versátil que permite jugar tanto en modo portátil como en la televisión. Modelos como la Nintendo Switch estándar y la Nintendo Switch OLED se pueden conectar a la TV. ¿Quieres saber más detalles sobre sus características o juegos disponibles?"
    ]),
    
    # Precios
    (r"cuales son los precios de las consolas?|cuales son los precios?|los precios?|que precio estan las nintendo|que precio estan las nintendo?|los precios de las consolas|los precios de las consolas?", [
        "Aquí tienes los precios de las consolas Nintendo Switch:\n"
        "- Nintendo Switch (Versión 1): $299.99\n"
        "- Nintendo Switch (Versión 2): $299.99\n"
        "- Nintendo Switch OLED: $349.99\n"
        "- Ediciones especiales de Nintendo Switch (como la edición especial de Mario): $349.99."
    ]),
    (r"cuanto cuesta la Nintendo Switch?|cuanto cuesta la Nintendo Switch|que precio esta la switch|que precio esta la switch?|que precio estan las consolas|que precio estan las consolas?", [
        "El precio de la Nintendo Switch (Versión 1) es de $299.99."
    ]),
    (r"hay algun descuento en las consolas Nintendo Switch?|hay algun descuento?|hay algun descuento", ["Actualmente, estamos ofreciendo un descuento del 10% en la compra de una consola."]),
    
    # Variaciones sobre precios
    (r"que cuesta la consola?|precios?|que cuestan las consolas?|que cuesta la switch|que cuesta la switch?|quiero saber los precios de las consolas", [
        "Aquí tienes los precios de las consolas Nintendo Switch:\n"
        "- Nintendo Switch (Versión 1): $299.99\n"
        "- Nintendo Switch (Versión 2): $299.99\n"
        "- Nintendo Switch OLED: $349.99\n"
        "- Ediciones especiales: $349.99."
    ]),
    (r"cuanto vale la consola?|cuanto vale la consola", ["El precio de la Nintendo Switch (Versión 1) es de $299.99."]),
    (r"que precio tiene la Nintendo Switch?|que precio tiene la Nintendo Switch", ["El precio actual es de $299.99 para la versión estándar."]),
    (r"que cuesta la Nintendo Switch?|que cuesta la Nintendo Switch", [
        "La Nintendo Switch (Versión 1) está a la venta por $299.99.\n"
        "La Nintendo Switch OLED está a $349.99.\n"
        "Las ediciones especiales cuestan $349.99."
    ]),
    (r"cuanto es el precio de las consolas?|que precio estan las consolas?", [
        "Los precios son:\n"
        "- Versión 1: $299.99\n"
        "- Versión 2: $299.99\n"
        "- OLED: $349.99\n"
        "- Ediciones especiales: $349.99."
    ]),
    (r"regalame una consola?| regalame una|regalame una consola", ["Lo siento, no puedo regalarte una consola, pero puedo ayudarte a comprar una."]),
    
    # Recomendaciones
    (r"cual me recomiendas?|cual me recomiendas|cual nintendo me recomiendas|cual nintendo me recomiendas?", [
        "Si vas empezando en el mundo de las consolas, te recomiendo la versión 1, ya que con esta consola podrás jugar en la televisión y en modo portátil a la vez."
    ]),
    
    # Juegos
    (r"hay juegos disponibles?|hay juegos disponibles", ["Sí, tenemos una variedad de juegos. ¿Te gustaría saber más sobre algún juego en particular?"]),
    (r"cuales son los mejores juegos para Nintendo Switch?|cuales son los mejores juegos", ["Algunos de los mejores juegos incluyen 'The Legend of Zelda: Breath of the Wild', 'Animal Crossing: New Horizons' y 'Super Mario Odyssey'."]),
    (r"que juegos tienen en stock?|que juegos tienen", ["Contamos con juegos como 'Splatoon 2', 'Mario Kart 8 Deluxe' y 'Super Smash Bros. Ultimate'."]),
    
    # Métodos de pago
    (r"cuales son los metodos de pago?|cuales son los metodos de pago", ["Aceptamos tarjetas de crédito, PayPal y transferencias bancarias."]),
    (r"puedo pagar con tarjeta de debito?|puedo pagar con tarjeta de debito o credito?", ["Sí, puedes pagar con tarjeta de débito y crédito."]),

    # Envío
    (r"cuanto tiempo tarda el envío?|cuanto tiempo tarda el envío", ["El envío tarda entre 3 a 5 días hábiles."]),
    (r"como funciona el envio?|como funciona el envio", ["Realizamos envíos a todo el país y puedes rastrear tu pedido una vez enviado."]),
    
    # Devoluciones
    (r"tienen politica de devoluciones?|tienen politica de devoluciones", ["Sí, aceptamos devoluciones dentro de los 30 días después de la compra."]),
    (r"como puedo devolver un producto?|como puedo devolver un producto", ["Para devolver un producto, simplemente contacta nuestro servicio al cliente y te guiaremos."]),
    
    # Soporte
    (r"que hago si tengo un problema con mi consola?|que hago si tengo un problema con mi consola", ["Si tienes un problema, por favor contáctanos a nuestro soporte técnico y estaremos encantados de ayudarte."]),
    (r"hay garantia para las consolas?|hay garantia para las consolas", ["Sí, todas nuestras consolas vienen con una garantía de un año."]),
    (r"y si se me quiebra?|y si se me quiebra la consola", ["Si se te quiebra no tiene garantía ya que no es desperfecto del equipo."]),
    
    # Agradecimientos y despedidas
    (r"gracias|muchas gracias|te agradezco|gracias por tu ayuda", ["¡De nada! Si tienes más preguntas, no dudes en preguntar."]),
    (r"adios|hasta luego|nos vemos|hasta pronto", ["¡Hasta luego! Que tengas un buen día."]),
]

# Inicializando el chatbot
chatbot = Chat(pairs, reflections)

# Configuración de la aplicación Flask
app = Flask(__name__)

# Función para encontrar la pregunta más cercana usando fuzzywuzzy
def get_closest_match(user_input):
    closest_match = None
    highest_score = 0
    for pattern, responses in pairs:
        score = fuzz.ratio(user_input, pattern)  # Calcular similitud
        if score > highest_score:
            highest_score = score
            closest_match = responses[0]
    return closest_match if highest_score >= 60 else "Lo siento, no entiendo lo que quieres consultar."

@app.route("/")
def home():
    return render_template("chatbotIA.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = chatbot.respond(user_input)
    
    # Si no hay respuesta exacta, buscar coincidencia aproximada
    if response is None:
        response = get_closest_match(user_input)
    
    time.sleep(0.3)  # Esperar 0.3 segundos antes de enviar la respuesta
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
