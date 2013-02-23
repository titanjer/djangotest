
syncdb ouput
------------

    (djangotest)jmlin@[djangotest]> python manage.py syncdb --noinput
    > __name__:  sub_app.base 
    
    >> decl.__name__:  Some
    >> decl.__module__:  sub_app.base.models
    >> decl._meta.db_table:  ChangeName => ChangeName
    >> decl._meta.app_label:  base => sub_app
    
    >> decl.__name__:  Base
    >> decl.__module__:  sub_app.base.models
    >> decl._meta.db_table:  base_base => sub_app_base
    >> decl._meta.app_label:  base => sub_app
    
    Creating tables ...
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table ChangeName
    Creating table sub_app_base
    Creating table sub_app_root
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)


check ContentType
-----------------

    (djangotest)jmlin@[djangotest]> python manage.py shell
    
    Python 2.7.1 (r271:86832, Jun 25 2011, 05:09:01)
    Type "copyright", "credits" or "license" for more information.
    
    IPython 0.13.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: from django.contrib.contenttypes.models import ContentType
    
    In [2]: for o in ContentType.objects.all():
        print 'app_label: ' + o.app_label
        print 'model: ' + o.model
        print 'name: ' + o.name
        print
       ...: 
    SELECT "django_content_type"."id",
           "django_content_type"."name",
           "django_content_type"."app_label",
           "django_content_type"."model"
    FROM "django_content_type"
    ORDER BY "django_content_type"."name" ASC  [1.20ms]
    
    app_label: sub_app
    model: base
    name: base
    
    app_label: contenttypes
    model: contenttype
    name: content type
    
    app_label: auth
    model: group
    name: group
    
    app_label: auth
    model: permission
    name: permission
    
    app_label: sub_app
    model: root
    name: root
    
    app_label: sessions
    model: session
    name: session
    
    app_label: sites
    model: site
    name: site
    
    app_label: sub_app
    model: some
    name: some
    
    app_label: auth
    model: user
    name: user
    
