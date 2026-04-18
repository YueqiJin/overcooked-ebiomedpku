# Installation

## Availability

DEBKS source code:

- https://github.com/yangence/DEBKS

## Dependencies

Python 3 with:

- pysam
- numpy
- pandas
- scipy

## Install with conda

```bash
conda install -c colinliuzelin DEBKS -c bioconda
```

## Install with pip

```bash
pip install DEBKS
```

## Install from source

```bash
git clone https://github.com/yangence/DEBKS.git
cd DEBKS
pip install -r requirements.txt
python setup.py install
```

## Required files

### 1. Indexed genome FASTA

```bash
samtools faidx $genome
```

### 2. Tabix-indexed gene annotation GTF

```bash
grep -v '#' $gtf | sort -k 1,1 -k 4,4n | bgzip > sort.gtf.gz
tabix sort.gtf.gz
```
