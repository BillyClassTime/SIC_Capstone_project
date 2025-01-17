# **8. Clientes y Parques de Atracciones**

### Funcionalidad: 

**Descripción:** Este grupo gestiona las interacciones entre los clientes (visitantes) y los parques de atracciones. Permite agregar parques de atracciones y sus atracciones, gestionar la compra de tickets, reservas, y realizar otras actividades dentro del parque, como montar en las atracciones, comprar comida, y solicitar reembolsos. Además, incluye funcionalidades para mostrar la información de las atracciones, los tiempos de espera, y gestionar el estado de apertura y cierre del parque.

## Comandos a utilizar

- **park add_park <park_name>**: Agregar un nuevo parque de atracciones al sistema
- **park add_ride <park_name> <ride_name>**: Agregar una nueva atracción (ride) en el parque
- **client add_client <client_name>**: Agregar un cliente al sistema
- **client buy_ticket <client_name> <park_name> <ride_name>**: Comprar un ticket para una atracción en el parque
- **park show_ride_info <park_name> <ride_name>**: Mostrar la información sobre una atracción específica
- **client enter_park <client_name> <park_name>**: Permitir que un cliente entre al parque
- **client exit_park <client_name> <park_name>**: Permitir que un cliente salga del parque
- **park show_rides <park_name>**: Mostrar la lista de todas las atracciones disponibles en un parque
- **client check_wait_time <client_name> <park_name> <ride_name>**: Consultar el tiempo de espera para una atracción
- **client ride_ride <client_name> <park_name> <ride_name>**: Permitir que un cliente monte una atracción
- **park set_open_close <park_name> <open/close>**: Abrir o cerrar el parque de atracciones
- **client make_reservation <client_name> <park_name>**: Reservar un lugar para una atracción específica
- **client cancel_reservation <client_name> <park_name>**: Cancelar una reserva en el parque
- **park show_clients <park_name>**: Mostrar la lista de clientes en el parque
- **client request_refund <client_name> <park_name> <ride_name>**: Solicitar un reembolso por un ticket de una atracción
- **client purchase_food <client_name> <park_name>**: Comprar comida dentro del parque
- **park show_food_menu <park_name>**: Mostrar el menú de comida disponible en el parque
- **client add_to_cart <client_name> <food_item>**: Añadir un alimento al carrito de compras dentro del parque
- **client check_cart <client_name>**: Verificar los artículos en el carrito de compras del cliente
- **client pay_for_food <client_name> <park_name>**: Pagar los artículos del carrito en el parque
- **park show_ticket_sales <park_name>**: Mostrar las ventas de tickets en el parque
- **park remove_ride <park_name> <ride_name>**: Eliminar una atracción del parque

