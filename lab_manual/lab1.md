# **Lab 1 - Introduction to Python/Django Framework**

## **Objective:**
> 1. To ensure the proper initialization of Python and Django
> 2. To learn about the basics of Django and Python
> 3. To learn how DBeaver creates the database
> 4. To add different modules in the eCommerce project created
> 5. Performing CRUD operation on the product added.

## **Introduction:**

1. ### **E-commerce**
    <pre>
        Ecommerce, also known as electronic commerce or internet commerce, refers to the
        buying and selling of goods or services using the internet, and the transfer of money and
        data to execute these transactions. Ecommerce is often used to refer to the sale of
        physical products online, but it can also describe any kind of commercial transaction
        that is facilitated through the internet.
    </pre>

2. ### **Python**
    <pre>
        Python is an interpreted, object-oriented, high-level programming language with
        dynamic semantics. It’s high-level built-in data structures, combined with dynamic
        typing and dynamic binding, make it very attractive for Rapid Application Development.
        Python's simple, easy to learn syntax emphasizes readability and therefore reduces the
        cost of program maintenance. Python supports modules and packages, which
        encourages program modularity and code reuse.
    </pre>

3. ### **Django**
    <pre>
        Django is a high-level Python Web framework that encourages rapid development and
        clean, pragmatic design. Built by experienced developers, it takes care of much of the
        hassle of Web development, so you can focus on writing your app without needing to
        reinvent the wheel. It's free and open source.
    </pre>

4. ### **Sqlite**
    <pre>
        SQLite3 is very easy to use database engine. It is self-contained, serverless,
        zero-configuration and transactional. It is very fast and lightweight, and the entire
        database is stored in a single disk file. It is used in a lot of applications as internal data
        storage. The Python Standard Library includes a module called "sqlite3" intended for
        working with this database.
    </pre>

5. ### **DBeaver**
    <pre>
        DBeaver is a universal database management tool for everyone who needs to work with
        data in a professional way.
        With DBeaver you are able to manipulate with your data like in a regular spreadsheet,
        create analytical reports based on records from different data storages, export
        information in an appropriate format. For advanced database users, DBeaver suggests a
        powerful SQL-editor, plenty of administration features, abilities of data and schema
        migration, monitoring database connection sessions, and a lot more.
    </pre>

6. ### **VSCode**
    <pre>
        Visual Studio Code is a lightweight but powerful source code editor which runs on your
        desktop and is available for Windows, macOS and Linux. It comes with built-in support
        for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other
        languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and
        Unity).
    </pre>

## **Procedure:**

1. Check python version:
    * python --version
2. Initialize django project:
    * django-admin startproject ecommerce_lab1
    * cd ecommerce_lab1
    * code .
3. Ensure required database and tables are initialized correctly
    * python manage.py migrate
    * python manage.py createsuperuser
4. Verify that you have configured correctly
    * python manage.py runserver
5. Let’s add a module product_manager
    * Let’s add a module product_module
6. Go to settings.py and add the module to INSTALLED_APPS list
    * INSTALLED_APPS = [ ...,'product_module' ]
7. In the module, open “models.py” and add code for Product model
    ```python

    from django.db import models
    from django.contrib.auth.models import User

    class Brand(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()

    ```
8. Ensure database table for added model is created properly
    * python manage.py makemigrations
    * python manage.py migrate
7. In database tool, verify that the added table is created properly
8. Goto “admin.py” and add the following code
    ```python

    from .models import Brand
    admin.site.register(Brand)

    ```
9. Run the server and verify CRUD operation
    * python manage.py runserver    
10. Perform: create, read, update, delete operation from admin panel

## **Observations:**

> 1. From this lab exercises, we learnt the basics of Django and Python, it’s
installation process and how to manipulate various datas within it. Also we learnt
how DBeaver helps for database.
> 2. We learnt to create different modules within the project and also learnt to
perform CRUD operations.
> 3. DBeaver needs to have sqlite3 as the reference point to the database for the
Djnago project.
> 4. Knowledge of indentation is a must in Python and Django.
> 5. Models must be added to the settings.py compulsorily to perform any further
operations in Django.

## **Conclusion:**
<pre>
    In conclusion, the Django framework is very easy to use and learn in an environment
    where it self initializes many important files so that our work can be more convenient
    and faster. Also dbeaver is also a much preferable database tool for use in creating our
    projects as it is very convenient.
</pre>