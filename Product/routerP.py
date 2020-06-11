class App1DBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Product':
            return 'productDB'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Product':
            return 'productDB'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Product' and \
                obj2._meta.app_label == 'Product':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'productDB':
            if model._meta.app_label == 'Product':
                return True
        elif model._meta.app_label == 'Product':
            return False
        return None
