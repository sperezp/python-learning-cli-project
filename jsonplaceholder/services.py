import importlib.util
import inspect
import os


class ServiceBase:
    def run_action(self, action):
        if action.lower() == "get_all":
            return self.get_all()
        return None

    def get_all(self):
        pass


def get_service_by_name(name):
    service_path = os.getcwd() + "/jsonplaceholder/" + name + "/service.py"
    print(service_path)
    spec = importlib.util.spec_from_file_location("service", service_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for attr in dir(module):
        object = getattr(module, attr)
        if inspect.isclass(object) and issubclass(object, ServiceBase):
            return object()
    return None
