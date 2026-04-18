# Installation

## Software requirements

- Python 3.12.3
- BEDTools
- gffread
- numpy
- pandas
- torch
- selene_sdk
- pyBigWig
- scipy
- matplotlib
- tabix

## Obtain Deep-TEIRI

```bash
git clone https://github.com/janky-yz/Deep-TEIRI.git
```

## Inputs you should prepare

- GTF files generated from short-read RNA-seq transcript assembly (for example, StringTie output)
- Two CPM-normalized bigWig files (uniquely mapped reads and multi-mapped reads)
- TE annotation BED file
- Reference annotation GTF file
- Reference FASTA file
- Chromosome length file
