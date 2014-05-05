#! /usr/bin/perl -w

print "Please type in the directory structure from where to read the input files:\n";
print "Example:    C://Main Storage//Research//Ursel//\n";
chomp($dir_name = <STDIN>);

print "Please enter the general name you want for a file:\n";
print "Example:   MspI\n";
chomp($file_name = <STDIN>);

print "Please enter the first letter (capital) of the color to be processed (B/G/Y):\n";
chomp($color = <STDIN>);
if($color ne 'B'& $color ne 'G' & $color ne 'Y'){die ("not a color")};

print "please enter the number of files you want to process\n";
chomp($numb_files = <STDIN>);

print "Please enter a name of an output file to send the R program to:\n";
chomp($out_file = <STDIN>);

open OUTFILE, ">$out_file";

for($i = 1; $i <= $numb_files; $i++){
   print OUTFILE $file_name.$i.' <- read.table(file="'.$dir_name.$file_name.$i.'.txt",col.names= c("Color", "time", "length", "height", "area", "point"))'."\n";
   print OUTFILE $file_name.$i.'.'.$color.' <- cbind('.$file_name.$i.'[grep("^'.$color.'", as.character('.$file_name.$i.'$Color),perl=T),3],'.$file_name.$i.'[grep("^'.$color.'", as.character('.$file_name.$i.'$Color),perl=T),5])'."\n";
   print OUTFILE $file_name.$i.'.'.$color.' <- cbind('.$file_name.$i.'.'.$color.', '.$file_name.$i.'.'.$color.'[,2]/sum('.$file_name.$i.'.'.$color.'[,2]))'."\n\n";
}
for($j = 1; $j <= $numb_files; $j++){
   push @list, "$file_name$j\.$color"; 
}
$list = join ",",@list;
print OUTFILE $color.'.list <- list('.$list.')'."\n";
print OUTFILE $color.'.Data <- Gfiltering.ftn('.$color.'.list, 3)'."\n";
print OUTFILE $color.'.ClusBin     <- GclustBin.ftn('.$color.'.Data[[1]], 1)'."\n";
print OUTFILE 'write.table(t('.$color.'.ClusBin), file = "'.$dir_name.$color.'.txt",sep="\t",row.names=c(put row names here separated by a comma),col.names=F)'."\n";

close OUTFILE;
