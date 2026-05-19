from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm, PedidoForm
from django.contrib.auth import authenticate, login
from .models import Cliente,Pedido
from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render

@login_required
def inicio(request):
    return render(request, "inicio.html", {
        "usuario": request.user
    })

def catalogo(request):

    query = request.GET.get("q", "").strip()
    genre = request.GET.get("genre", "")

    # 📚 Google Books API
    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    else:
        url = "https://www.googleapis.com/books/v1/volumes?q=f"

    libros = []

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        for item in data.get("items", [])[:12]:

            info = item.get("volumeInfo", {})

            titulo = info.get("title", "Sin título")
            autores = info.get("authors", ["Desconocido"])

            subjects = info.get("categories", [])  # 👈 importante

            # 🖼️ imagen
            imagen = ""
            if info.get("imageLinks"):
                imagen = info["imageLinks"].get("thumbnail", "")

            # 🔥 FILTRO GÉNERO
            if genre:
                if genre == "fiction" and not any("Fiction" in s for s in subjects):
                    continue
                if genre == "history" and not any("History" in s for s in subjects):
                    continue
                if genre == "classic" and not any("Classics" in s for s in subjects):
                    continue

            libros.append({
                "titulo": titulo,
                "autor": autores[0],
                "imagen": imagen
            })

    except Exception as e:
        print("ERROR API:", e)

    # 🔥 fallback seguro
    if len(libros) < 3:
        libros = [
            {"titulo": "Alicia en el País de las Maravillas", "autor": "Lewis Carroll", "imagen": ""},
            {"titulo": "Don Quijote de la Mancha", "autor": "Cervantes", "imagen": ""},
            {"titulo": "Ana Karenina", "autor": "Tolstói", "imagen": ""}
        ]

    print("LIBROS:", len(libros))

    return render(request, "catalogo_libros.html", {
        "libros": libros,
        "query": query
    })

def inicio_sesion(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect("inicio")

    else:
        form = LoginForm()

    return render(request, "inicio_sesion.html", {"form": form})

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )

            Cliente.objects.create(usuario=user)

            return redirect("inicio_sesion")

    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})

def crear_pedido(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        precio = request.POST.get("precio")
        autor = request.POST.get("autor")

        # Guardar en sesión (simple para empezar)
        pedido = {
            "titulo": titulo,
            "precio": precio,
            "autor": autor
        }

        request.session['pedido'] = pedido

        return redirect('detalle_pedido')

    return redirect('catalogo')

# Diferenciar entre Usuarios y Gestor
@login_required
def perfil(request):
    if not request.user.is_authenticated:
        return redirect("inicio_sesion")

    return render(request, "perfil.html")

# Creo las VISTAS para que se VEAN !!!!
def add_carrito(request):
    titulo = request.POST.get("titulo")
    autor = request.POST.get("autor")

    carrito = request.session.get("carrito", [])

    carrito.append({
        "titulo": titulo,
        "autor": autor
    })

    request.session["carrito"] = carrito

    return redirect("catalogo")


def detalle_pedido(request):
    return render(request, 'detalle_pedido.html')

def inicio_sin_sesion(request):
    return render(request, 'inicio_sin_sesion.html')

def gestor(request):
    return render(request, 'gestor.html')


"""
def crear_gestor(request):
    get.save()
    return HttpResponse("Gestor creado Exitosamnete{get.}")

def getgestores():

get editgestores():


y crear un gestor.html
"""
