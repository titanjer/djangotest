import django.db.models        
import sys                     

from models import *

print '> __name__: ', __name__, '\n'

appname = "sub_app"
for decl in globals().values(): 
    try:
        if decl.__module__.startswith(__name__) and issubclass(decl, django.db.models.Model):
            print '>> decl.__name__: ', decl.__name__
            print '>> decl.__module__: ', decl.__module__
            tmp_db_table = decl._meta.db_table
            tmp_app_label = decl._meta.app_label

            # 
            modelname = decl.__name__.lower()
            if decl._meta.db_table == '%s_%s' % (decl._meta.app_label, modelname):
                decl._meta.db_table = '%s_%s' % (appname, modelname)
            decl._meta.app_label = appname   
            django.db.models.loading.register_models(appname, decl)

            print '>> decl._meta.db_table: ', tmp_db_table, '=>', decl._meta.db_table
            print '>> decl._meta.app_label: ', tmp_app_label, '=>', decl._meta.app_label
            print

    except:
        pass

