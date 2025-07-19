from typing import Type, Any


def typedproperty(name: str, expected_type: Type[Any]):
    '''Creates a private property and a setter for it with provided type.'''
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value: Any):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}, but {type(value)} given')
        setattr(self, private_name, value)

    return prop

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)