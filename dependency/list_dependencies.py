import os, json

ignore = ['.git', 'node_modules', '.idea']


def get_json_file_list_of_dic(scan_path):
    package_list = []
    for root, dirs, files in os.walk(scan_path):
        dirs[:] = [d for d in dirs if d not in ignore]
        for file in files:
            if file not in ignore and file == "package.json":
                path = os.path.join(root, file)
                package_list.append({"path": path, "name": file})
    return package_list


def get_package_json_object(path_info:dict):
    data = None
    with open(path_info['path']) as f:
        data = json.load(f)
    return data


def print_dependencies(dependency: dict):
    for library in dependency:
        print("Library : " + library + " Version : " + dependency[library])


def list_dependencies(path_info: dict):
    package_json_object = get_package_json_object(path_info)
    if "dependencies" in package_json_object:
        print_dependencies(package_json_object['dependencies'])
    if "devDependencies" in package_json_object:
        print_dependencies(package_json_object['devDependencies'])


def process():
    source_root = "D:\\business-ledger-ui"
    packages = get_json_file_list_of_dic(source_root)
    for package in packages:
        list_dependencies(package)


if __name__ == '__main__':
   process()
