from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pedir', methods=['POST'])
def procesar_pedido():
    cant_pollo = int(request.form.get('cantidad_pollo', 0))
    cant_mostrito = int(request.form.get('cantidad_mostrito', 0))
    cant_hamburguesa = int(request.form.get('cantidad_hamburguesa', 0))
    
    precio_pollo = 72.00
    precio_mostrito = 26.00
    precio_hamburguesa = 24.00
    
    sub_pollo = cant_pollo * precio_pollo
    sub_mostrito = cant_mostrito * precio_mostrito
    sub_hamburguesa = cant_hamburguesa * precio_hamburguesa
    total_general = sub_pollo + sub_mostrito + sub_hamburguesa
    
    if total_general == 0:
        return "<h3>No has seleccionado ningún producto. <a href='/'>Volver al menú</a></h3>"
    
    resumen = f"""
    <html>
    <body style="font-family: 'Segoe UI', sans-serif; padding: 50px; background: #f4f4f4; color: #222;">
        <div style="background: white; padding: 30px; border-radius: 15px; max-width: 500px; margin: 0 auto; box-shadow: 0 5px 15px rgba(0,0,0,.1);">
            <h2 style="color: #d62828; text-align: center;">🍗 ¡Pedido Recibido, Don Gallo!</h2>
            <hr style="border: 1px solid #eee;">
            <h3>Detalle de tu orden:</h3>
            <ul>
                {f"<li>{cant_pollo}x Pollo Entero - S/ {sub_pollo:.2f}</li>" if cant_pollo > 0 else ""}
                {f"<li>{cant_mostrito}x Mostrito - S/ {sub_mostrito:.2f}</li>" if cant_mostrito > 0 else ""}
                {f"<li>{cant_hamburguesa}x Hamburguesa Brasa - S/ {sub_hamburguesa:.2f}</li>" if cant_hamburguesa > 0 else ""}
            </ul>
            <hr style="border: 1px solid #eee;">
            <h3 style="color: #fb8500;">Total a Pagar: S/ {total_general:.2f}</h3>
            <p style="font-size: 14px; color: #666; text-align: center; margin-top: 20px;">Tu pedido está siendo preparado en la cocina.</p>
            <div style="text-align: center; margin-top: 20px;">
                <a href="/" style="background:#ffb703; color:#111; padding:10px 20px; text-decoration:none; border-radius:30px; font-weight:bold;">Hacer otro pedido</a>
            </div>
        </div>
    </body>
    </html>
    """
    return resumen
if __name__ == '__main__':
    app.run(debug=True, port=8080)