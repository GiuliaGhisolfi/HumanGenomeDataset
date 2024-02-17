# Human Genome Reference Sequence

This repository contains a dataset loaded from the Reference Sequence (RefSeq) Database.

[RefSeq](https://www.ncbi.nlm.nih.gov/refseq/) is the National Center for Biotechnology Information (NCBI) database, that contains reference sequences. It is a curated, non-redundant set including genomic DNA contigs, mRNAs, and proteins for known genes, and entire chromosomes.

The dataset was obtained from the RefSeqGene section of the Reference Sequence Database for [Homo sapiens gene](https://ftp.ncbi.nih.gov/refseq/H_sapiens/RefSeqGene/).

## Dataset

The dataset is included in the folder `human_genome.zip`.

- `human_genoma_rna.pkl`: Contains RNA sequence data.
- `human_genoma_protein.pkl`: Contains protein sequence data.
- `human_genoma_protein_coding_seq.pkl`: This is a subset of `human_genoma_rna.pkl` and contains only sequences that are protein coding.

For more information about the datasets and the analyses performed, please refer to the notebook [EDA.ipynb](EDA.ipynb).


Load repository:
```
git clone https://github.com/GiuliaGhisolfi/HumanGenomeDataset.git
```

Import dataset:
```
from HumanGenomeDataset.load_dataset import load_dataset

protein_coding_sequences_df = load_dataset('dna_protein_coding_sequences')
rna_sequences_df = load_dataset('rna_sequences') 
protein_sequences_df = load_dataset('protein_sequences')
```