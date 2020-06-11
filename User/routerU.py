class App2DBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'User':
            return 'productDB'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'User':
            return 'productDB'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'User' and \
                obj2._meta.app_label == 'User':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'productDB':
            if model._meta.app_label == 'User':
                return True
            else:
                return False
        elif model._meta.app_label == 'User':
            return False
        return None