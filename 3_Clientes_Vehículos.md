# 3. Clientes y Vehículos

**Funcionalidad:** Este grupo se ocupa de las operaciones relacionadas con vehículos y sus propietarios (clientes). Permite agregar vehículos, gestionar la compra y venta de vehículos, y permitir que los clientes interactúen con sus vehículos (entrar, salir, mover, y repostar). También incluye funcionalidades para manejar pasajeros y estados de los vehículos (por ejemplo, si están en movimiento o sin combustible).

## Comandos a utilizar

- **vehicle add <vehicle_name>**: Agregar un vehículo al sistema.
- **client add <client_name>**: Agregar un cliente al sistema.
- **client buy <client_name> <vehicle_name>**: Comprar un vehículo, manteniendo un registro de cuántos vehículos posee el cliente; no puede comprar un vehículo que ya ha sido adquirido por otro cliente ni uno que no ha sido añadido al sistema.
- **client get_in <client_name> <vehicle_name>**: Subir al vehículo; si el cliente no lo ha comprado, debe ser informado de que no posee ningún vehículo.
- **client sell <client_name> <vehicle_name>**: Vender un vehículo, haciéndolo disponible para que otro cliente lo adquiera.
- **client get_out <client_name> <vehicle_name>**: Bajar del vehículo; no puede salir si no se ha subido previamente.
- **client move <client_name> <vehicle_name> <destination>**: Mover el vehículo; si el vehículo no ha sido comprado y el cliente no está dentro, debe ser informado de que no puede hacerlo.
- **vehicle refuel <vehicle_name> <amount>**: Reabastecer el vehículo; si el cliente no posee ningún vehículo, no puede reabastecerlo.
- **client pick_up_passenger <client_name> <vehicle_name> <passenger_name>**: Recoger a un pasajero; el vehículo debe pertenecer al cliente, el otro cliente debe estar en el sistema, no puede estar en otro vehículo, y el vehículo debe tenercombustible.
- **client drop_off_passenger <client_name> <vehicle_name> <passenger_name>**: Dejar a un pasajero; el pasajero debe haber sido recogido previamente.
- **client stop <client_name> <vehicle_name>**: Detener el vehículo; el cliente debe haber movido el vehículo previamente.
- **vehicle stop_light_traffic <vehicle_name>**: Detener el tráfico en un semáforo; el vehículo debe haber sido vendido, el cliente debe estar dentro, debe tener combustible, y el motor debe estar encendido.
- **vehicle get_back_on_track <vehicle_name>**: Retomar el movimiento; el vehículo debe estar detenido para reanudarlo.
- **vehicle show_in_system**: Mostrar vehículos en el sistema.
- **vehicle show_moving**: Mostrar vehículos actualmente en movimiento.
- **vehicle show_without_fuel**: Mostrar vehículos que están sin combustible.
- **client show_in_system**: Mostrar clientes en el sistema.
- **client show_with_vehicle**: Mostrar clientes que poseen vehículos.
- **client show_inside_vehicle**: Mostrar clientes actualmente dentro de un vehículo.
- **vehicle random_breakdown <vehicle_name>**: Marcar aleatoriamente un vehículo vendido como descompuesto; el cliente no puede moverlo.