# 1. Supermercados y Clientes

**Funcionalidad:** Este grupo se encarga de gestionar las operaciones de un supermercado y sus clientes. Permite agregar supermercados, productos, y clientes, así como realizar acciones relacionadas con las compras, como recoger productos, pagar cuentas, y gestionar el inventario del supermercado. Los comandos permiten también el manejo de la caja y la interacción entre clientes y el personal del supermercado.

## Comandos a utilizar

- **supermarket add <supermarket_name>**: Agregar un nuevo supermercado al sistema.
- **supermarket add_product <supermarket_name> <product_name>**: Agregar un producto al inventario del supermercado.
- **client add <client_name>**: Agregar un cliente al sistema.
- **client move <client_name> <to_supermarket>**: Mover a un cliente a un supermercado específico.
- **client pick_up <client_name> <product_name>**: Permitir que un cliente recoja un producto.
- **supermarket show_clients <supermarket_name>**: Mostrar la lista de clientes en el supermercado.
- **supermarket show_products <supermarket_name>**: Mostrar la lista de productos en el supermercado.
- **supermarket restock <supermarket_name> <product_name> < amount>**: Reabastecer un producto en el supermercado.
- **client pay <client_name>**: Pagar todos los productos que tenga en el carrito cuando haya salido del checkout.
- **client show_cart <client_name>**: Mostrar los productos en la cesta del cliente.
- **client out_of _line<client_name>**: Permite que un cliente salga de la fila porque se le olvido comprar algo, sale de la cola si esta a punto de ser atendido. 
- **supermarket show_clients_in_cash <supermarket_name>**: Mostrar la lista de clientes en la caja.
- **supermarket serve_next_customer <supermarket_name>**: Atender al siguiente cliente en la fila de caja.
- **client leave <client_name>**: Permitir que un cliente salga del supermercado, siempre que haya pagado.
- **client leave_without_checkout <client_name>**: Permitir que un cliente salga sin comprar, si su cesta está vacía.
- **client check_cart <client_name> <product_name>**: Verificar si un producto está en la cesta del cliente.
- **supermarket set_open_close <supermarket_name> <open/close>**: Abrir / Cerrar el supermercado si no hay clientes dentro.
- **supermarket show_inventory <supermarket_name>**: Mostrar todo el inventario del supermercado.
- **client remove_from_cart <client_name> <product_name>**: Permitir que el cliente retire un producto de su cesta.
- **client get_in_line <client_name>**: Permitir que un cliente se ponga en la fila para pagar.

- **load_agents <file_path>**:  Load agents from a `JSON` file.
- **save_agents <file_path>**: Save agents to a `JSON` file.

