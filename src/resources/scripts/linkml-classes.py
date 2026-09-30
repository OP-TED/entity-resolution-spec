"""
An attempt to fix the fact that `linkml generate --no-mergeimports` [doesn't work](https://github.com/linkml/linkml/issues/1296).

This script lists all the classes defined in a LinkML file, possibly in a format that can be passed to the
generator command, ie, as a sequence of `--classes` restrictions.

The problem is this doesn't work either, since the resulting file drags linked imported classes anyway 
into output like a UML diagram.

TODO: delete?
"""
import sys
import yaml
import argparse

def main():
    
    parser = argparse.ArgumentParser(
        description="List class names from the 'classes' section of a LinkML YAML file."
    )
    parser.add_argument("yaml_file", help="Path to the LinkML YAML file")
    parser.add_argument("--prefix", default="", help="Prefix to prepend to each class name")
    args = parser.parse_args()

    with open(args.yaml_file, "r") as f:
        data = yaml.safe_load(f)

    classes = data.get("classes", {})
    for class_name in classes.keys():
        if args.prefix:
            print(f"{args.prefix} {class_name}")
        else:
            print(class_name)

if __name__ == "__main__":
    main()