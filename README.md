# Human Reference genome

This repository contains a dataset loaded from the Reference Sequence (RefSeq) Database.

[RefSeq](https://www.ncbi.nlm.nih.gov/refseq/) is the National Center for Biotechnology Information (NCBI) database, that contains reference sequences. It is a curated, non-redundant set including genomic DNA contigs, mRNAs, and proteins for known genes, and entire chromosomes.

The dataset was obtained from the RefSeqGene section of the Reference Sequence Database [for Homo sapiens gene](https://ftp.ncbi.nih.gov/refseq/H_sapiens/RefSeqGene/).


The dataset is included in the folder `human_genome.zip`.
To unzip datsets:
```
unzip human_genome.zip
```

- `human_genome_rna.pkl`: Contains RNA sequence data.
- `human_genome_protein.pkl`: Contains protein sequence data.
- `human_genome_protein_coding.pkl`: This is a subset of `human_genome_rna.pkl` and contains only sequences that are protein coding.
For more information about the datasets and the analyses performed, please refer to the notebook [EDA.ipynb](EDA.ipynb).

human_genome_rna.pkl contains data rna sequence
human_genome_protein.pkl
human_genome_protein_coding.pkl è un sub set di human_genome_rna e contiene solo le sequenze che sono protein coding

per più info sui data set, vedi i notebbok EDA.ipynb
