#!/usr/bin/python3

import glob
import re

base_dir = ".."
file_dirs = [
    "execution/include/beman/execution/detail",
    "task/include/beman/task/detail"
    ]

get_name = re.compile(r".*/([^/]*)\.hpp")
get_include = re.compile(r"\s*#\s*include\s*<.*/([^/]*)\.hpp>.*")

components = []
dependencies = {}

def process_file(component, filename):
    for line in open(filename):
        m = get_include.match(line)
        if m:
            if component in dependencies:
                dependencies[component].append(m.group(1))
            else:
                dependencies[component] = [m.group(1)]

def process_filename(filename):
    m = get_name.match(filename)
    component = m.group(1)
    components.append(component)
    process_file(component, filename)

for d in file_dirs:
    pattern = f"{base_dir}/{d}/*.hpp"
    for f in glob.glob(pattern):
        process_filename(f)

process_filename(f"{base_dir}/execution/include/beman/execution/execution.hpp")

for k in dependencies:
    for d in dependencies[k]:
        print(f"{k} {d}")