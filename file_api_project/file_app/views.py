from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import File
import os
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class FileListView(View):
    # Redirigir al login del admin
    @method_decorator(login_required(login_url='/admin/login/'))  
    def get(self, request):
        files = File.objects.all()
        user_group = request.user.groups.first().name if request.user.groups.exists() else 'User'
        return render(request, 'file_list.html', {'files': files, 'user_group': user_group})

class UploadFileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            file = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response({'error': 'Archivo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(file)
        return Response(serializer.data)

class DeleteFileView(View):
    def post(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)

        # Log :Imprimir la ruta del archivo
        print(f"Ruta del archivo: {file_path}")

        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("El archivo no existe en la ruta especificada.")

        file.delete()
        return redirect('file_list')
