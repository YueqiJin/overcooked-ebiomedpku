# Installation

## Install ucircfull binary release

```bash
wget https://github.com/YueqiJin/ucircfull/releases/download/v1.1.0/ucircfull-1.1.0-Linux.tar.gz
tar -xzf ucircfull-1.1.0-Linux.tar.gz
/path/to/ucircfull-1.1.0-Linux/bin/ucircfull --help
```

## Install ucircfull from source code

### Dependencies

- cmake >= 3.4
- make
- g++ with C++23 support (GCC >= 13 recommended)
- gcc with C++23 support (GCC >= 13 recommended)
- libboost-all-dev
- libseqan3-dev >= 3.4.0
- libseqan2-dev
- minimap2
- rust
- porechop
- seqkit
- samtools

### Build ucircfull from source code

```bash
git clone https://github.com/yangence/ucircfull.git
cd ucircfull
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
```

### Install ucircfull to a deployment prefix

```bash
cmake --install build --prefix /opt/ucircfull
```

This installs executables to `/opt/ucircfull/bin` and shared libraries to `/opt/ucircfull/lib`.

## Run ucircfull in apptainer

```bash
apptainer pull docker://jinyueqi/ucircfull
apptainer exec /path/to/ucircfull-latest.sif ucircfull --help
```

## Required files

Users can prepare the external files under the following instructions:

1. Indexed genome fasta file

```bash
samtools faidx $genome
```

2. gene annotation GTF file
