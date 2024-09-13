import mp4_merger
import os

def get_folders_in_directory(directory):
    # List all entries in the directory and filter only folders
    folders = [os.path.join(directory,name) for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    return folders

def delete_files(files):
    for file in files:
        os.remove(file)
        
def check_for_output_file(files):
    for file in files:
        if "output.MP4" in file:
            return True
    return False


def merge_file(folder,delete = False):
    files = os.listdir(folder)

    files = [os.path.join(folder, file) for file in files if file.endswith(".MP4")]
    # files = ["G:\GoPro Vids\August 31, 2024 18_43\GX010019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX020019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX030019.MP4"]
    print(files)
    if not check_for_output_file(files) and len(files) > 1:
        output_file = f"{folder}\{folder}_output.MP4"
        print(files)
        try:
            mp4_merger.merge_videos(files, output_file)
            print("Videos merged successfully!")
            if delete:
                delete_files(files)
            return True
        except Exception as e:
            print(f"Error during merging: {e}")
            return False
            


def merge_files(FOLDER = "G:\GoPro Vids",delete = False):

    folders  = get_folders_in_directory(FOLDER)

    for i,folder in enumerate(folders[:3]):
        
        merge_file(folder,delete)

                
        print(f"{i+1}/{len(folders)} folders processed")