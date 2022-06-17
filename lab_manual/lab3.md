# **Lab 3 - Search Products (Admin)**

## **Objective:**
> 1. To perform search and filter operations in the admin panel. 
> 2. To understand the basic operation of FK in an ER diagram..

## **Introduction:**

1. ### **Foreign Key**
    <pre>
        A foreign key is a column or group of columns in a relational database table that provides a 
        link between data in two tables. It acts as a cross-reference between tables because it references 
        the primary key of another table, thereby establishing a link between them.
    </pre>

2. ### **Search in Django**
    <pre>
        It enables a search box on the admin change list page. This should be set to a list
        of field names that will be searched whenever somebody submits a search query
        in that text box.
        These fields should be some kind of text field, such as CharField or TextField.
            search_fields = ['foreign_key__related_fieldname']
    </pre>

3. ### **Mark safe**
    <pre>
        It helps to indicate that the text is trusted (i.e. not coming from userinput).
        Strings that can be displayed safely without further escaping in HTML can be
        done by the means of mark_safe.
    </pre>

4. ### **Meta**
    <pre>
        In Django, Meta is just used to pass information into the process of creating the
        _meta Options object. Django's Model class specifically handles having an
        attribute named Meta which is a class.
    </pre>

5. ### **Read-only fields**
    <pre>
        It makes it in a way so that, Django will read from your fields in our database, but
        never try to write them. It can be useful if our fields are populated by triggers or
        something.
    </pre>

## **Procedure:**

1. For implementation of search and other enchancement in admin panel 
we will go to "admin.py".Then,
    * Replace
        ```python

        admin.site.register(Product)

        ```
    * With
        ```python

        class ProductAdmin(admin.ModelAdmin):
            list_display = ["name", "price", "brand", "category",]
            search_fields = ["name", "price", "brand__name", "category__name",]
            list_filter = ["brand","category",]
            #readonly_fields = ["quantity",]
        
        class Meta:
            model = Product
        admin.site.register(Product, ProductAdmin)
        
        ```
2. After that we do same kind of changes in Brand and Category model.
3. For dispaying image in admin panel on product page we will use mark_safe
    ```python

    ...
    from django.utils.html import mark_safe
    ...
    class Product(models.Model):
        ...
        def image_tag(self):
            return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
        image_tag.short_description = "Product"
        def __str__(self):
            return self.name

    ```
4. We will run the project and navigate to admin panel.
    * python manage.py runserver

5. In admin panel we will check if image is shown or not and perform various search and filter operatons. 

## **Observation:**

> 1.  There’s the usage of search (e.g. brand_name) for the referenced table
(referenced by foreign key, e.g. brand) and field in the referenced table (name).
> 2. Notice the usage of mark_safe to mark a custom string as a safe string for
HTML/output rendering.
> 3. mark_safe needs to be imported from django.utils.html for the image tag to be
used safely without causing any problem in the admin. It helps to indicate that
the text is trusted (i.e. not coming from userinput).
> 4. readonly_fields should either be nullable or have a database default or be filled
by a trigger.
> 5. When somebody does a search in the admin search box, Django splits the search
query into words and returns all objects that contain each of the words.
> 6. {self.image_url} needs to have the image’s URL source of an image and not
directly copied from the search list.
> 7. In the case of readonly_fields, there can be the input of items into the fields other
than the one which has been taken as read-only.

## **Conclusion:**
<pre>
    Thus, the lab was conducted successfully which helped us to learn more about Foreign
    Key, search and filter operations involved in the admin panel. We also learned to display
    the product’s image and mark safe.
</pre>