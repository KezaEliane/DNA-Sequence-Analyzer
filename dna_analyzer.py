# DNA Sequence Analyzer
def count_nucleotides(dna_sequence):
    """Counts occurrences of each nucleotide in a DNA sequence."""
    nucleotides = {"A": 0, "T": 0, "C": 0, "G": 0}
    
    for nucleotide in dna_sequence:
        if nucleotide in nucleotides:
            nucleotides[nucleotide] += 1
    
    return nucleotides

# Example DNA sequence
dna_sequence = "ATGCTTCAGAAAGGTCTTACG"
counts = count_nucleotides(dna_sequence)

# Display results
print("Nucleotide Counts:", counts)
