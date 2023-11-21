from django.shortcuts import render, redirect
from django.contrib import messages

from app.models import Usuario, Plan_Telefonia, Plan_Internet, Plan_Television


def index(request):
    return render(request, 'index.html')

def editar_plan_internet(request):
    return render(request, 'editar_perfil.html')

def editar_plan_television(request):
    return render(request, 'editar_perfil.html')

def editar_plan_telefonia(request):
    return render(request, 'editar_perfil.html')

def cerrarSesion(request):
    return render(request, 'cerrarSesion.html')

def editar_perfil(request):
    return render(request, 'editar_perfil.html')

def planes_telefonia(request):
    return render(request, "planes_telefonia.html")

def planes_television(request):
    return render(request, 'planes_television.html')
a
def planS(request):
    return render(request, "planS.html")

def planM(request):
    return render(request, "planM.html")

def planL(request):
    return render(request, "planL.html")

def planXL(request):
    return render(request, "planXL.html")

def cliente_dashboard(request):
    return render(request, "cliente_dashboard.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def empleado_dashboard(request):
    return render(request, "empleado_dashboard.html")

def enviar_comentario(request):
    return render(request, "enviar_comentario.html")

def registro(request):
    if request.method == "GET":
        return render(request, "registroUsuario.html")
    elif request.method == "POST":
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        numero = request.POST.get('numero')
        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')
        usuario = Usuario(rut=rut,
                          nombre=nombre,
                          apellido=apellido,
                          correo=correo,
                          numero=numero,
                          comuna=comuna,
                          direccion=direccion,
                          contrasena=contrasena,
                          rol_id=1)
        
        if usuario is not None:
            usuario.save()
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('/inicioSesion')
        else:
            messages.error(request, 'Error en el formulario. Verifica los datos ingresados.')
            return render(request, 'registroUsuario.html')
        

def login_view(request):
    if request.method == "GET":
        return render(request, "inicioSesion.html")
    elif request.method == "POST":
        getUsuario = request.POST.get('rut')
        getContrasena = request.POST.get('contrasena')
        usuario = Usuario.objects.filter(rut=getUsuario, 
                                         contrasena=getContrasena).first()

        if usuario and usuario.rol_id==1:
            # Para agregar un valor dentro de la SESSION, lo hacemos como si fuera un diccionario
            request.session["cliente"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render(request, "index.html", {'rut':getUsuario})
        
        elif usuario and usuario.rol_id==2:
            # Para agregar un valor dentro de la SESSION, lo hacemos como si fuera un diccionario
            request.session["empleado"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render('empleado_dashboard.html',{'rut':getUsuario})
        
        elif usuario and usuario.rol_id==3:
            request.session["administrador"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render(request, 'admin_dashboard.html',{'rut':getUsuario})
        
        else:
            error_message = "Por favor, ingrese un nombre de usuario."
            return render(request, "inicioSesion.html", {"error_message": error_message})




'''def editar_plan_telefonia(request, plan_id):
    #Obtén la instancia del plan de telefonía
    plan = PlanTelefonia.objects.get(id=plan_id)

    if request.method == 'POST':
        # Si se envió el formulario, procesa los datos
        form = EditarPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            #Redirige a la página de detalles del plan o a donde desees
            return redirect('detalle_plan', plan_id=plan.id)
    else:
       # Si es una solicitud GET, muestra el formulario con los datos actuales del plan
       form = EditarPlanForm(instance=plan)'''

#return render(request, 'editar_plan.html', {'form': form, 'plan': plan})

def resumen_plan_internet(request, plan_id):
    plan = Plan_Internet.objects.get(id=plan_id)
    return render(request, 'resumen_plan_internet.html', {'plan': plan})

def resumen_plan_television(request, plan_id):
    plan = Plan_Television.objects.get(id=plan_id)
    return render(request, 'resumen_plan_television.html', {'plan': plan})

def resumen_plan_telefonia(request, plan_id):
    plan = Plan_Telefonia.objects.get(id=plan_id)
    return render(request, 'resumen_plan_telefonia.html', {'plan': plan})

def confirmar_suscripcion(request):
    # Aquí iría la lógica para procesar la suscripción, pero necesito el login para que los datos del clinete y el plan se puedan insertar en base de datos.
    return render(request, 'confirmar_suscripcion.html')

def planes_internet(request):
    return render(request, 'planes_internet.html')


'''
def editar_plan_television(request, plan_id):
    # Obtén la instancia del plan de televisión
    plan = PlanTelevision.objects.get(id=plan_id)

    if request.method == 'POST':
        # Si se envió el formulario, procesa los datos
        form = EditarPlanTelevisionForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            # Redirige a la página de detalles del plan o a donde desees
            return redirect('detalle_plan_television', plan_id=plan.id)
    else:
        # Si es una solicitud GET, muestra el formulario con los datos actuales del plan
        form = EditarPlanTelevisionForm(instance=plan)

    return render(request, 'editar_plan_television.html', {'form': form, 'plan': plan})

def editar_plan_internet(request, plan_id):
    # Obtén la instancia del plan de Internet
    plan = PlanInternet.objects.get(id=plan_id)

    if request.method == 'POST':
        # Si se envió el formulario, procesa los datos
        form = EditarPlanInternetForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            # Redirige a la página de detalles del plan o a donde desees
            return redirect('detalle_plan_internet', plan_id=plan.id)
    else:
        # Si es una solicitud GET, muestra el formulario con los datos actuales del plan
        form = EditarPlanInternetForm(instance=plan)

    return render(request, 'editar_plan_internet.html', {'form': form, 'plan': plan})
'''