def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


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


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it
    contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ASTCG')
    False
    >>> is_valid_sequence('atcggc')
    False

    """
    valid = True
    nucleotides = "ATCG"
    for char in dna:
        if char in nucleotides:
            valid = True
        else:
            valid = False
            return valid
    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    The first two parameters are DNA sequences and the third
    parameter is an index. Return the DNA sequence obtained
    by inserting the second DNA sequence into the first DNA
    sequence at the given index.

    Precondition: index must be valid.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'

    """
    return dna1[:index]+dna2+dna1[index:]


def get_complement(nucleotide):
    """
    (str) -> str

    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    >>> get_complement('W')
    'Not Valid'
    
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'Not Valid'


def get_complementary_sequence(dna1):
    """
    (str) -> str

    The parameter is a DNA sequence. Return the DNA sequence
    that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('ATGC')
    'TACG'
    >>> get_complementary_sequence('ATXYZ')
    'Invalid Sequence'
    """

    if is_valid_sequence(dna1):
        dna2 = ''
        for char in dna1:
            dna2 = dna2 + get_complement(char)
        return dna2
    else:
        return 'Invalid Sequence'



    

    
