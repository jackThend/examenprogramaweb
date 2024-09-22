from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1 - Cálculo de compras
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        # Calcular el descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - total_descuento

        return render_template('resultado1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_descuento=total_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

# Ejercicio 2 - Inicio de sesión
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Validar credenciales
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = "Bienvenido administrador juan"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('resultado2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
