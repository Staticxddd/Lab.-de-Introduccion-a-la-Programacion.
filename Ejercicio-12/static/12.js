async function cargarProductos() {
    const respuesta = await fetch("/api/productos");
    const productos = await respuesta.json();

    const contenedor = document.getElementById("lista-productos");

    productos.forEach(producto => {
        contenedor.innerHTML += `
            <article class="tarjeta">
                <img src="${producto.imagen}" alt="${producto.nombre}">
                
                <div class="info">
                    <h3>${producto.nombre}</h3>
                    <p>Código: ${producto.codigo}</p>
                    <p class="precio">$${producto.precio}</p>
                </div>
            </article>
        `;
    });
}

cargarProductos();