import sys
from io import BytesIO
import pickle as _pickle

ALLOWED_PICKLE_MODULES = ['__main__', 'app']
UNSAFE_NAMES = ['__builtins__',]


class SafeDeserialize(_pickle.Unpickler):
    def find_class(self, module, name):
        print(module, name,flush=True)
        if (module in ALLOWED_PICKLE_MODULES and not any(name.startswith(f"{name_}.") for name_ in UNSAFE_NAMES)):
            return super().find_class(module, name)
        raise _pickle.UnpicklingError()
def unpickle(data):
    return SafeDeserialize(BytesIO(data)).load()
