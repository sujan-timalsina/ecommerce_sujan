# **Lab 3 - Search Product for the user**

## **Objective:**
> 1. To perform search and filter operations in the user panel.

## **Introduction:**

1. ### **Template**
    <pre>
        It is the way or blueprint by which the eCommerce website needs to be built. It specifies the working areas for the blocks to be fit into according to the respective tasks.
    </pre>

2. ### **Bootstrap**
    <pre>
        Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
    </pre>

3. ### **Block**
    <pre>
    Block is used for overriding specific parts of a template. In your case, you have a block named content and this is supposed to be overridden by children that inherit from this template. That's where the power of the templates comes from in a sense.
    {% block block_name %}
        ... your block contents go here ...
    {% endblock %}
    </pre>

## **Procedure:**

1. Create a directory “templates” and add a base HTML template file “base.html".
2. To ensure that the “templates/base.html” is available globally, adjust the
TEMPLATES/DIRS setting. Go to “settings.py” and make the following adjustment.
3. Inside “product_module”, create a directory “templates”. Note that this “templates” folder is different from Step #1. Create a html “index.html”.
4. From the project “product_module” open “views.py” and add the code as below for search operation (GET and POST).
5. Run the project and navigate to admin to check the result.

## **Conclusion:**
<pre>
    Thus, the lab was conducted successfully which helped us to learn more about the use of Bootstrap and all the interactive interfaces to be used in the user-panel. We also learned to display the product’s image, use filters and search, help the user to input the products, category and brands directly from the user interface via the Admin url link.
</pre>