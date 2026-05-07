import streamlit as st
Usuario = "admin"
Contraseña = "Admin2026"
Intentos = 3

if "login" not in st.session_state:
    st.session_state.login = False

if "intentos" not in st.session_state:
    st.session_state.intentos = 0

st.set_page_config(page_title="Sistema", layout="centered")
st.title("Sistema de Gestion")

if not st.session_state.login:

    st.subheader("Inicio de Sesion")

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")

    if st.button("Ingresar", use_container_width=True):

        if st.session_state.intentos >= Intentos:
            st.error("Acceso bloqueado.")
        
        elif not usuario.isalnum():
            st.error("Usuario invalido.")
            st.session_state.intentos += 1

        elif len(clave) < 8 or not any(c.isalpha() for c in clave) or not any(c.isdigit() for c in clave):
            st.error("Contraseña invalida.")
            st.session_state.intentos += 1

        elif usuario == Usuario and clave == Contraseña:
            st.session_state.login = True
            st.session_state.intentos = 0
            st.rerun()

        else:
            st.session_state.intentos += 1
            st.error(f"Credenciales incorrectas ({st.session_state.intentos}/{Intentos})")
else:

    opcion = st.selectbox(
        "Seleccione una opcion",
        ["Clasificar Numero", "Categoria Edad", "Calcular Tarifa"]
    )

    if opcion == "Clasificar Numero":

        numero = st.number_input("Numero", value=0)

        if st.button("Clasificar"):

            if numero > 0:
                st.success("Numero positivo")

            elif numero < 0:
                st.error("Numero negativo")

            else:
                st.info("Numero cero")

    elif opcion == "Categoria Edad":

        edad = st.number_input("Edad", 0, 120, 18)

        if st.button("Ver Categoria"):

            if edad < 13:
                st.info("Niño")

            elif edad < 18:
                st.warning("Adolescente")

            elif edad < 65:
                st.success("Adulto")

            else:
                st.info("Adulto mayor")
    else:

        precio = st.number_input("Precio", min_value=0.0, value=100.0)
        edad = st.number_input("Edad Cliente", 0, 120, 30)

        if st.button("Calcular"):

            descuento = 0.15 if edad < 18 else 0.20 if edad >= 65 else 0
            total = precio * (1 - descuento)

            st.success(f"Total: ${total:.2f}")
    st.divider()

    if st.button("Cerrar Sesion", use_container_width=True):

        st.session_state.login = False
        st.rerun()