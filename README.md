# mtbDrugResistance
Signatures of selection at drug resistance loci in Mycobacterium tuberculosis

### Rmarkdown
#### drugResistancePopGenSummary.Rmd
Rmarkdown file with code to process and plot upstream analyses
#### drugResistancePopGenSummary.html
HTML file produced from Rmarkdown

### data
#### 160129_Mtb_removeRegions_mergedCloserThan1000bp.bed
Repetitive regions masked from all alignments
#### bydrug_stats.txt
Diversity statistics for alignments of susceptible and resistant subpopulations of first and second line drugs
#### drugSpecificStats_lineage2.txt
Diversity statistics for alignments of susceptible and resistant subpopulations in L2
#### drugSpecificStats_lineage4.txt
Diversity statistics for alignments of susceptible and resistant subpopulations in L4
#### drugSusceptibilityTotals.txt
Drug susceptibility from phenotypic data
#### fst_cutoffs.txt
Maximum Fst values when susceptibility is randomly assigned
#### functionalCategories.TXT
Functional categories previously used in O'Neill et al. 2015 for functional enrichment tests
#### gappedPositions_5percThreshold.txt
Positions where > 5% of isolates have a gap or missing data character
#### geneLengths.txt
Gene lengths from H37Rv annotation
#### genewise_pi.txt
Pi values for each gene in resistant and susceptible subpopulations
#### genewise_theta.txt
Theta values for each gene in resistant and susceptible subpopulations
#### genewiseStats.txt
Diversity statistics for each gene using entire sample
#### genewiseStats_lineage2.txt
Diversity statistics for each gene in L2
#### genewiseStats_lineage4.txt
Diversity statistics for each gene in L4
#### homoplastic_indels.txt
List of indels identified as homoplastic
#### homoplastic_merged_indels.txt
List of indels indentified as homoplastic when indels from the same gene are considered identical
#### homoplastic_snps_counts.txt
List of homoplastic SNPs and the number of times they occcur on the phylogeny
#### indel_descriptions.txt
Indel names, types, and impacted genes
#### lineage2_genewise_pi.txt
Pi values for each gene in resistant and susceptible subpopulations in L2
#### lineage2_genewise_theta.txt
Theta values for each gene in resistant and susceptible subpopulations in L2
#### lineage2_wcFst_mergedIndels.txt
Fst values for indels in L2
#### lineage4_genewise_pi.txt
Pi values for each gene in resistant and susceptible subpopulations in L4
#### lineage4_genewise_theta.txt
Theta values for each gene in resistant and susceptible subpopulations in L4
#### lineage4_wcFst_mergedIndels.txt
Fst values for indels in L4
#### merged_indels_description.txt
Genes and types of indels after merging
#### mtb_drugResistance_snps.txt
Location, type, and gene of all SNPs in alignments
#### resistanceGeneNames.txt
List of resistance loci
#### rv_numbers.txt
Rv numbers for genes in H37Rv genome
#### tree.newick
Phylogenetic tree estimated with FastTree
#### wcFst.txt
Fst values for SNPs
#### wcFst_indels.txt
Fst values for indels
#### wcFst_indels_lineage2.txt
Fst values for indels in L2
#### wcFst_indels_lineage4.txt
Fst values for indels in L4
#### wcFst_lineage2.txt
Fst values for SNPs in L2
#### wcFst_lineage4.txt
Fst values for SNPs in L4
#### wcFst_mergedIndels.txt
Fst values of indels when indels from the same gene are considered identical
#### wholeAlignmentDiversity.txt
Diversity values for entire alignment

### scripts
#### combineIndels.py  
Merges indels in the same gene
#### randomizeFst.py  
Calculates Fst after randomly assigning populations
#### runFst.py  
Calculates Fst
#### selectionStats.py
Calculates diversity statistics for alignments


### tables
#### accessions.txt
Accession numbers and lineage designation for sequence data used (Supplementary Table 1)
#### drGenesStats.txt
Signatures of selection in known drug resistance genes (Table 2)
#### fst_homoplasy_table.txt
Homoplastic Fst outliers (Table 3)

### tbdream_DB
#### tbdreamDB.csv
Edited CSV of TB Drug Resistance Database that can be parsed in R (orginally obtained from https://tbdreamdb.ki.se/Info/)
