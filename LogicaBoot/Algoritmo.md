
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>

## Conexion con el Exchange ()
* Consultar API Bitso y Binance
* Validar credenciales y acceso 

## Establecer el mercado a operar manual ()
* input para selecionar entre los siguientes mercados
    * EURODOLLAR
    * BTCUSDT
    * ETHUSDT
    * ADAUSDT
* Input para seleccionar el tipo de operaciones
    * SPOT
    * MARGIN ISOLATED
    * MARGIN CRUZADO
    * FUTUROS

## Consultar del precio de Mercado ()
* Presentear en pantalla precio de mercado.

## Establecer la temporalidad ()
* Frame 5, 15, 30 = Scalping.
* Frame 30, 1hr, 2hrs = Intradia.
* Frame 4hr, D, W = Swing.

## Analizar tendencia por tipo de temporalidad ()
* Tomar informacion de las velas de acuero a la temporalidad:
    * Sacalping: ultimas No. barras
    * Intradia: Utimas No. barras.
    * Swing: Utimas No. barras.

## Funcion Estrategias de entrada()
* Cruces de Medias moviles.
* Precio y Volumen.
* Retroceso Fibonacci.
* RSI divergencias.

## Establecer puntos de compra y venta ()
* Orden Limitada.
* Orden de mercado.
* Orden OCO.

## Funcion Gestion de Riesgo del Portafolio ()
* Establecer monto maximo de exposicion.
* Establecer % de riesgo maximo del total de transacciones abiertas.
* Establecer % de stopo loss + adicional y % que de el precio Objetivo.
* El Riesgo no puede ser menor a 1:1.5 el ideal es 1:3.
* La perdidas no pueden superar el 5% del valor total de portafolio.
* Debe auto ajustar (Aumentar/disminuir)el valor maximo exposicion de la entrada a mercado.

## Funcion TrailStop ()
* Establecer parametros para cambiar de modo TrailStop.

## Funcion DCA ()
* Establecer directris para mercado spot para hacer compras escalonadas en swing.
* Establecer condiciones para hacer compras y generar data que Guarde y Muestre el promedio.
* Establecer condiciones para re-plantear nuevo punto de venta para toma de ganacias.
* Establecer condiciones para reiniciar el ciclo.

## Funcion Portafolio Equilibrado()
* Establecer reglas sobre el portafolio y que porcentajes debe de tener cada uno:
    - BTC 40%
        Expuesto %
        ColdWallet %
    - ETH 15%
        Expuesto %  
        ColdWallet %
    - ADA 15%
        Expuesto %
        ColdWallet %
    - USD 20%
        Siempre disponible
    - VARIOS 8%
        Expuesto %
        ColdWallet %
    - Nuevas tecnologias 2%
        Segun aplique

* Crear logica para que compare todo el portafolio y tome cierto porcentaje para que siempre mantenga el% designado en USDT,MXN u otra Stable coin.
* Generar alertas con el analisis por correo y/o webhooks para toma de deciciones manuales
* Whislist Automatizar la toma de desicion 

# Backtesting
* Establecer reglas para dar una estrategia como viable por medio de Backtesting en Pinescript
* desarrollar funcion para guardar un libro de trading
* Generar analiticos que se puedan exportar a Excel 
* Whislist generar api que pueda mandar datos a una DB nube y prensente graficamente en PowerBi, Tableo etc.


## Funcion Acciones con Dividendos ()
* Solicitar datos de portafolio de Quantfury a Api de Tradingview
* Presentar datos de fecha de pago de Dicidendos
* Estadistico de Revenues
* Presentar calificaicon por medio de escreener (webscraping) en caso de que no lo entregue api de tradingview + PineScript
* Calculo de pago de dividendos del portafolio o por Accion
    - Semanal
    - Quincenal
    - Mensual
    - Semestral
    - Anual 
* Calculo por accion para que de la cantidadObejtivo Mensual
* Data que presente cuales acciones se han mantenido en tendencia Alcista en anual y semestral (Diferentes periodos)
* Promedio de estado de resultdos ultomos 3 años, Anual, Semestral
* Promedio de Dividendos ultimos 3 años , 2 años , Anual, Semestral
* Alertamiento de caidas de precio de accion de 10, 15, 35, 40, 45, 50, 55, 60, 66, 75
    Crear reglas tomando en cuentas promedio de Dividendos, Promedio de estado de resultados, tendencia alcista o bajista
* Dependiendo de la convinacion de estos indicadores generar alertas para toma de deciciones
    - Desarrolar reglas para Decicion para DCA
    - Desarrollar reglas para Decicion de Venta



