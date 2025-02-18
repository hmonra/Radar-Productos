#  Radar de Productos PcComponentes 

¡Caza las mejores ofertas de PcComponentes antes que nadie! Este proyecto de Python te permite monitorizar los nuevos productos y descuentos de PcComponentes y recibir alertas en tiempo real a través de Telegram.

##  Descripción General

¿Cansado de perderte las mejores ofertas de PcComponentes? Este script, creado en 2022, te ayuda a encontrar los productos más deseados a precios increíbles.  Automatiza la búsqueda y te notifica directamente en Telegram, ¡justo a tiempo para aprovechar las gangas!

### ✨ Funcionalidades Principales

1.  ** Extracción y clasificación inteligente:** El script rastrea la web de PcComponentes y clasifica los nuevos productos en categorías específicas, ¡cada una con su propio canal de Telegram!

    *   ️ Periféricos
    *    Discos duros
    *    Disipadores
    *    Fuentes de alimentación
    *   ️ Impresoras
    *    Portátiles
    *    TVs
    *    Cajas y torres
    *    Procesadores
    *    Consolas
    *    Smartphones
    *   ️ Monitores
    *    Tarjetas gráficas
    *    Placas base
    *    Electrodomésticos
    *    Sillas gaming
    *    Fotografía

2.  ** Alertas personalizables en Telegram:** Recibe notificaciones en canales de Telegram exclusivos según el porcentaje de descuento:

    *    **¡Ofertas Calientes!** Descuentos superiores al 25%
    *    **¡Descuentos Impactantes!** Descuentos superiores al 70%
    *    **¡Alerta Error de Precio!** Descuentos superiores al 89% (¡Aprovecha estas oportunidades únicas!)

## ⚙️ Cómo Funciona

El script utiliza **Selenium** y **undetected-chromedriver** para navegar sigilosamente por PcComponentes sin ser detectado.  Extrae la información de los productos, los clasifica y envía alertas a través de la API de Telegram a los canales correspondientes.

## ️ Instalación y Uso

1.  **Clona el repositorio:** `git clone https://github.com/hmonra/Radar-Productos.git`
2.  **Instala las dependencias:** `pip install -r requirements.txt`
3.  **Configura las variables de entorno:** Crea un archivo `.env` y añade tus credenciales (token del bot de Telegram, IDs de los canales, etc.).
4.  **Ejecuta el script:** `python main.py`

## ⚠️ Advertencias

*   El scraping responsable es clave. Respeta los términos de servicio de PcComponentes.
*   El uso de bots de compra automática puede estar prohibido.

##  Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

##  Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues o enviar pull requests.

## ✉️ Contacto

¿Tienes alguna pregunta o sugerencia? ¡No dudes en contactarme!