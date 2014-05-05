__author__ = 'Sam Westreich and Zac Lewis'
# Designed to break export file produced by PeakScanner up into different sub-files for analysis in R after running Perl script by Abdo et al.
# Created 3/07/14

print "File must be in default folder, or script will not find it!\n"
filename = raw_input("Type in file name to be processed: ")

sample_number = 0                                       
# sets an initial value for the sample number counter
line_counter = 0

file_in = open(filename, 'r')                           # currently uses default path and ends if file isn't present

for l in file_in:
    line_counter += 1
    array_all = l.split("\t")                           # splits by tab into columns
    array = []
    try:
        array.extend((array_all[11], array_all[0], array_all[13], array_all[14], array_all[15], array_all[9]))
                                                        # 0 = combined sample name and type (Alu, Hae, Liar), 13 = size, 14 = height, 15 = area in points, 8 = Sample Name (UD1) 9 = Sample Type, Alu, Hae, or Liar (UD2), 10 = Sample Number (UD3), 11 = Dye/Sample
    except IndexError:
        print "There seems to be vital data missing at line ", line_counter
        continue                                        # hopefully should let the loop keep going if an entry is blank
    if sample_number != array_all[10]:
        sample_number = array_all[10]                    # sets the sample number (UD3, Column 10) counter to the first encountered sample
        file_out_Hae = open("Hae" + sample_number + ".txt", 'w')
        file_out_Alu = open("Alu" + sample_number + ".txt", 'w')
        file_out_Liar = open("Liar" + sample_number + ".txt", 'w')
        if array_all[11] != '' and array_all[13] != '' and array_all[14] != '':
                                                        # only selects non-blanks in Dye/Sample and Size entries
            if array_all[9] == "Alu":                     # sorts whether array is printed to Alu, Hae, or Liar
                print >>file_out_Alu, '\t'.join(array)
            elif array_all[9] == "Hae":
                print >>file_out_Hae, '\t'.join(array)
            elif array_all[9] == "Liar":
                print >>file_out_Liar, '\t'.join(array)
            else:                                       # if something other than Alu, Liar, or Hae
                print "line ", line_counter, " has something other than Alu, Hae, or Liar\n"
    else:                                               # moves on if still on same sample as previous line
        if array_all[11] != '' and array_all[13] != '' and array_all[14] != '':
                                                        # only selects non-blank entries in "Dye/Sample Peak"
            if array_all[9] == "Alu":                     # sorts whether array is printed to Alu, Liar or Hae
                print >>file_out_Alu, '\t'.join(array)
                                                        # file_out is technically undefined, but should be open already
            elif array_all[9] == "Hae":
                print >>file_out_Hae, '\t'.join(array)
            elif array_all[9] == "Liar":
                print >>file_out_Liar, '\t'.join(array)
            else:                                       # break here stops run if there's no Alu, Liar or Hae
                print "line ", line_counter, " has something other than Alu, Liar, or Hae (in field UD1?)\n"

file_in.close()
file_out_Hae.close()                                      # closes the last set of open files. Note that row one will often show up as an alert (not containing alu, hae, or liar, and a file may created for that row that needs to be deleted later.
file_out_Alu.close()
file_out_Liar.close()

print "Run complete!\n"
