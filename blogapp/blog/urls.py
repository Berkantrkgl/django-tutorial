from django.urls import path
from . import views



# http://127.0.0.1:8000/            => index.html
# http://127.0.0.1:8000/index       => index.html
# http://127.0.0.1:8000/blogs       => blogs
# http://127.0.0.1:8000/blogs/3     => blog-details

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    # Garip bir sekilde index'te sonuna ters slash eklemeden kabul ediyor ama
    # blogs kisminda hata veriyor.
    path("blogs/", views.blogs),
    path("blogs/<int:id>", views.blog_details),
]
