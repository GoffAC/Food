import os
a_dir = r'C:\Users\Alex\Desktop\Food\www.bbc.co.uk\food'
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]