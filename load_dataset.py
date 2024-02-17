import pandas as pd
import zipfile

ZIP_FILE_PATH = 'zip_files/'
FOLDER_PATH = 'human_genome/'
PROTEIN_PATH = 'human_genome/human_genome_protein.pkl'


def concatenate_datasets(datasets_name, number_of_files):
    df = pd.DataFrame()
    for i in range(number_of_files):
        with zipfile.ZipFile(ZIP_FILE_PATH+datasets_name+'_{}.zip'.format(i+1), 'r') as zip_ref:
            zip_ref.extractall(FOLDER_PATH)
        df = pd.concat([df, pd.read_pickle(datasets_name+'_{}/'.format(i+1)+datasets_name+'_{}.pkl'.format(i+1))])
    return df
    

def load_dataset(dataset_name):
    # unzip file and load the dataset
    if dataset_name == 'dna_protein_coding_sequences':
        return concatenate_datasets(datasets_name='human_genome_protein_coding_sequence', number_of_files=8)
    
    elif dataset_name == 'rna_sequences':
        return concatenate_datasets(datasets_name='human_genome_rna', number_of_files=10)
    
    elif dataset_name == 'protein_sequences':
        with zipfile.ZipFile(ZIP_FILE_PATH+'human_genome_protein.zip', 'r') as zip_ref:
            zip_ref.extractall(FOLDER_PATH)
        return  pd.read_pickle(PROTEIN_PATH)
    
    else:
        print('Invalid dataset name, please choose from: dna_protein_coding_sequences, rna_sequences, protein_sequences')
        return None