import pandas as pd
import zipfile

FOLDER_PATH = 'human_genome.zip'
DNA_PROTEIN_CODING_PATH = 'human_genome/human_genome_protein_coding_seq.pkl'
RNA_PATH = 'human_genome/human_genome_rna.pkl'
PROTEIN_PATH = 'human_genome/human_genome_protein.pkl'

def load_dataset(dataset_name):
    # Unzip the file
    with zipfile.ZipFile(FOLDER_PATH, 'r') as zip_ref:
        zip_ref.extractall('human_genome/')

    # Load the dataset
    if dataset_name == 'dna_protein_coding_sequences':
        return  pd.read_pickle(DNA_PROTEIN_CODING_PATH)
    elif dataset_name == 'rna_sequences':
        return  pd.read_pickle(RNA_PATH)
    elif dataset_name == 'protein_sequences':
        return  pd.read_pickle(PROTEIN_PATH)
    else:
        print('Invalid dataset name, please choose from: dna_protein_coding_sequences, rna_sequences, protein_sequences')
        return None