# Librerias
import time
import undetected_chromedriver.v2 as uc
import telebot
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Opciones de navegación
options = uc.ChromeOptions()
options.add_argument('--start')
options.add_argument('--disable-extensions')
options.add_argument("--disable-software-rasterizer")
options.add_argument('--ignore-ssl-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--disable-gpu')
options.add_argument("--disable-infobars")
options.add_argument("--force-device-scale-factor=1")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-notifications')
options.add_argument("--mute-audio")
options.add_argument("--disable-hang-monitor")
# options.add_argument('--blink-settings=imagesEnabled=false')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
driver = uc.Chrome(options=options)

# HORA INICIO SCRIPT
hora_inicial = datetime.now()

# Para enviar mensaje de aviso por telegram
#########################################
#########################################
# AVISOS CANAL REACONDICIONADOS ONLY
def telegram_bot_sendtext():
    enlace_summary = "https://www.pccomponentes.com/cart/summary"
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n'
    combo_producto += '    <b><a href="' + enlace_summary + '">🚀 Enlace directo a botón de compra</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# AVISOS CANAL CHOLLAZOS ONLY
def telegram_bot_sendtext9():
    enlace_summary = "https://www.pccomponentes.com/cart/summary"
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n'
    combo_producto += '    <b><a href="' + enlace_summary + '">🚀 Enlace directo a botón de compra</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# AVISOS CANAL OFERTAS TOP
def telegram_bot_ofertastop():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# AVISOS CANAL DEALS TOP
def telegram_bot_dealstop():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# AVISOS CANAL CHOLLOS TOP
def telegram_bot_chollostop():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
#########################################
#########################################
#########################################
# AVISOS CANALES POR CATEGORIAS
def telegram_bot_perifericos():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_discosduros():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_disipadores():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_psus():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_impresoras():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_portatiles():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_tvs():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_cajastorres():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_procesadores():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_consolas():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_smartphones():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_monitores():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_tarjetasgraficas():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_placasbase():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_electrodomesticos():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_sillasgaming():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_fotografia():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
def telegram_bot_errorprecio():
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
##############################
##############################
# BOT TELEGRAM DESCUENTOS
def telegram_bot_sendtext3():
    # enlace_compra_inicial = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    # enlace_compra = "https://cuty.io/quick?token=c785096224eb96f06ba1365c2&url=" + enlace_compra_inicial
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TEST DESCUENTOS
def telegram_bot_sendtext2():
    enlace_summary = "https://www.pccomponentes.com/cart/summary"
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>🔻 #' + cuadro_categoria + " " + cuadro_descuento + ' Dto! 🔻</b>' + '\n'
    combo_producto += '<b><a href="' + enlace_producto + '">' + nombre_producto + '</a></b>' + '\n' + '\n'
    combo_producto += '    <b>🔥 OFERTA: ' + precio_producto + '€ </b>' + ' (pvpr: ' + precio_original + '€)' + '\n'
    combo_producto += '    <b><a href="' + enlace_compra + '">🛒 Enlace directo a la cesta</a></b>' + '\n'
    combo_producto += '    <b><a href="' + enlace_summary + '">🚀 Enlace directo a botón de compra</a></b>' + '\n' + '\n'
    combo_producto += '<b>' + estado_producto + '</b>' + '\n'
    combo_producto += 'Estado: ' + detalle_rastrillo + '\n'
    combo_producto += 'Garantía: ' + garantia + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR TIME OUT
def telegram_bot_sendtext4():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>❌ Error en url, time out ❌</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR CAPTCHA
def telegram_bot_sendtext6():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>✅ Captcha detectado, pulsando botón ✅️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR AL PULSAR CAPTCHA
def telegram_bot_sendtext7():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>⛔️ Captcha detectado, fallo al pulsar botón ⛔️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR BAD GATEWAY
def telegram_bot_sendtext8():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>☑️ Bad gateway, refresco página ☑️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR BAD GATEWAY
def telegram_bot_sendtext10():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>⁉️ Enlace oferta no existente, se pasa al siguiente enlace ⁉️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR URL SIN DESCUENTO
def telegram_bot_sendtext11():
    bot_token = 'TOKEN DEL BOT' # AÑADIMOS TOKEN DE NUESTRO BOT DE AVISOS
    bot_chatid = 'ID DEL CHAT' # AÑADIMOS ID DEL CHAT DEL CANAL CORRESPONDIENTE
    combo_producto = '<b>☢️ Producto sin descuento, se pasa al siguiente enlace ☢️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# FUNCION PARA DETERMINAR SI EL PRODUCTO RASTRILLO ESTÁ DISPONIBLE O NO (BOTÓN COMPRAR)
def producto_disponible():
    if descuento_error_precio < descuento_final:
        telegram_bot_errorprecio()
    else:
        if descuento2 < descuento_final:
            telegram_bot_sendtext9()
        else:
            telegram_bot_chollostop()
            telegram_bot_dealstop()
            telegram_bot_ofertastop()
            telegram_bot_sendtext3()
    categoria = ['Altavoces', 'Teclados', 'Auriculares', 'TarjetasSonido', 'Ratones', 'Webcam', 'Joysticks', 'Volantes',
                 'TPV', 'DVDBluRay', 'Routers', 'AndroidSmartTV', 'TarjetasRed', 'Conectividad', 'PantallasProyección',
                 'BarrasSonido', 'TabletasDigitales', 'MicroCadenas', 'DJ', 'GafasRealidadVirtual', 'Bombillasinteligentes']
    if cuadro_categoria in categoria:
        telegram_bot_perifericos()
    categoria = ['DiscosDuros']
    if cuadro_categoria in categoria:
        telegram_bot_discosduros()
    categoria = ['VentiladoresCPU', 'RefrigeraciónLíquida', 'VentiladoresSuplementarios', 'VentiladoresCPU']
    if cuadro_categoria in categoria:
        telegram_bot_disipadores()
    categoria = ['FuentesAlimentación']
    if cuadro_categoria in categoria:
        telegram_bot_psus()
    categoria = ['Multifunciones', 'Impresoras']
    if cuadro_categoria in categoria:
        telegram_bot_impresoras()
    categoria = ['Portátiles', 'Tablets']
    if cuadro_categoria in categoria:
        telegram_bot_portatiles()
    categoria = ['Televisores', 'TVTDT', 'BluRayDVDCinema', 'SoportesTVoMonitor']
    if cuadro_categoria in categoria:
        telegram_bot_tvs()
    categoria = ['Torres', 'TorresCajasPC', 'ArmariosRack']
    if cuadro_categoria in categoria:
        telegram_bot_cajastorres()
    categoria = ['Procesadores']
    if cuadro_categoria in categoria:
        telegram_bot_procesadores()
    categoria = ['Gamepads', 'JuegosXboxSeriesXS', 'NintendoSwitch', 'AccesoriosPS5', 'MandosPS4', 'AccesoriosPS5',
                 'JuegosXboxOne', 'XboxSeriesXS', 'MandosPS5']
    if cuadro_categoria in categoria:
        telegram_bot_consolas()
    categoria = ['Móviles', 'SmartWatch', 'MóvilesBásicos', 'PulserasActividad']
    if cuadro_categoria in categoria:
        telegram_bot_smartphones()
    categoria = ['Monitores']
    if cuadro_categoria in categoria:
        telegram_bot_monitores()
    categoria = ['TarjetasGráficas']
    if cuadro_categoria in categoria:
        telegram_bot_tarjetasgraficas()
    categoria = ['PlacasBase']
    if cuadro_categoria in categoria:
        telegram_bot_placasbase()
    categoria = ['Frigoríficos', 'Básculas', 'Microondas', 'Tratamientodelaire', 'RobotsCocina', 'Termos',
                 'Ventiladores', 'Freidoras', 'Calefactores', 'Tostadoras', 'Lavavajillas', 'Cafeteras', 'RobotAspirador']
    if cuadro_categoria in categoria:
        telegram_bot_electrodomesticos()
    categoria = ['Sillas']
    if cuadro_categoria in categoria:
        telegram_bot_sillasgaming()
    categoria = ['AccesoriosCamaras', 'CámarasDigitales', 'ObjetivosparaCámaras']
    if cuadro_categoria in categoria:
        telegram_bot_fotografia()
# FUNCION PARA DETERMINAR SI EL PRODUCTO REACONDICIONADO ESTÁ DISPONIBLE O NO (BOTÓN COMPRAR)
def producto_disponible3():
    if descuento_error_precio < descuento_final:
        telegram_bot_errorprecio()
    else:
        if descuento2 < descuento_final:
            telegram_bot_sendtext9()
        else:
            telegram_bot_chollostop()
            telegram_bot_dealstop()
            telegram_bot_ofertastop()
            telegram_bot_sendtext()
            telegram_bot_sendtext3()
    categoria = ['Altavoces', 'Teclados', 'Auriculares', 'TarjetasSonido', 'Ratones', 'Webcam', 'Joysticks', 'Volantes',
                 'TPV', 'DVDBluRay', 'Routers', 'AndroidSmartTV', 'TarjetasRed', 'Conectividad', 'PantallasProyección',
                 'BarrasSonido', 'TabletasDigitales', 'MicroCadenas', 'DJ', 'GafasRealidadVirtual', 'Bombillasinteligentes']
    if cuadro_categoria in categoria:
        telegram_bot_perifericos()
    categoria = ['DiscosDuros']
    if cuadro_categoria in categoria:
        telegram_bot_discosduros()
    categoria = ['VentiladoresCPU', 'RefrigeraciónLíquida', 'VentiladoresSuplementarios', 'VentiladoresCPU']
    if cuadro_categoria in categoria:
        telegram_bot_disipadores()
    categoria = ['FuentesAlimentación']
    if cuadro_categoria in categoria:
        telegram_bot_psus()
    categoria = ['Multifunciones', 'Impresoras']
    if cuadro_categoria in categoria:
        telegram_bot_impresoras()
    categoria = ['Portátiles', 'Tablets']
    if cuadro_categoria in categoria:
        telegram_bot_portatiles()
    categoria = ['Televisores', 'TVTDT', 'BluRayDVDCinema', 'SoportesTVoMonitor']
    if cuadro_categoria in categoria:
        telegram_bot_tvs()
    categoria = ['Torres', 'TorresCajasPC', 'ArmariosRack']
    if cuadro_categoria in categoria:
        telegram_bot_cajastorres()
    categoria = ['Procesadores']
    if cuadro_categoria in categoria:
        telegram_bot_procesadores()
    categoria = ['Gamepads', 'JuegosXboxSeriesXS', 'NintendoSwitch', 'AccesoriosPS5', 'MandosPS4', 'AccesoriosPS5',
                 'JuegosXboxOne', 'XboxSeriesXS', 'MandosPS5']
    if cuadro_categoria in categoria:
        telegram_bot_consolas()
    categoria = ['Móviles', 'SmartWatch', 'MóvilesBásicos', 'PulserasActividad']
    if cuadro_categoria in categoria:
        telegram_bot_smartphones()
    categoria = ['Monitores']
    if cuadro_categoria in categoria:
        telegram_bot_monitores()
    categoria = ['TarjetasGráficas']
    if cuadro_categoria in categoria:
        telegram_bot_tarjetasgraficas()
    categoria = ['PlacasBase']
    if cuadro_categoria in categoria:
        telegram_bot_placasbase()
    categoria = ['Frigoríficos', 'Básculas', 'Microondas', 'Tratamientodelaire', 'RobotsCocina', 'Termos',
                 'Ventiladores', 'Freidoras', 'Calefactores', 'Tostadoras', 'Lavavajillas', 'Cafeteras', 'RobotAspirador']
    if cuadro_categoria in categoria:
        telegram_bot_electrodomesticos()
    categoria = ['Sillas']
    if cuadro_categoria in categoria:
        telegram_bot_sillasgaming()
    categoria = ['AccesoriosCamaras', 'CámarasDigitales', 'ObjetivosparaCámaras']
    if cuadro_categoria in categoria:
        telegram_bot_fotografia()


# DETALLE DE CLASIFICACIÓN POR % DE DESCUENTO
alcance = 5 # ALCANCE DE RASTREO
pos_actual = 1924720 # NUMERO DE PRODUCTO ACTUAL
pos_ini = 1924720 # NUMERO DE PRODUCTO INICIAL
descuento = 24
descuento2 = 69
descuento_error_precio = 89
detalle_rastrillo = "Como nuevo."
boton_detalle_rastrillo = 'article-datasheet-refurbished'

# BUCLE DE RASTREO
while True:
    print("-- Posición inicial ", pos_ini, "--")
    print("Script corriendo desde: ", hora_inicial)
    try:
        # Loop para navegar entre páginas rastrillo.
        enlacerastrillo = ("https://www.pccomponentes.com/rastrillo/" + pos_actual.__str__())
        driver.get(enlacerastrillo)
        print(enlacerastrillo)
    except TimeoutException:
        print("")
        print("Url Time out..")
        print("Volviendo a escanear...")
        print("")
        telegram_bot_sendtext4()
        driver.refresh()
        continue
    try:
        if driver.find_elements(By.CLASS_NAME, 'inline-block'):
            print("Bad gateway..")
            print("Volviendo a escanear...")
            telegram_bot_sendtext8()
            driver.refresh()
            continue
        if driver.find_elements(By.ID, 'challenge-running'):
            print("Detectado por captcha..")
            time.sleep(3)
            WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'hcaptcha-box'))).click()
            print("Pulso botón captcha..")
            telegram_bot_sendtext6()
            time.sleep(3)
        else:
            print("Bypass captcha OK..")
            if driver.find_elements(By.CLASS_NAME, 'btn.btn-block.btn-primary.btn-lg.m-t-1.accept-cookie'):
                print("Cookies pendientes de aceptar..")
                WebDriverWait(driver, 40) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-block.btn-primary.btn-lg.m-t-1.accept-cookie'))).click()
                print("Cookies aceptadas..")
                time.sleep(2)
            else:
                print("Cookies OK..")
            try:
                # Se verifica si el link está en uso.
                contenedor_principal = WebDriverWait(driver, 30) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'contenedor-principal')))
                contenedor_principal = contenedor_principal.text
            except TimeoutException:
                print("")
                print("Url Time out..")
                print("Volviendo a escanear...")
                print("")
                telegram_bot_sendtext4()
                driver.refresh()
                continue
            if "Código de error 404" in contenedor_principal:
                current_time = datetime.now().time()
                print("Enlace sin asignar, escaneando... ", current_time)
                pos_actual = pos_actual + 1
            else:
                # Se extrae el nombre.
                nombre_producto = WebDriverWait(driver, 40) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'h4')))
                nombre_producto = nombre_producto.text
                # Se extrae el precio original y con descuento.
                elements = driver.find_elements(By.ID, 'precio-main')
                for e in elements:
                    precio_producto = (e.get_attribute("data-price"))
                    # precio_original = (e.get_attribute("data-baseprice"))
                    precio_producto = float(precio_producto)
                    precio_producto = round(precio_producto, 2)
                    precio_producto = str(precio_producto)
                elements = driver.find_elements(By.CLASS_NAME, 'original-price-nodiscount')
                for e in elements:
                    precio_original = (e.get_attribute("data-price"))
                # Se extrae la categoria
                cuadro_categoria_inicial = WebDriverWait(driver, 40) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'navegacion-secundaria__migas-de-pan')))
                cuadro_categoria_inicial = cuadro_categoria_inicial.text
                print(cuadro_categoria_inicial)
                # OPCIONES PARA LIMPIAR NOMBRE
                b_string = cuadro_categoria_inicial
                b_string = b_string.replace("Home", "")
                b_string = b_string.replace("Componentes", "")
                b_string = b_string.replace("Audio", "")
                b_string = b_string.replace(",", "")
                b_string = b_string.replace("Vídeo", "")
                b_string = b_string.replace("y", "")
                b_string = b_string.replace("Redes", "")
                b_string = b_string.replace("Cables", "")
                b_string = b_string.replace("Periféricos", "")
                b_string = b_string.replace("Electrodomésticos", "")
                b_string = b_string.replace("Mundo", "")
                b_string = b_string.replace("/", "")
                b_string = b_string.replace("Ordenadores", "")
                b_string = b_string.replace("Comparador", "")
                b_string = b_string.replace("de", "")
                b_string = b_string.replace("Hogar", "")
                b_string = b_string.replace("Foto", "")
                b_string = b_string.replace("Portátiles  Portátiles", "Portátiles")
                b_string = b_string.replace("Ventilación", "")
                b_string = b_string.replace("     Televisores", "Televisores")
                b_string = b_string.replace("Smartphones", "")
                b_string = b_string.replace("Telefonía", "")
                b_string = b_string.replace("Cuidado", "")
                b_string = b_string.replace("Personal", "")
                b_string = b_string.replace("Salud", "")
                b_string = b_string.replace("Proección", "Proyección")
                b_string = b_string.replace("Gaming", "")
                b_string = b_string.replace("Vioconsolas", "Videoconsolas")
                b_string = b_string.replace("Reacondicionados", "")
                b_string = b_string.replace(" ", "")
                b_string = b_string.replace(">VertodoslosAccesorios", "Accesorios")
                b_string = b_string.replace("ConsolasviojuegosAccesoriosXboxOne", "XboxOne")
                b_string = b_string.replace("VideoconsolasXboxSeriesXS", "XboxSeriesXS")
                b_string = b_string.replace("TorresCajasCarcasasBarebones", "Barebones")
                b_string = b_string.replace("TorresCajasCarcasasTorres", "Torres")
                b_string = b_string.replace("Proectores", "Proyectores")
                b_string = b_string.replace("Micro-CanasHi-Fi", "Micro-Cadenas/Hi-Fi")
                b_string = b_string.replace("ConsolasviojuegosMandosPS4", "ConsolasvideojuegosMandosPS4")
                b_string = b_string.replace("PequeñoelectrodomésticoMicroondas", "Microondas")
                b_string = b_string.replace("PortátilesPortátiles", "Portátiles")
                b_string = b_string.replace("GamepadsJosticksGamepads", "Gamepads")
                b_string = b_string.replace("MandosPCGamepads", "Gamepads")
                b_string = b_string.replace("VentiladoresRefrigeraciónLíquida", "RefrigeraciónLíquida")
                b_string = b_string.replace("VentiladoresVentiladoresCPU", "VentiladoresCPU")
                b_string = b_string.replace("ConsolasviojuegosNintendoSwitchVideoconsolasNintendoSwitch", "NintendoSwitch")
                b_string = b_string.replace("WearablesSmartphoneMóviles", "Móviles")
                b_string = b_string.replace("ConsolasviojuegosAccesoriosPS5", "AccesoriosPS5")
                b_string = b_string.replace("ConsolasviojuegosPlastation4MandosPS4", "MandosPS4")
                b_string = b_string.replace("ConsolasviojuegosPlastation5AccesoriosPS5", "AccesoriosPS5")
                b_string = b_string.replace("ConsolasviojuegosXBoxOneJuegosXboxOne", "JuegosXboxOne")
                b_string = b_string.replace("ConsolasviojuegosXboxSeriesXSXboxSeriesXS", "XboxSeriesXS")
                b_string = b_string.replace("GamepadsJosticksJosticks", "Joysticks")
                b_string = b_string.replace("GamepadsJosticksVolantes", "Volantes")
                b_string = b_string.replace("ImpresorasConsumiblesImpresoras", "Impresoras")
                b_string = b_string.replace("personalsaludbienestarBásculas", "Básculas")
                b_string = b_string.replace("AltavocesTVBarrasSonido", "BarrasSonido")
                b_string = b_string.replace("WearablesRelojSmartWatch", "SmartWatch")
                b_string = b_string.replace("hogarGranElectrodomésticoFrigoríficos", "Frigoríficos")
                b_string = b_string.replace("hogarLimpiezalaRopaRobotAspirador", "RobotAspirador")
                b_string = b_string.replace("TabletsEbooksAccesoriosparaTabletsPenStlus", "TabletsPenStylus")
                b_string = b_string.replace("hogarGranElectrodomésticoLavadoras", "Lavadoras")
                b_string = b_string.replace("PortátilesAccesoriosPortatiles", "AccesoriosPortatiles")
                b_string = b_string.replace("hogarBicicletasEléctricas", "BicicletasEléctricas")
                b_string = b_string.replace("hogarGranElectrodomésticoHornos", "Hornos")
                b_string = b_string.replace("SmarthomeEficienciaenergéticaBombillasinteligentes", "Bombillasinteligentes")
                b_string = b_string.replace("hogarClimaAireAcondicionado", "AireAcondicionado")
                b_string = b_string.replace("SmarthomeEficienciaenergéticaTermostatosInteligentes", "TermostatosInteligentes")
                b_string = b_string.replace("TPVTPV", "TPV")
                b_string = b_string.replace("GrabadorasDVDBluRa", "DVDBluRay")
                b_string = b_string.replace("TabletsEbooksTablets", "Tablets")
                b_string = b_string.replace("WearablesMóvilesBásicos", "MóvilesBásicos")
                b_string = b_string.replace("hogarPequeñoElectrodomésticoMicroondas", "Microondas")
                b_string = b_string.replace("hogarClimaTratamientolaire", "Tratamientodelaire")
                b_string = b_string.replace("hogarPequeñoElectrodomésticoRobotscocina", "RobotsCocina")
                b_string = b_string.replace("hogarGranElectrodomésticoCalentadoresTermos", "Termos")
                b_string = b_string.replace("hogarClimaVentiladores", "Ventiladores")
                b_string = b_string.replace("hogarSillas", "Sillas")
                b_string = b_string.replace("ReceptoresTVTDT", "TVTDT")
                b_string = b_string.replace("OciotiempolibrePatinetes", "Patinetes")
                b_string = b_string.replace("hogarPequeñoElectrodomésticoFreidoras", "Freidoras")
                b_string = b_string.replace("hogarMicroCanasHi-Fi", "MicroCadenas")
                b_string = b_string.replace("ReproductoresBluRaDVDCinema", "BluRayDVDCinema")
                b_string = b_string.replace("VentiladoresVentiladoresSuplementarios", "VentiladoresSuplementarios")
                b_string = b_string.replace("hogarPulserasActividad", "PulserasActividad")
                b_string = b_string.replace("hogarElectrodomesticosTostadoras", "Tostadoras")
                b_string = b_string.replace("hogarCalefacciónCalefactores", "Calefactores")
                b_string = b_string.replace("hogarGranElectrodomésticoLavavajillas", "Lavavajillas")
                b_string = b_string.replace("personalsaludFitnessaparatosgimnasiaBicicletasEstáticas", "BicicletasEstáticas")
                b_string = b_string.replace("hogarCafeterascápsulasCafeteras", "Cafeteras")
                cuadro_categoria = b_string
                print(cuadro_categoria)
                if driver.find_elements(By. CLASS_NAME, 'badget-discount'):
                    # Se extrae el descuento.
                    cuadro_descuento = WebDriverWait(driver, 40) \
                        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'badget-discount--number')))
                    cuadro_descuento = cuadro_descuento.text
                    print("Descuento: " + cuadro_descuento)
                    c_string = cuadro_descuento
                    c_string = c_string.replace("-", "")
                    c_string = c_string.replace("%", "")
                    descuento_final = c_string
                    descuento_final = (int(descuento_final))
                else:
                    print("Url sin indicación de descuento..")
                    print("Paso al siguiente enlace...")
                    telegram_bot_sendtext11()
                    pos_ini = pos_actual + 1
                    pos_actual = pos_ini
                    continue
                try:
                    if descuento < descuento_final:
                        print("Descuento enorme encontrado!")
                        codigo_articulo = WebDriverWait(driver, 40) \
                            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'codigo-articulo-pc')))
                        codigo_articulo = codigo_articulo.text
                        print("Código artículo: " + codigo_articulo)
                        # MODIFICACION CODIGO WEB PARA MOSTRAR DETALLE RASTRILLO
                        modificacion = driver.find_element(By.ID, 'read-more-full-state')
                        driver.execute_script("arguments[0].style.display = 'inline';", modificacion)
                        # SE EXTRAE INFORMACION DEL ESTADO DEL PRODUCTO
                        detalle_rastrillo_pre = WebDriverWait(driver, 40) \
                            .until(EC.element_to_be_clickable((By.ID, 'read-more-full-state')))
                        detalle_rastrillo_pre = detalle_rastrillo_pre.text
                        r_string = detalle_rastrillo_pre
                        r_string = r_string.replace(
                            "Este producto ha sido testado, superando nuestros test de calidad. Producto reacondicionado por nuestros técnicos.",
                            "")
                        detalle_rastrillo = r_string
                        if "En perfecto estado" not in detalle_rastrillo:
                            estado_producto = "🔸 SEMINUEVO 🔸"
                            garantia = "1 año."
                            enlace_producto = enlacerastrillo
                            print(detalle_rastrillo)
                            producto_disponible()
                        else:
                            estado_producto = "🔹 REACONDICIONADO 🔹"
                            garantia = "3 años."
                            # OPCIONES PARA LIMPIAR NOMBRE
                            a_string = nombre_producto
                            a_string = a_string.replace("Á", "a")
                            a_string = a_string.replace("É", "e")
                            a_string = a_string.replace("Í", "i")
                            a_string = a_string.replace("Ó", "o")
                            a_string = a_string.replace("Ú", "u")
                            a_string = a_string.replace("á", "a")
                            a_string = a_string.replace("é", "e")
                            a_string = a_string.replace("í", "i")
                            a_string = a_string.replace("ó", "o")
                            a_string = a_string.replace("ú", "u")
                            a_string = a_string.replace("--", "-")
                            a_string = a_string.replace(" + ", "-")
                            a_string = a_string.replace(" ", "-")
                            a_string = a_string.replace("\"", "")
                            a_string = a_string.replace(".", "")
                            a_string = a_string.replace(" ", "")
                            a_string = a_string.replace("/", "-")
                            a_string = a_string.replace("(", "")
                            a_string = a_string.replace(")", "")
                            a_string = a_string.replace("%", "")
                            a_string = a_string.replace("º", "")
                            print(a_string)
                            enlace_reacondicionado = ("https://www.pccomponentes.com/" + a_string + "-reacondicionado")
                            a_string = enlace_reacondicionado
                            a_string = a_string.replace("--", "-")
                            a_string = a_string.replace("+", "")
                            a_string = a_string.replace(" ", "")
                            enlace_reacondicionado_final = a_string
                            print("Accediendo a enlace reacondicionado...")
                            print(enlace_reacondicionado_final.lower())
                            driver.get(enlace_reacondicionado_final.lower())
                            if driver.find_elements(By.ID, 'contenedor-principal'):
                                contenedor_principal = WebDriverWait(driver, 30) \
                                     .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'contenedor-principal')))
                                contenedor_principal = contenedor_principal.text
                            if driver.find_elements(By.ID, 'root'):
                                contenedor_principal = WebDriverWait(driver, 30) \
                                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'root')))
                                contenedor_principal = contenedor_principal.text
                            if "Código de error 404" in contenedor_principal:
                                print("Enlace reacondicionado erróneo...")
                                print("Accediendo a enlace de ofertas...")
                                # Genero enlace ofertas.
                                # OPCIONES PARA LIMPIAR NOMBRE
                                a_string = nombre_producto
                                a_string = a_string.replace("Á", "a")
                                a_string = a_string.replace("É", "e")
                                a_string = a_string.replace("Í", "i")
                                a_string = a_string.replace("Ó", "o")
                                a_string = a_string.replace("Ú", "u")
                                a_string = a_string.replace("á", "a")
                                a_string = a_string.replace("é", "e")
                                a_string = a_string.replace("í", "i")
                                a_string = a_string.replace("ó", "o")
                                a_string = a_string.replace("ú", "u")
                                a_string = a_string.replace("--", "-")
                                a_string = a_string.replace(" + ", "-")
                                a_string = a_string.replace(" ", "-")
                                a_string = a_string.replace("\"", "")
                                a_string = a_string.replace(".", "")
                                a_string = a_string.replace(" ", "")
                                a_string = a_string.replace("/", "-")
                                a_string = a_string.replace("(", "")
                                a_string = a_string.replace(")", "")
                                a_string = a_string.replace("%", "")
                                print(a_string)
                                enlace_reacondicionado = (
                                        "https://www.pccomponentes.com/ofertas/" + a_string + "?filters=pccomponentes-reaconditioned")
                                a_string = enlace_reacondicionado
                                a_string = a_string.replace("--", "-")
                                a_string = a_string.replace("+", "")
                                a_string = a_string.replace(" ", "")
                                enlace_reacondicionado_final = a_string
                                print(enlace_reacondicionado_final.lower())
                                driver.get(enlace_reacondicionado_final.lower())
                                # Se comprueba que el enlace es válido.
                                contenedor_principal = WebDriverWait(driver, 30) \
                                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'contenedor-principal')))
                                contenedor_principal = contenedor_principal.text
                                if "Código de error 404" in contenedor_principal:
                                    print("Enlace ofertas erróneo, se pasa a siguiente enlace...")
                                else:
                                    # Compruebo si hay unidades.
                                    unidades_producto = WebDriverWait(driver, 40) \
                                        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-seller-list__row--summary')))
                                    unidades_producto = unidades_producto.text
                                    print(unidades_producto)
                                    if "0" in unidades_producto:
                                        print("No hay stock, pasando a siguiente enlace...")
                                    else:
                                        # Compruebo estado del producto.
                                        detalle_rastrillo = WebDriverWait(driver, 40) \
                                            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-seller-list__row__condition-description-text')))
                                        detalle_rastrillo = detalle_rastrillo.text
                                        d_string = detalle_rastrillo
                                        d_string = d_string.replace("Estado: ", "")
                                        detalle_rastrillo = d_string
                                        print(detalle_rastrillo)
                                        if "En perfecto estado" in detalle_rastrillo:
                                            estado_producto = "🔹 REACONDICIONADO 🔹"
                                            garantia = "3 años."
                                        else:
                                            estado_producto = "🔸 SEMINUEVO 🔸"
                                            garantia = "1 año."
                                        if driver.find_elements(By.CLASS_NAME, 'c-seller-list__row__price-value'):
                                            print("Encontrado enlace de oferta, hago click..")
                                            WebDriverWait(driver, 40) \
                                                .until(EC.element_to_be_clickable((By.CLASS_NAME, 'c-seller-list__row__price-value'))).click()
                                        else:
                                            print("No hay URL para hacer click..")
                                            print("Paso al siguiente enlace...")
                                            telegram_bot_sendtext10()
                                            pos_ini = pos_actual + 1
                                            pos_actual = pos_ini
                                            continue
                                        # Se verifica si el link está en uso.
                                        contenedor_principal = WebDriverWait(driver, 30) \
                                            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'contenedor-principal')))
                                        contenedor_principal = contenedor_principal.text
                                        if "Código de error 404" in contenedor_principal:
                                            current_time = datetime.now().time()
                                            print("Enlace erróneo, paso al siguiente enlace... ", current_time)
                                        else:
                                            enlace_producto = driver.current_url
                                            # Se extrae el precio.
                                            elements = driver.find_elements(By.ID, 'precio-main')
                                            for e in elements:
                                                precio_producto = (e.get_attribute("data-price"))
                                                precio_producto = float(precio_producto)
                                                precio_producto = round(precio_producto, 2)
                                                precio_producto = str(precio_producto)
                                            codigo_articulo = WebDriverWait(driver, 30) \
                                                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'codigo-articulo-pc')))
                                            codigo_articulo = codigo_articulo.text
                                            print(codigo_articulo)
                                            producto_disponible3()
                            else:
                                if driver.find_elements(By.ID, 'sticky-bar-buy-box'):
                                    print("Detectado enlace reacondicionado nuevo diseño, accediendo a codigo producto..")
                                    codigo_articulo = WebDriverWait(driver, 40) \
                                        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div[2]/div[3]/span[2]')))
                                    codigo_articulo = codigo_articulo.text
                                    cod_string = codigo_articulo
                                    cod_string = cod_string.replace("Cod. ", "")
                                    cod_string = cod_string.replace("Artículo", "")
                                    cod_string = cod_string.replace(": ", "")
                                    codigo_articulo = cod_string
                                    enlace_producto = enlace_reacondicionado_final.lower()
                                    producto_disponible3()
                                else:
                                    # Se extrae el precio.
                                    elements = driver.find_elements(By.ID, 'precio-main')
                                    for e in elements:
                                        precio_producto = (e.get_attribute("data-price"))
                                        precio_producto = float(precio_producto)
                                        precio_producto = round(precio_producto, 2)
                                        precio_producto = str(precio_producto)
                                    enlace_producto = enlace_reacondicionado_final.lower()
                                    codigo_articulo = WebDriverWait(driver, 40) \
                                        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'codigo-articulo-pc')))
                                    codigo_articulo = codigo_articulo.text
                                    producto_disponible3()
                    else:
                        print("Descuento insuficiente...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("Volviendo a escanear...")
                    print("")
                    telegram_bot_sendtext4()
                    driver.refresh()
                    continue
                else:
                    print("Pasando al siguiente enlace...")
                    pos_ini = pos_actual + 1
                    pos_actual = pos_ini
                    detalle_rastrillo = "Como nuevo."
            if pos_actual > pos_ini + alcance:
                print("Pasado rango de alcance, reiniciando...")
                pos_actual = pos_ini
    except TimeoutException:
        print("")
        print("Url Time out..")
        print("Volviendo a escanear...")
        print("")
        telegram_bot_sendtext7()
        driver.refresh()
        continue
