# Installation

## Availability

circfull source code is available at:

- https://github.com/yangence/circfull

## Dependencies

Install the following tools before running circfull:

- minimap2 (>=2.1)
- bedtools (>=2.29.2)
- samtools (>=1.6)
- porechop (0.2.4)

The circfull repository also includes TideHunter (1.0) and TRF (4.09).

Python 3 is required with these packages:

- pysam
- numpy
- pandas
- python-intervals
- pyfasta
- sklearn
- interval
- mappy
- progressbar
- docopt

## Install from pip

```bash
pip install circfull
```

## Install from source

```bash
git clone https://github.com/yangence/circfull.git
cd circfull/script
pip install -r requirements.txt
python setup.py install
```

If installing `pyfasta` fails with pip, try installing it via conda.

## Required reference files

### 1. Indexed genome FASTA

```bash
samtools faidx $genome
```

### 2. Tabix-indexed gene annotation GTF

```bash
grep -v '#' $gtf | sort -k 1,1 -k 4,4n | bgzip > sort.gtf.gz
tabix sort.gtf.gz
```

### 3. Repetitive elements (optional)

Optional repetitive-element annotations can be downloaded from:

- https://genome.ucsc.edu/cgi-bin/hgTables
