# **Lab 2 - Product, Brand and Category**

## **Objective:**
> 1. To learn about the use of Foreign Key and its implementation 
> 2. To learn the process and the use of Relationship in ER diagram

## **Introduction:**

1. ### **Foreign Key**
    <pre>
        A foreign key is a column or group of columns in a relational database table that provides a 
        link between data in two tables. It acts as a cross-reference between tables because it references 
        the primary key of another table, thereby establishing a link between them.
    </pre>

2. ### **Relationship**
    <pre>
        A relationship, in the context of databases, is a situation that exists between two relational database 
        tables when one table has a foreign key that references the primary key of the other table. Relationships 
        allow relational databases to split and store data in different tables while linking disparate data items.
    </pre>

## **Procedure:**

1. In the product_module module, open “models.py” and edit code for Brand model
    ```python

    class Brand(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()

    ```
2. Similarly, edit code for Category
    ```python

    class Category(models.Model):
        name = models.CharField(max_length=200, default='')
        is_active = models.BooleanField()

        class Meta:
            verbose_name_plural = "Categories"

    ```
3. And at last edit code for Product model.
    ```python

    class Product(models.Model):
        name = models.CharField(max_length=200)
        price = models.FloatField()
        quantity = models.IntegerField()
        image_url = models.CharField(max_length=500)
        color_code = models.CharField(max_length=20)
        brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        registered_on = models.DateTimeField()
        is_active = models.BooleanField()

    ```
4. We will use sqllite3 which is default database in Django
    ```python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    ```
5. Ensure database table for added model is created properly
    * python manage.py makemigrations
    * python manage.py migrate
6. In database tool, verify that the added table is created properly
7. Goto “admin.py” and add the following code
    ```python

    from .models import Brand, Category, Product
    admin.site.register(Brand)
    admin.site.register(Category)
    admin.site.register(Product)
    
    ```
8. Run the server and verify CRUD operation
    * python manage.py runserver    
9. Perform: create, read, update, delete operation from admin panel

## **Discussion:**

> 1. Each model inherits “models.Model”.
> 2. Use of ForeignKey for one-to-many relationship.
> 3. Use of max_length in CharField.
> 4. Use of on_delete=models.CASCADE for ForeignKey.
> 5. Use of CharField, FloatField, IntegerField, DateTimeField, BooleanField, 
ForeignKey.

## **Conclusion:**
<pre>
    Thus, in this lab, we got to learn about the use of Foreign key, relationship 
    in the ER-diagram by the means of Django, created three tables and saw at the level 
    of implementation between them.
</pre>