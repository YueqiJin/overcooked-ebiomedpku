# ucircFL-seq Library Construction

## Materials and Reagents
1. Ethanol
2. DNase/RNase-free water
3. Thermostable RNase H (NEB, catalog number: M0523)
4. DNase I (NEB, catalog number: M0303S)
5. ATP (10 mM) (NEB, catalog number: P0756S)
6. Poly(A) Polymerase (NEB, catalog number: M0276S)
7. RNA Clean Beads (Vazyme, catalog number: N411-01/02)
8. RNase R (Lucigen, catalog number: RNR0725)
9. Equalbit RNA BR Assay Kit (Vazyme, catalog number: EQ212-01)
10. dATP (NEB, catalog number:N0440S)
11. ddATP (Jena Bioscience, catalog number: NU-1015S)
12. HiScript III 1st Strand cDNA Synthesis Kit (Vazyme, catalog number: R312-01/02) or SuperScript IV First-Strand Synthesis System (Invitrogen, catalog number: 18091050)
13. DNA Clean Beads (Vazyme, catalog number: N412-01/02)
14. Terminal deoxynucleotidyl transferase (TDT) (Invitrogen, catalog number: EP0161)
15. UltraHiFi Master Mix (Tiangen, catalog number: KP213-02)
16. SYBR Green I (10000×) (Solarbio, catalog number: SY1020)
17. Equalbit 1× dsDNA HS Assay Kit (Vazyme, catalog number: EQ121-01)
18. First-strand synthesisprimer P1N-UMI-N6: CTACACGACGCTCTTCCGATCTCNNNYRNNNYRNNNYRNNNGAG(N)6(6 randomized mixed bases)
19. Second-strand synthesis primer P2N-T24: AAGCAGTGGTATCAACGCAGAG(T)24(24 consecutive Ts as reverse-complement to polyA)
20. PCR primers: P1N (CTACACGACGCTCTTCCGATCT), P2N (AAGCAGTGGTATCAACGCAGAG)
21. NEBNext FFPE DNA Repair Mix (NEB, catalog number: M6630S)
22. NEBNext Ultra II End repair/dA-tailing Module (NEB, catalog number: E7546S)
23. NEB Blunt/TA Ligase Master Mix (NEB, catalog number: M0367S)
24. NEBNext Quick Ligation Module (NEB, catalog number: E6056S)
25. Nanopore Ligation Sequencing Kit (ONT, catalog number: SQK-LSK110)
26. Nanopore Flow Cell (ONT, catalog number: MinION/PromethION R10.4.1)
27. rRNA probes mix (see Recipes)
28. Probe hybridization buffer (see Recipes)

## Procedure
![ucircFL-seq library construction workflow](../images/ucircFL-seq.png)

*Note: RNA is easily degradable. Clean all surfaces with 70% ethanol and RNase-away solution, change gloves frequently, and sterilize all materials before use.*

### A. circRNA enrichment

#### A1. rRNA depletion
1. Mix total RNA, rRNA probes, and probe hybridization buffer to a final volume of 15 uL.

| Component | Volume per sample |
|---|---|
| Total RNA | 2.0 µg |
| rRNA probes | 1.0 µL |
| Probe hybridization buffer | 2.0 µL |
| Nuclease-free water | to 15.0 µL |

2. Place samples in a thermocycler with heated lid (~105°C). Heat to 95°C for 2 min, slowly cool to 22°C (-0.1°C/s), then incubate at 22°C for 5 min.
3. Add thermostable RNase H and 10x RNase H buffer for a final volume of 20 µL.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 15.0 µL |
| Thermostable RNase H | 2.0 µL |
| 10x RNase H buffer | 2.0 µL |
| Nuclease-free water | 1.0 µL |

4. Incubate at 50°C for 30 min (lid 50°C).
5. Add DNase I reaction components for a final volume of 30 µL.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 20.0 µL |
| DNase I | 2.5 µL |
| 10x DNase I buffer | 3.0 µL |
| Nuclease-free water | 4.5 µL |

6. Incubate at 37°C for 30 min (lid 50°C), then place on ice.

#### A2. Poly(A) tailing and RNase R treatment
1. Add ATP, 10x Poly(A) Polymerase Reaction Buffer, and Poly(A) Polymerase for poly(A) tailing.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 30.0 µL |
| ATP (10 mM) | 4.0 µL |
| 10x Poly(A) Polymerase Reaction Buffer | 4.0 µL |
| Poly(A) Polymerase | 1.0 µL |
| Nuclease-free water | 1.0 µL |

2. Incubate at 37°C for 30 min (lid 50°C), then place on ice.
3. Purify RNA with 2.5x RNA Clean Beads and elute in 8 µL nuclease-free water. Expected yield is ~200 ng RNA.
4. Remove linear RNA using RNase R.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 8.0 µL |
| 1 U/µL RNase R | 1.0 µL |
| 10x RNase R buffer | 1.0 µL |

5. Incubate at 37°C for 30 min, then 70°C for 10 min.

### B. Full-length circRNA cDNA preparation

#### B1. Reverse transcription (first-strand cDNA synthesis)
1. Reverse transcribe enriched circRNA in a 20 µL reaction using P1N-UMI-N6 and HiScript III reverse transcriptase.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 10.0 µL |
| Nuclease-free water | 5.0 µL |
| 10x HiScript III Buffer | 2.0 µL |
| HiScript III mix | 2.0 µL |
| P1N-UMI-N6 | 1.0 µL |

2. Thermocycler program: 25°C for 5 min, 50°C for 50 min, 70°C for 2 min, 85°C for 5 s (lid ~105°C).
3. Purify cDNA using 0.75x DNA Clean Beads.

#### B2. Poly(A) tailing and second-strand cDNA synthesis
1. Add poly(A) tails at 3' ends in a 20 µL reaction using TDT. Final concentrations: dATP 2.5 mM and ddATP 25 µM.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 14.0 µL |
| 100 mM dATP | 0.5 µL |
| 1 mM ddATP | 0.5 µL |
| 5x TDT Buffer | 4.0 µL |
| TDT | 1.0 µL |

2. Incubate at 37°C for 20 min (lid 50°C), then place on ice.
3. Purify cDNA using 0.75x DNA Clean Beads.
4. Synthesize second-strand cDNA with P2N-T24 and UltraHiFi Mix II.

| Component | Volume per sample |
|---|---|
| Last-step reaction | 12.0 µL |
| UltraHiFi Mix II | 13.0 µL |
| 10 µM P2N-T24 | 1.0 µL |

*Note: PCR mix volume may slightly decrease after thorough mixing; total reaction volume remains 25 µL.*

5. Incubate at 98°C for 2 min, 50°C for 2 min, and 72°C for 10 min (lid ~105 °C), then place on ice.

### C. Amplification
#### C1. First time amplification
1. reaction mix preparation:

| Component | Volume per sample |
|---|---|
| Last-step reaction | 26.0 µL |
| 10 µM P1N | 10.0 µL |
| 10 µM P2N | 10.0 µL |
| UltraHiFi Mix II | 112.0 µL |
| Nuclease-free water | 92.0 µL |

*Note: PCR mix volume may slightly decrease after thorough mixing; total reaction volume remains 250 µL.*

2. Cycles determined through qPCR: use 45 µL reaction mix for qPCR with SYBR Green, and run 20-25 cycles of 98°C for 30 s, 55°C for 20 s, and 72°C for 2.5 min (lid ~105 °C). Choose cycle number at the middle of the exponential phase:

```R
library(qpcR)
data <- read.table("qPCR_results.txt", header=TRUE, sep="\t")
pcrfit <- pcrfit(data, 1, 2, model=l4) # pcrfit(data, cycle_column, fluorescence_column, model)
eff <- effenciency(pcrfit)
eff$cpD1
```

3. PCR cycling: cpD1 cycles of 98°C for 30 s, 55°C for 20 s, and 72°C for 2.5 min (lid ~105 °C).
4. Purify with 0.5x DNA Clean Beads and resuspend in 20 µL nuclease-free water.

*Note: During the second bead selection, longer fragments (~1,000 bp) are preferred to further enrich circRNA cDNA library molecules.*

5. Quantify the DNA library with Qubit.

#### C2. Second time amplification
1. Prepare PCR mix:
| Component | Volume per sample |
|---|---|
| Purified first-time PCR product | not more than 8 ng |
| 10 µM P1N | 10.0 µL |
| 10 µM P2N | 10.0 µL |
| UltraHiFi Mix II | 125.0 µL |
| Nuclease-free water | up to 250.0 µL |

2. Cycles determined through qPCR: use 45 µL reaction mix for qPCR with SYBR Green, and run 15-20 cycles of 98°C for 30 s, 55°C for 20 s, and 72°C for 2.5 min (lid ~105 °C). Choose cycle number at the middle of the exponential phase as in the first time amplification step.

3. Run cpD1 cycles of 98°C for 30 s, 55°C for 20 s, and 72°C for 2.5 min (lid ~105 °C).
4. Purify with 0.5x DNA Clean Beads and resuspend in 20 µL nuclease-free water.


#### C3. Sample quality check
1. Quantify library concentration using Qubit. For section C, use 0.5-1 µg cDNA library input.
2. Check fragment distribution with BioAnalyzer. Expected peak is around 1,000 bp; most fragments should range from 600-2,000 bp.
3. If library quality is low, troubleshoot by checking RNA integrity and bead cleanup efficiency, and confirm effective depletion of rRNA/linear RNA in step A.

### D. Nanopore library preparation and sequencing
1. DNA library for barcoding and ligation sequencing can be prepared according to ONT protocols EXP-NBD104 and SQK-LSK110.
2. Repair and dA-tail 0.1-0.5 µg circFL-seq cDNA using NEBNext FFPE DNA Repair Mix and NEBNext Ultra II End Repair/dA-Tailing Module, then purify with 1.5x DNA Clean Beads.
3. For multiplexing, barcode repaired/end-prepped DNA with Native Barcodes using NEB Blunt/TA Ligase Master Mix, then purify with 1x DNA Clean Beads.
4. Pool barcoded samples equimolarly. Ligate 700 ng pooled DNA (or single unbarcoded sample) to ONT adapter using NEBNext Quick Ligation Module, then purify with 0.5x DNA Clean Beads and Short Fragment Buffer.
5. Mix DNA library with sequencing buffer, load onto PromethION or MinION flow cell, and sequence. For downstream analysis, target ~10 million reads (~10 Gb) per sample.
