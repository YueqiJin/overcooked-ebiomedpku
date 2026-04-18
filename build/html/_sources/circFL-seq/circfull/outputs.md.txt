# Output files

| File name | Details |
|---|---|
| `circFL_Normal.txt` | Normal circRNA isoforms detected by `RG`, `cRG`, `sRG` |
| `circFL_Normal_pass.txt` | Final circRNA isoforms from `mRG` |
| `circFL_Fusion.txt` | Fusion circRNA isoforms detected by `RG` |
| `novoCluster.txt` | CircRNA isoforms detected by `DNSC` with `-c` |
| `circ_Var.txt` | Variants in circRNAs detected by `var` |
| `geneCountDf.txt` | Gene expression quantified by `geneExp` |
| `strandedFq.fastq` | Transcript-strand circFL-seq reads from `strand` |
| `circ_anno.txt` | Full-length circRNA annotations from `anno` |

## circFL_Normal.txt / circFL_Normal_pass.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | circID | circRNA ID |
| 2 | isoID | isoform ID |
| 3 | chr | Chromosome |
| 4 | start | Start coordinate |
| 5 | end | End coordinate |
| 6 | len | circRNA length |
| 7 | exonNum | Number of exons |
| 8 | exon_start | Exon start coordinates |
| 9 | exon_end | Exon end coordinates |
| 10 | motif | Back-splice motif |
| 11 | leftSeq | Start-junction motif |
| 12 | rightSeq | End-junction motif |
| 13 | exon_leftSeq | Exon-start-junction motif |
| 14 | exon_rightSeq | Exon-end-junction motif |
| 15 | strand | Strand |
| 16 | geneName | Gene name |
| 17 | readCount | Supporting read count |
| 18 | readID | Supporting read IDs |

## circFL_Fusion.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | circID | circRNA ID |
| 2 | isoID | Isoform ID |
| 3 | chr_first | Chromosome of first locus |
| 4 | start_first | Start coordinate of first locus |
| 5 | end_first | End coordinate of first locus |
| 6 | len_first | Length of first locus |
| 7 | exonNum_first | Exon number of first locus |
| 8 | exon_start_first | Exon start coordinates (first locus) |
| 9 | exon_end_first | Exon end coordinates (first locus) |
| 10 | exon_leftSeq_first | Exon start-junction motif (first locus) |
| 11 | exon_rightSeq_first | Exon end-junction motif (first locus) |
| 12 | strand_first | Strand of first locus |
| 13 | geneName_first | Gene name of first locus |
| 14 | chr_second | Chromosome of second locus |
| 15 | start_second | Start coordinate of second locus |
| 16 | end_second | End coordinate of second locus |
| 17 | len_second | Length of second locus |
| 18 | exonNum_second | Exon number of second locus |
| 19 | exon_start_second | Exon start coordinates (second locus) |
| 20 | exon_end_second | Exon end coordinates (second locus) |
| 21 | exon_leftSeq_second | Exon start-junction motif (second locus) |
| 22 | exon_rightSeq_second | Exon end-junction motif (second locus) |
| 23 | strand_second | Strand of second locus |
| 24 | geneName_second | Gene name of second locus |
| 25 | readCount | Supporting read count |
| 26 | readID | Supporting read IDs |

## novoCluster.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | ID | Read ID |
| 2 | cluster | Cluster ID |
| 3 | strand | 1/0 for sense/antisense transcript strand |
| 4 | readLen | Read length |
| 5 | start | Start of tandem repeats |
| 6 | end | End of tandem repeats |
| 7 | consLen | Consensus length |
| 8 | copyNum | Tandem repeat copy number |
| 9 | usage | Proportion of tandem repeats |
| 10 | consensus | Consensus sequence |

## circ_Var.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | isoID | Isoform ID |
| 2 | chr | Chromosome |
| 3 | pos | Variant coordinate |
| 4 | ref | Reference base |
| 5 | alt | Alternative base |
| 6 | refCount | Reads supporting reference base |
| 7 | altCount | Reads supporting alternative base |
| 8 | ratio | Alternative-base ratio |

## geneCountDf.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | geneID | Ensembl gene ID |
| 2 | geneName | Gene name |
| 3 | num | Supporting read count |
| 4 | ratio | Read count ratio among genes |

## circ_anno.txt

| No. | Column | Details |
|:---:|---|---|
| 1 | chr | Chromosome |
| 2 | start | Start coordinate |
| 3 | end | End coordinate |
| 4 | isoID | Isoform ID |
| 5 | strand | Strand |
| 6 | exon_start | Exon start coordinates |
| 7 | exon_end | Exon end coordinates |
| 8 | len | circRNA length |
| 9 | start_type | Start-site annotation type |
| 10 | end_type | End-site annotation type |
| 11 | geneName | Gene name |
| 12 | detail_type | Detailed isoform annotation |
