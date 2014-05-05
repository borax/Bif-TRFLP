Bif-TRFLP
=========

Scripts used for analysis of Bif-TRFLP and LIAR data

The Bif-TRFLP method was first published by Lewis et. al (http://www.ncbi.nlm.nih.gov/pubmed/23261904). LIAR is a yet-to-be-published method for subspecies-level identification of Bifidobacterium longum.  

The Spreadsheet Splitter script was authored by Sam Westreich and Zac Lewis, and allows for raw exported electropherogram data from Peakscanner (http://www.lifetechnologies.com/order/catalog/product/4381867) to be split into individual files for each sample (and each treatment, Hae, Alu, and LIAR) in a way that is compatible with the analysis pipeline in Abdo et al. (http://onlinelibrary.wiley.com/doi/10.1111/j.1462-2920.2005.00959.x/abstract). To ensure compatibility, you must enter a unique sample name in UD1 in Peakscanner, the sample's type (Alu, Hae, or Liar) in UD2, and a uniqe sample number (starting at 1) in UD3. Run the Spreadsheet splitter on an "export all" file first to generate individual files for each sample. Then the analysis pipeline then follows instructions here http://www.webpages.uidaho.edu/~joyce/Lab%20page/TRFLP-STATS.html. 

The R Filtering and Binning Script, R Cover Program, and Perl scrpit to generate R script for specific individual files are not my work (authored by Zaid Abdo as far as I know), but in the spirit of openness and reproducibility I am including them here. They can also be currently (5/5/2014) found at:
http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/FilteringandBinning.txt
http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/CoverProgram.txt
http://www.webpages.uidaho.edu/~joyce/Lab%20page/16SRNA/AutomaticProgR.txt
At one point their webpage disappeared and was re-worked, leading to older links to the scripts (such as the one published in their paper) to be broken. Hopefully including their script on GitHub leads to a more permanent solution to code sharing.
