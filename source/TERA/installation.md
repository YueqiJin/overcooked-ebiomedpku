# Installation

## Software requirements

1. Required: Python 3 (pandas, numpy), R
2. TERA detect (TE identification): SERVE (v1.0), StringTie (v2.1.1), Telescope (v1.0.3)
3. TERA anno (TE annotation): BEDTools (v2.27.1)
4. TERA quant (TE quantification): Telescope (v1.0.3), RSEM (v1.2.28) or Kallisto (0.44.0)

## Install via conda

```bash
conda env create -n tera -f environment.yml
conda activate tera
conda install -c bioconda gffread=0.12.1 stringtie bedtools
```

## Install via singularity

```bash
singularity build TERA.sif TERA.def
```

## Obtain TERA

```bash
git clone https://github.com/janky-yz/TERA.git
chmod u+x TERA/script/TERA
```
