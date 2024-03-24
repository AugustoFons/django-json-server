from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

carrito = []
favoritos = []

@csrf_exempt
def carrito_prod(request, producto_id=None):
    global carrito

    #POST
    if request.method == 'POST':
        data = json.loads(request.body)
        # procesar los datos y agregarlos al carrito
        carrito.append(data)
        return JsonResponse({"message": "Producto agregado al carrito correctamente"}, status=200)

    #GET
    elif request.method == 'GET':
        return JsonResponse(carrito, safe=False)

    #PUT(cantidades y precios)
    elif request.method == 'PUT':
        if producto_id is not None:
            # Recibe los datos del cuerpo de la solicitud
            data = json.loads(request.body)
            # Busca el producto en el carrito
            for producto in carrito:
                if producto["id"] == int(producto_id):
                    # Actualiza la cantidad y el precio del producto en el carrito
                    producto["cantidad"] = data.get("cantidad", producto["cantidad"])
                    producto["precioT"] = data.get("precioT", producto["precioT"])
                    return JsonResponse(producto, safe=False)
            return JsonResponse({"error": "Producto no encontrado en el carrito"}, status=404)
        else:
            return JsonResponse({"error": "ID del producto no proporcionado"}, status=400)
    
    # DELETE (eliminar todo el carrito)
    elif request.method == 'DELETE':
        if producto_id is not None:
            # Buscar el producto en el carrito por su ID
            for producto in carrito:
                if producto["id"] == int(producto_id):
                    # Eliminar el producto del carrito
                    carrito.remove(producto)
                    return JsonResponse({"message": f"Producto con ID {producto_id} eliminado del carrito"}, status=200)
            return JsonResponse({"error": "Producto no encontrado en el carrito"}, status=404)
        else:
            # Si no se proporciona un ID de producto, eliminar todo el carrito
            carrito = []
            return JsonResponse({"message": "Carrito vaciado correctamente"}, status=200)

    else:
        return JsonResponse({"error": "Método HTTP no permitido"}, status=405)



@csrf_exempt
def favoritos_prod(request, favoritos_id=None):
    global favoritos

    # POST
    if request.method == 'POST':
        data = json.loads(request.body)
    # Verificar si el cuerpo de la solicitud contiene solo un objeto JSON
        if isinstance(data, dict):
            # Verificar si el producto ya está en favoritos
            if data["id"] not in [producto["id"] for producto in favoritos]:
                # Si el producto no está en favoritos, agregarlo
                favoritos.append(data)
                return JsonResponse({"message": "Producto agregado a favoritos correctamente"}, status=200)
            else:
                return JsonResponse({"error": "El producto ya está en favoritos"}, status=400)
        else:
            return JsonResponse({"error": "El cuerpo de la solicitud debe contener solo un objeto JSON"}, status=400)

    # GET
    elif request.method == 'GET':
        # Convertir el conjunto favoritos a una lista antes de devolverlo como JSON
        return JsonResponse(favoritos, safe=False)

    # DELETE (eliminar todo o un producto específico)
    elif request.method == 'DELETE':
        if favoritos_id is not None:
            for producto in favoritos:
                if producto["id"] == int(favoritos_id):
                    favoritos.remove(producto)
                    return JsonResponse({"message": f"Producto con ID {favoritos_id} eliminado de favoritos"}, status=200)
            return JsonResponse({"error": "Producto no encontrado en favoritos"}, status=404)

    else:
        return JsonResponse({"error": "Método HTTP no permitido"}, status=405)