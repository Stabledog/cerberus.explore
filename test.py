import yaml 
from cerberus import Validator


def load_doc():
    with open('./my_yaml.yaml', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exception:
            raise exception

schema = eval(open('./schema.py', 'r').read())
v = Validator(schema)
doc = load_doc()
print( v.validate(doc, schema))
print( v.errors)

