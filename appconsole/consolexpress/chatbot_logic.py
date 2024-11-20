# Definición de pares de preguntas y respuestas
pairs = [
    # Saludos
    (r"hola|buenas|ola|holo|olo|buenos dias|oli|holi|buenas tardes|buenas noches|hey|que hondas|hi|hello", ["¡Hola! ¿En qué puedo ayudarte hoy?"]),
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
    (r"tienen consolas Nintendo Switch?|tienen consolas Nintendo Switch|tienen consolas?", ["Sí, tenemos consolas Nintendo Switch disponibles. ¿Te gustaría saber los precios?"]),
    (r"puedo comprar una consola Nintendo Switch?|puedo comprar una consola Nintendo Switch", ["Por supuesto, puedes comprarla directamente en nuestro sitio."]),
    (r"que modelos de Nintendo Switch tienen?|modelos?|que modelos hay?|que modelos de Nintendo Switch tienen", ["Disponemos de varios modelos, incluyendo Nintendo Switch estándar, Nintendo Switch Lite, y Nintendo Switch OLED."]),
    
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
    (r"regalame una consola?|regalame|regalame una|regalame una consola", ["Lo siento, no puedo regalarte una consola, pero puedo ayudarte a comprar una."]),
    
    # Recomendaciones
    (r"cual me recomiendas?|recomiendame?|cual me recomiendas|cual nintendo me recomiendas|cual nintendo me recomiendas?", [
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
    (r"hay garantia para las consolas?|tienen garantia las consolas?", ["Sí, todas nuestras consolas vienen con una garantía de un año."]),
    (r"y si se me quiebra?|y si se me quiebra la consola", ["Si se te quiebra no tiene garantía ya que no es desperfecto del equipo."]),

    #hay consolas
    (r"consolas?|hay consolas?|quiero saber si hay consolas?|necesito saber si hay consolas?", ["si tenemos consolas swicth hay variedad para escoger de cual quisieras saber? switch v1, switch v2, switch oled, switch lite"]),

    (r"switch v1", ["La Nintendo Switch V1 (modelo original) se lanzó en marzo de 2017 con un precio aproximado de $300 USD. Ofrece una pantalla LCD de 6.2 pulgadas (720p), Joy-Con desmontables y autonomía de batería de 2.5 a 6.5 horas."]),
     (r"switch v2", ["La Nintendo Switch V2, lanzada en agosto de 2019, mantiene el diseño del modelo original pero mejora la duración de la batería (4.5 a 9 horas), conservando el mismo precio de $300 USD."]),
      (r"switch oled", ["La Nintendo Switch Lite, disponible desde septiembre de 2019, tiene un precio de $200 USD, es exclusivamente portátil, cuenta con una pantalla LCD de 5.5 pulgadas y una batería de 3 a 7 horas. Finalmente,"]),
       (r"switch lite", ["la Nintendo Switch OLED, lanzada en octubre de 2021, mejora la pantalla (OLED de 7 pulgadas), duplica el almacenamiento a 64 GB y tiene una batería similar a la V2, con un costo de $350 USD"]),

    # Agradecimientos y despedidas
    (r"gracias|muchas gracias|te agradezco|gracias por tu ayuda", ["¡De nada! Si tienes más preguntas, no dudes en preguntar."]),
    (r"adios|hasta luego|nos vemos|hasta pronto", ["¡Hasta luego! Que tengas un buen día."]),

    (r"Qué diferencia hay entre la Switch OLED y la normal?|comparación entre modelos|¿cuál es mejor, Switch OLED o V2?", ["La Switch OLED tiene una pantalla más grande y colores más vivos. También tiene 64 GB de almacenamiento interno. ¿Te interesa conocer más detalles?"]),

    (r"¿Qué tan buena es la batería?|duración de batería de la Switch", ["La duración de batería depende del modelo: entre 2.5 y 9 horas. ¿Quieres saber de algún modelo específico?"]),

 (r"mi consola no prende|mi consola no enciende|la consola no funciona|la switch no prende", ["Si tu consola no enciende, intenta mantener presionado el botón de encendido durante 15 segundos. Si persiste el problema, conecta el adaptador de corriente directamente al puerto de carga y verifica si responde. ¿Necesitas más ayuda?"]),
 (r"que accesorios tienen?|tienen accesorios?|que accesorios hay?", ["Contamos con una variedad de accesorios como controles Pro, estuches de transporte, protectores de pantalla, y estaciones de carga para Joy-Con. ¿Te interesa alguno en particular?"]),
 (r"que procesador usa la switch?|que especificaciones tiene la consola?|cual es el hardware de la switch?", ["La Nintendo Switch utiliza un procesador Nvidia Tegra X1. ¿Quieres más detalles sobre el hardware o el rendimiento?"]),
 (r"hay ediciones limitadas?|tienen consolas especiales?|ediciones especiales", ["Sí, tenemos ediciones especiales como la de *Animal Crossing: New Horizons* y *Super Mario 35 Aniversario*. ¿Te gustaría más información?"]),
 (r"que diferencia hay entre la switch lite y la oled?|switch lite vs oled|cual es mejor, switch lite o oled?", ["La Switch OLED tiene una pantalla más grande y vibrante, con mejor calidad de colores, mientras que la Lite es más compacta y exclusivamente portátil. ¿Te interesa saber algo más?"]),
 (r"que juegos recomiendas para niños?|juegos para niños|juegos infantiles", ["Recomendamos juegos como *Mario Kart 8 Deluxe*, *Super Mario Party*, y *Pokémon Let's Go Pikachu/Eevee*. ¿Quieres conocer más opciones?"]),
 (r"como puedo revisar mis compras?|donde veo mis compras?|como revisar el historial", ["Puedes acceder a tu historial de compras iniciando sesión en tu cuenta en nuestro sitio web. ¿Necesitas ayuda con esto?"]),
 
  (r"Existen versiones especiales de la consola Nintendo Switch?|hay consolas de edicion especial?|consolas especiales?|ediciones especiales?|edicion especial", ["Sí, hay versiones especiales de la Nintendo Switch como la edición temática de The Legend of Zelda: Tears of the Kingdom y la edición de Animal Crossing: New Horizons. Estas suelen incluir diseños únicos en la consola y los Joy-Con."]),
  (r"Cómo se entregan las consolas de edición especial?", ["Entregamos las consolas en paquete completo o individual, en excelente calidad, hasta la puerta de tu casa :3"]),
  (r"Hay accesorios de buena calidad?", ["Claro que si tenemos accerios de buena calida puedes darte una vuelta en nuestra tienda y verlos"]),
  (r"Como se entregan las consolas?|como entregan las consolas?", ["Entregamos el producto que has ordenado dependiendo como pediste la consola es decir cómo paquete completo O individual"]),
  (r"Tienen redes sociales?", ["Claro que si por el momento contamos con whatsapp"]),
  (r"Cual es el numero de teléfono para comunicarme?|Cual es el numero de whatsapp?|cual es el numero?|dame el numero|podrias darme el numero ", ["Nuestro numero de whatsapp es 74725100"]),
  (r"Tienen ofertas en consolas actualmente?", ["si por el momento tenemos en oferta la Nintendo Switch Oled en 300"]),
  (r"Los productos que compre tienen garantia?|tienen garantia las consolas?|hay garantia?", ["Claro que si todos nuestros productos tienen una garantia de 3 meses"]),
 

]