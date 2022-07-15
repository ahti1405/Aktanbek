from django.urls import path
from .views import HomePageView, ProductsPageView, ProductDetailView, csv_view, PortfolioView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', ProductsPageView.as_view(), name='products'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('test/', FileDownloadView.as_view(), name='test'),
    path('csv/<int:pk>/', csv_view, name='csv'),
    path('portfolio-detail/<int:pk>/', PortfolioView.as_view(), name='portfolio'),
]