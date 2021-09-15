from django.conf import settings


class RoadDBRouter:

    route_app_labels = {'spatialapp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'road'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'road'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print(app_label)
        if app_label in self.route_app_labels:
            return db == 'road'
        return None

    def allow_relation(self,obj1, obj2, **hints):

        if(
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None


class DefaultDBRouter:

    route_app_labels = {'src'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if(
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None




