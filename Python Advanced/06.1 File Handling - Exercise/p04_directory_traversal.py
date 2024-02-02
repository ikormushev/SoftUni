import os


def file_check(given_directory, dir_first_level=False):
    for file_name in os.listdir(given_directory):
        file = os.path.join(given_directory, file_name)

        if os.path.isfile(file):
            file_extension = "." + file_name.split(".")[-1]
            if file_extension not in files_by_extensions:
                files_by_extensions[file_extension] = []
            files_by_extensions[file_extension].append(file_name)

        elif os.path.isdir(file) and not dir_first_level:
            file_check(file, dir_first_level=True)


files_by_extensions = {}

directory = input()
if "\\" in directory:
    split_directory = directory.split("\\")
    directory = os.path.join(*split_directory)
elif "/" in directory:
    split_directory = directory.split("/")
    directory = os.path.join(*split_directory)

file_check(directory)

sorted_files_extensions = dict(sorted(files_by_extensions.items(), key=lambda d: d[1]))

for (extension, files) in sorted_files_extensions.items():
    sorted_files = sorted(files)
    sorted_files_extensions[extension] = sorted_files

report_file_path = os.path.join(directory, "report.txt")

with open(report_file_path, "w") as report_file:
    for (extension, files) in sorted_files_extensions.items():
        report_file.write(f"{extension}\n")
        for file in files:
            report_file.write(f"- - - {file}\n")
