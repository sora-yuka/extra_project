from rest_framework import status
from product.models import Product, Category
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from product.views import ProductAPIView, CategoryAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class ProductTest(APITestCase):
    """
    Test product view
    """
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.setup_category()
        self.setup_product()
        self.access_token = self.setup_bearer_token()
        self.url = "api/v1/product"
        
    def setup_user(self):
        user = User.objects.create_user(
            email="example@mail.com", 
            password="qwerty", 
            is_active=True
        )
        
        return user
    
    def setup_bearer_token(self):
        data = {
            "email": "example@mail.com",
            "password": "qwerty",
        }
        
        request = self.factory.post("api/v1/account/login", data=data)
        view = TokenObtainPairView.as_view()
        response = view(request)
        return response.data["access"]
    
    def setup_category(self):
        Category.objects.create(title="example_category_title")
        
    def setup_product(self):
        products = [
            Product(
                owner=self.user, 
                category=Category.objects.get(title="example_category_title"), 
                price=1200, 
                image="example_image", 
                title="example_title"
            ),
            Product(
                owner=self.user, 
                category=Category.objects.get(title="example_category_title"), 
                price=1200, 
                image="example_image_2", 
                title="example_title_2"
            )
        ]
        
        Product.objects.bulk_create(products)
        
    def test_get_product(self):
        request = self.factory.get(self.url)
        view = ProductAPIView.as_view({"get": "list"})
        response = view(request)
        
        assert response.status_code == status.HTTP_200_OK
        assert Product.objects.count() == 2
        
    def test_post_product(self):
        image = open("media/images/photo_2022-11-15_09-41-44_mkdczs6.jpg", "rb")
        data = {
            "owner": self.user.id,
            "category": Category.objects.first().title,
            "title": "example_product",
            "price": "1200",
            "image": image
        }
        
        request = self.factory.post("api/v1/product/", data=data, HTTP_AUTHORIZATION = "Bearer " + self.access_token)
        view = ProductAPIView.as_view({"post": "create"})
        response = view(request)
        image.close()
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.filter(title="example_product").exists()
        
    # def test_patch_product(self):
    #     data = {
    #         "title": "example_patching"
    #     }
        
    #     request = self.factory.patch("api/v1/product/", data, HTTP_AUTHORIZATION = "Bearer " + self.access_token)
    #     view = ProductAPIView.as_view({"patch": "update"})
    #     response = view(request)
        
        # assert request.status_code == status.HTTP_200_OK
        # print(response.data)
        
        
class CategoryTest(APITestCase):
    """
    Test category view
    """
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.setup_category()
        self.user = self.setup_user()
        self.url = "api/v1/product"
        
    def setup_user(self):
        user = User.objects.create_user(
            email="example@mail.com", 
            password="qwerty", 
            is_active=True
        )
        
        return user
        
    def setup_category(self):
        list_of_category = [
            Category("Education"), 
            Category("Sport"),
            Category("Entertainment"),
        ]
        
        # list_of_category = []
        
        # for i in range(1, 101):
        #     list_of_category.append(Category(f"category {i}"))
        
        Category.objects.bulk_create(list_of_category)
        
    def test_get_category(self):
        request = self.factory.get(self.url + "category/")
        view = CategoryAPIView.as_view({"get": "list"})
        response = view(request)
        
        assert response.status_code == status.HTTP_200_OK
        # assert Category.objects.count() == 100
        assert Category.objects.first().title == "Education"
        
    def test_post_category(self):
        data = {
            "title": "Gadged"
        }
        
        request = self.factory.post(self.url + "category/", data=data)
        force_authenticate(request, user=self.user)
        view = CategoryAPIView.as_view({"post": "create"})
        response = view(request)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.filter(title="Gadged").exists()
        # print(response.data)