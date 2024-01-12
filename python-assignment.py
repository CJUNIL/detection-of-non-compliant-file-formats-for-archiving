import os
import matplotlib.pyplot as plt

def get_folder_path():
    while True:
        folder_path = input("Enter the folder path for analysis: ")
        if not folder_path or not os.path.exists(folder_path):
            print(f"Error: Invalid folder path '{folder_path}'. Please try again.")
        elif not os.listdir(folder_path):
            print(f"This folder is empty, please try another folder")
        else:
            return folder_path

def read_archiving_formats():
    return set(line.strip().lower() for line in open("archiving_formats.txt"))

def list_non_conform_files(folder_path, archiving_formats):
    non_conform_files = []
    number_of_conform_files = volume_gb_of_conform_files = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path, file_extension = os.path.join(root, file), file.split(".")[-1].lower()
            if file_extension in archiving_formats:
                number_of_conform_files += 1
                volume_gb_of_conform_files += os.path.getsize(file_path) / (1024 ** 3)
            else:
                non_conform_files.append(file_path)
    
    non_conform_files.sort(key=lambda x: (os.path.splitext(x)[1], x))
    return number_of_conform_files, volume_gb_of_conform_files, non_conform_files

def plot_pie_chart(number_of_conform_files, number_of_non_conform_files):
    labels, sizes, colors = ['Conform', 'Non-Conform'], [number_of_conform_files, number_of_non_conform_files], ['green', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Conformance Summary')
    plt.show()

def plot_histogram(non_conform_files):
    if not non_conform_files:
        print("No non-conform files to plot.")
        return
    extensions = [os.path.splitext(file)[1] for file in non_conform_files]
    unique_extensions, counts = zip(*sorted(((ext, extensions.count(ext)) for ext in set(extensions)), key=lambda x: x[1], reverse=True))
    plt.bar(unique_extensions, counts)
    plt.xlabel('File Extensions')
    plt.ylabel('Count')
    plt.title('Non-Conform File Extensions')
    plt.show()

def print_summary(number_of_conform_files, volume_gb_of_conform_files, non_conform_files):
    volume_gb_of_non_conform_files = round(sum(os.path.getsize(file) for file in non_conform_files) / (1024 ** 3), 2)
    print(("--- SUMMARY ---"))
    print(f"\n{number_of_conform_files} conform files corresponding to {volume_gb_of_conform_files:.2f} GB")
    print(f"\n{len(non_conform_files)} non-conform files corresponding to {volume_gb_of_non_conform_files:.2f} GB")
    print("\nList of non-conform files:")
    for file_name in non_conform_files:
        print(f"- {file_name}")

def main():
    while True:
        folder_path = get_folder_path()
        archiving_formats = read_archiving_formats()
        number_of_conform_files, volume_gb_of_conform_files, non_conform_files = list_non_conform_files(folder_path, archiving_formats)
        volume_gb_of_conform_files = round(volume_gb_of_conform_files, 2)
        number_of_non_conform_files = len(non_conform_files)
        print_summary(number_of_conform_files, volume_gb_of_conform_files, non_conform_files)
        plot_pie_chart(number_of_conform_files, number_of_non_conform_files)
        plot_histogram(non_conform_files)
        another_folder = input("\nDo you want to look at another folder? (yes/no): ").lower()
        if another_folder != 'yes':
            break
if __name__ == "__main__":
    main()