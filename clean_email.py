import pandas as pd
import numpy as np
import os

def main():
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Data Cleaning\2024\Feb\7'
    file_name = 'Donor With Invalid Email.xlsx'
    file_path = os.path.join(folder_path,file_name)


    df = pd.read_excel(file_path)

    df['Updated Email'] = df['Email'].apply(lambda x: '' if x == 'noemail@unicef.org' else x)

    new_file_name = 'Donor With Invalid Email - Edited.xlsx'
    new_file_path = os.path.join(folder_path, new_file_name)
    df = df.to_excel(new_file_path, index=False)

    print(f'File {new_file_name} been saved in the folder')

if __name__ == '__main__':
    main()