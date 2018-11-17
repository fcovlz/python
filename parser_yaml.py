
import yaml

with open("yamo.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print "Error on YAML file"