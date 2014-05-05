Bif-TRFLP
=========

Scripts used for analysis of Bif-TRFLP and LIAR data

The Bif-TRFLP method was first published by Lewis et. al (http://www.ncbi.nlm.nih.gov/pubmed/23261904). LIAR is a yet-to-be-published method for subspecies-level identification of Bifidobacterium longum.  

The File Splitter script was authored by Sam Westreich and Zac Lewis, and allows for raw exported electropherogram data from Peakscanner (http://www.lifetechnologies.com/order/catalog/product/4381867) to be split into individual files for each sample (and each treatment, Hae, Alu, and LIAR) in a way that is compatible with the analysis pipeline in Abdo et al. (http://onlinelibrary.wiley.com/doi/10.1111/j.1462-2920.2005.00959.x/abstract). The pipeline then follows instructions here http://www.webpages.uidaho.edu/~joyce/Lab%20page/TRFLP-STATS.html. 

The Filtering and Binning Script, Cover Program, and Perl --> R scrpit are not my work (authored by Zaid Abdo as far as I know), but in the spirit of openness and reproducibility I am including them here. They can also be currently (5/5/2014) found at http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/FilteringandBinning.txt and http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/CoverProgram.txt and http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/AutomaticProgR.txt). At one point their webpage disappeared and was re-worked, leading to older links to the scripts to be broken. Hopefully including their script on GitHub leads to a more permanent solution to code sharing.

 

