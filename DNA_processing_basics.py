# Get length of a DNA sequence

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)



# Check if first sequence is longer than the second

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


   
# Count the appearance of a specific nucleotide in a given sequence

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for sequence in dna:
        if sequence == nucleotide:
            count = count + 1
    return count



# Check if second sequence is a part of the first sequence

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1



# Check if the given sequence is a valid sequence. Assumes only presence of 'A', 'T', 'C' and 'G' and not small case characters for the nucleotides

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence contains 'A', 'T', 'C', and 'G'.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCDB')
    False
    >>> is_valid_sequence('aTcgGC')
    False
    """
    for sequence in dna:
        valid = True
        if sequence not in 'ATCG':
            valid = False
            break
            
    return valid
        


# Insert second sequence into the first at a defined index position

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return DNA sequence obtained by inserting dna2 sequence in dna1 sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('ATCG', 'GCGG', 3)
    ATCGCGGG
    >>> insert_sequence('TAGC', 'ATCG', 0)
    ATCGTAGC
    """
    return dna1[:index] + dna2 + dna1[index:]



# Get complement of a given nucleotide

def get_complement(nucleotide):
    """ (str) -> str

    Return complement of given nucleotide.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'



# Get complementary sequence of a given sequence

def get_complementary_sequence(dna):
    """ (str) -> str

    Return complement of given dna sequence.

    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('TGC')
    ACG
    >>> get_complementary_sequence('CGTAGCGA')
    GCATCGCT
    """
    complemetary_sequence = ''
    
    for nucleotide in dna:     
        
        if nucleotide == 'A':
            complemetary_sequence = complemetary_sequence + 'T'
        if nucleotide == 'T':
            complemetary_sequence = complemetary_sequence + 'A'
        if nucleotide == 'C':
            complemetary_sequence = complemetary_sequence + 'G'
        if nucleotide == 'G':
            complemetary_sequence = complemetary_sequence + 'C'
            
    return complemetary_sequence



# Get reverse complement of a given sequence

def get_reverse_complementary_sequence(dna):
    """ (str) -> str

    Return reverse complement of given dna sequence.

    >>> get_reverse_complementary_sequence('ATTTCAGCTG')
    CAGCTGAAAT
    >>> get_reverse_complementary_sequence('CGTAGCGA')
    TCGCTACG
    """
    complemetary_sequence = ''
    
    for nucleotide in dna:     
        
        if nucleotide == 'A':
            complemetary_sequence = complemetary_sequence + 'T'
        if nucleotide == 'T':
            complemetary_sequence = complemetary_sequence + 'A'
        if nucleotide == 'C':
            complemetary_sequence = complemetary_sequence + 'G'
        if nucleotide == 'G':
            complemetary_sequence = complemetary_sequence + 'C'
            
    return complemetary_sequence[::-1]



# Get GC content of a given sequence
def GC_content(dna):
    """ (str) -> float

    Return GC content from a given dna sequence.

    >>> GC_content('AT')
    0
    >>> GC_content('TGC')
    0.6667
    >>> GC_content('CGTAGCGACGTAGCGATGC')
    0.6315
    """
    GC_count = 0
    for sequence in dna:
        if sequence in 'GC':
            GC_count = GC_count + 1
        
            
    return GC_count / len(dna)

