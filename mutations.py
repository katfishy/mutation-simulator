import random

Nucleotides = ['A', 'T', 'G', 'C']

def randinsert(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide insertion mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand:]
    return new_seq


def randdel(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide deletion mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + seq[rand + 1:]
    return new_seq


def randsub(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide substitution mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand + 1:]
    return new_seq


def insertion(seq: str, position: int, nucleotide: str) -> str:
    """Return the DNA seq with a single insertion mutation of a specific nucleotide
    at a specific position.
    """
    pos = position - 1
    new_seq = seq[:pos] + nucleotide + seq[pos:]
    return new_seq


def deletion(seq: str, position: int) -> str:
    """Return the DNA seq with a single deletion mutation at a specific position."""
    pos = position - 1
    new_seq = seq[:pos] + seq[pos + 1:]
    return new_seq


def substitution(seq: str, position: int, nucleotide: str) -> str:
    """Return the DNA seq with a single substitution mutation of a specific nucleotide 
    at a specific position.
    """
    pos = position - 1
    new_seq = seq[:pos] + nucleotide + seq[pos + 1:]
    return new_seq


def seqtoinsert(seq1: str, seq2: str) -> bool:
    """Return True if seq2 has a single nucleotide insertion mutation of seq1.
    
    >>> seqtoinsert('AATGC', 'AATGTC')
    True
    >>> seqtoinsert('AACC', 'AACCT')
    True
    """

    i = 0
    while i < len(seq1) and seq1[i] == seq2[i]:
        i += 1

    # Check for any insertion that is not at the end of seq1.
    if i != len(seq1):
        result = 0
        for pos in range(i, len(seq1)):
            if seq1[pos] == seq2[pos + 1]:
                result += 1
        return result == len(seq2) - (i + 1) and len(seq2) == len(seq1) + 1
    
    # Check for insertion that is at the end of seq1.
    else:
        return i == len(seq1) and len(seq2) == len(seq1) + 1


def seqtodel(seq1: str, seq2: str) -> bool:
    """Return True if seq2 has a single nucleotide deletion mutation of seq1."""
    return len(seq2) == len(seq1) - 1


def seqtosub(seq1: str, seq2: str) -> bool:
    """Return True if seq2 has a single mucleotide substitution mutation of seq1."""
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
