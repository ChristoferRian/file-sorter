import os
import shutil

def sorter(path):
    try:
        # Membuat direktori untuk setiap ekstensi file
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                file_extension = filename.split('.')[-1]
                target_directory = os.path.join(path, file_extension)

                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)

                # Pindahkan file ke direktori yang sesuai
                shutil.move(os.path.join(path, filename), os.path.join(target_directory, filename))

        print("File berhasil di-sortir.")
    except FileNotFoundError:
        print("Error: Lokasi folder tidak ditemukan.")

if __name__ == "__main__":
    Lokasi_Folder = input("Masukkan path folder yang ingin di-sortir: ")
    sorter(Lokasi_Folder)
