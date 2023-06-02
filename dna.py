# The main function effectively runs the entire code, calling the fuctions in the correct order.
# It starts by calling the intro function, then it establishing the input file, and output file names.
# It proceeds to then open the input file, and store the contents of the input file into a variable.
# A for loop is then used to go through the contents of the input file, and stores the proper data into a nucleotide sequence...
# into a variable.
# The count function is then called, along with the mass function.
# Followed by the codons_list function, then the output function.
# It finishes by writing all of the outputs from the variaous functions into an output file that was named when
# asking the user for the output file name.
def main():
    intro_message()
    in_file = input("Input file name? ")
    out_file = input("Output file name? ")
    with open(in_file) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 2):
        name = lines[i]
        nuc = lines[i + 1]
        nuc = nuc.upper()
        count_l, junk_count = get_count(nuc)
        mass_l, total_m = get_mass(count_l, junk_count)
        codon_l = codons_list(nuc)
        is_pro = is_protein(codon_l, mass_l)
        output_l = output(name, nuc, count_l, mass_l, total_m, codon_l, is_pro)
        with open(out_file, 'a') as o:
            for line in output_l:
                o.write(line)
        

# This function prints the intro statement that is placed at the beginning of the file.
def intro_message():
    print("This program reports information about DNA\nnucleotide sequences that may encode proteins.")
    


# This function effectively determines the amount of "A", "C", "G", and "T", values in the nucleotide
# sequence of the region name and returns a list of those counts, as well as amount of "-",
# or "junk".
def get_count(chain):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    junk_count = 0
    for nuc in chain:
        if nuc == "A":
            a_count += 1
        elif nuc == "C":
            c_count += 1
        elif nuc == "G":
            g_count += 1
        elif nuc == "T":
            t_count += 1
        elif nuc == "-":
            junk_count += 1
    count_list = [a_count, c_count, g_count, t_count]
    return count_list, junk_count

# This function compares the mass of each individual nucleotides and calculates the
# mass percentage of each ACGT nucleotide value and returns a list of those percentages.
# It also returns the total mass of all the nucleotides combined.
def get_mass(count_list, junk_count):
    a_count = count_list[0]
    c_count = count_list[1]
    g_count = count_list[2]
    t_count = count_list[3]
    amass_t = a_count * 135.128
    cmass_t = c_count * 111.103
    gmass_t = g_count * 151.128
    tmass_t = t_count * 125.107
    junk_t = junk_count * 100
    total_mass = round(amass_t + cmass_t + gmass_t + tmass_t + junk_t, 1)
    a_pct = round((amass_t / total_mass) * 100, 1)
    c_pct = round((cmass_t / total_mass) * 100, 1)
    g_pct = round((gmass_t / total_mass) * 100, 1)
    t_pct = round((tmass_t / total_mass) * 100, 1)
    mass_list = [a_pct, c_pct, g_pct, t_pct]
    return mass_list, total_mass

# This function splits the nucleotide sequence into codons, then puts each codon as an element
# into a list. That list is then returned.
def codons_list(nucleotide):
    codon_list = []
    nucleotide = nucleotide.split("-")
    nucleotide = "".join(nucleotide)
    for i in range(0, len(nucleotide) - 2, 3):
        var = nucleotide[i] + nucleotide[i + 1] + nucleotide[i + 2]
        codon_list.insert(i, var)
    return codon_list

# This function takes the codon list that was returned and proceeds to determine if it meets all of the requirements
# of being a protein. If it is determined to be a protein, the is_protein varaible is stored as YES, if not, is_protein
# is stored as NO... is_protein is then returned.
def is_protein(codon_list, mass_list):
    is_protein = ""
    end_codons = ["TAA", "TAG", "TGA"]
    c_pct = mass_list[1]
    g_pct = mass_list[2]
    if codon_list[0] == "ATG":
        if codon_list[len(codon_list) - 1] in end_codons:
            if len(codon_list) >= 5:
                if c_pct + g_pct > 30.0:
                    is_protein = "YES"
                else:
                    is_protein = "NO"
            else:
                    is_protein = "NO"
        else:
                    is_protein = "NO"
    else:
        is_protein = "NO"
    return is_protein
                
        
    
        
# This function effectively stores all of the outputted information into a list so that the main function can write
# all of these values into the output file. Once it does this it returns the output list.
def output(name, nuc, count_list, mass_list, total_mass, codon_list, protein):
    output_l = []
    output_l.append(f"Region Name: {name}")
    output_l.append(f"Nucleotides: {nuc}") 
    output_l.append(f"Nuc. Counts: {count_list}")
    output_l.append("\n")
    output_l.append(f"Total Mass%: {mass_list} of {total_mass}")
    output_l.append("\n")
    output_l.append(f"Codons List: {codon_list}")
    output_l.append("\n")
    output_l.append(f"Is Protein?: {protein}")
    output_l.append("\n")
    output_l.append("\n")
    return output_l
    
    
main()
