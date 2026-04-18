# About DEBKS

```{image} ../images/DEBKS-logo.png
:alt: DEBKS
:width: 50%
:align: center
```

## About

DEBKS is a toolkit for detecting differentially expressed circRNA (DEC) between two RNA-seq sample groups with replicates. The pipeline provides four modules:

- merge: collect circular and linear junction counts from circRNA detection outputs
- count: calculate linear junction counts from aligned RNA-seq BAM files
- anno: annotate circRNAs and infer potential lengths
- dec: identify DECs with an rMATS-based statistical model

![DEBKS workflow](../images/DEBKS.png)

## Guides

- [Installation](installation.md)
- [Usage](usage.md)
- [Example workflow](example.md)
- [Import from CIRIquant](import-from-ciriquant.md)

## Citation

If you use DEBKS in your research, please cite:
- Zelin Liu, Huiru Ding, Jianqi She, Chunhua Chen, Weiguang Zhang, Ence Yang, DEBKS: A Tool to Detect Differentially Expressed Circular RNAs, Genomics, Proteomics & Bioinformatics, 2022, 20(3):549-556, https://doi.org/10.1016/j.gpb.2021.01.003.