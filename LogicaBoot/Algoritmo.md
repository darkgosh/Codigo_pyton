
## Conexion con el Exchange ()
* Consultar API Bitso y Binance
* Validar credenciales y acceso 

## Establecer el mercado a operar manual ()
* input para selecionar entre los siguientes mercados
    * EURODOLLAR
    * BTCUSDT
    * ETHUSDT
    * CARDANOUSDT
* Input para seleccionar el tipo de operaciones
    * SPOT
    * MARGIN ISOLATED
    * MARGIN CRUZADO
    * FUTUROS

## Consultar del precio de Mercado ()
* Presentear en pantalla precio de mercado

## Establecer la temporalidad ()
* Frame 5, 15, 30 = Scalping
* Frame 30, 1hr, 2hrs = Intradia
* Frame 4hr, D, W = Swing

## Analizar tendencia por tipo de temporalidad ()
* Tomar informacion de las velas de acuero a la temporalidad:
    * Sacalping: ultimas No. barras
    * Intradia: Utimas No. barras
    * Swing: Utimas No. barras

## Funcion Estrategias de entrada()
* Cruces de Medias moviles
* Precio y Volumen
* Retroceso Fibonacci
* RSI divergencias

## Establecer puntos de compra y venta ()
* Orden Limitada
* Orden de mercado
* Orden OCO

## Funcion Gestion de Riesgo del Portafolio ()
* Establecer monto maximo de exposicion
* Establecer % de riesgo maximo del total de transacciones abiertas.
* Establecer % de stopo loss + adicional y % que de el precio Objetivo.
* El Riesgo no puede ser menor a 1:1.5 el ideal es 1:3
* La perdidas no pueden superar el 5% del valor total de portafolio.
* Debe auto ajustar (Aumentar/disminuir)el valor maximo exposicion de la entrada a mercado.

## Funcion TrailStop ()
* Establecer parametros para cambiar de modo TrailStop.

## Funcion DCA ()
* Establecer directris para mercado spot para hacer compras escalonadas en swing
* Establecer condiciones para hacer compras y generar datos guardados en tablas que lleven el promedio
* Establecer condiciones para replantear nuevo punto de venta para toma de ganacias
* Establecer condiciones para reiniciar el ciclo

## Funcion Portafolio Equilibrado()
* Establecer reglas sobre el portafolio y que porcentajes debe de tener cada uno 
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

##