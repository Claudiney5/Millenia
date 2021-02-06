'''
path('route<string>', viewfunction , [kwargs], [name= name])

- route - obrigatório , string com padrão de URL;
- viewfunction - obrigatório, funçaõ de vizualização;
- kwargs - argumentos arbitrários de keywords (dicionários) para visulização de destino;
- name - permite que se refira a URL em qualquer lugar do Django, sem ambiguidade.

'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('characters/', include('characters.urls')),
    path('admin/', admin.site.urls),
]
