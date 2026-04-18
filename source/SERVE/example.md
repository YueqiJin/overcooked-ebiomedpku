# Example pipeline

Use the upstream example script:

- https://github.com/janky-yz/SERVE/blob/main/script/example.sh

## Step-by-step commands

### 1. Detecting expressed ERVs per sample

```bash
SERVE.py --fastq1 ${fastq1} --fastq2 ${fastq2} \
	-e ${ref_erv} -r ${ref_genome} -a ${ref_annotation} \
	-t ${nthread} -p ${prefix}
```

### 2. Merging ERV transcripts from multiple samples

```bash
nsample=$(ls ${wrk_dir}/3_qc/*gtf | wc -l)
ls ${wrk_dir}/3_qc/*gtf > ${wrk_dir}/gtf.list
SERVE_merge.py -i ${wrk_dir}/gtf.list -n ${nsample} \
	-r ${ref_genome} -t ${nthread}
```

### 3. Quantifying ERVs

```bash
ERV_annotation=${wrk_dir}/SERVE_ERV_merge.gtf
merge_annotation=${wrk_dir}/GRCh38_ERV_merge.gtf

cat ${ref_annotation} ${ERV_annotation} > ${merge_annotation}
SERVE_quant.py --fastq1 ${fastq1} --fastq2 ${fastq2} \
	-r ${ref_genome} -a ${merge_annotation} -t ${nthread} -p ${prefix}
```

### 4. Merging quantification results and QC

```bash
ls ${wrk_dir}/*genes.results > ${wrk_dir}/sample.list
SERVE_quant_QC.py -i ${wrk_dir}/sample.list -p ${prefix}
```
