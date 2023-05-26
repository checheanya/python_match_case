class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.type = 'DNA'
        
    def transcribe(self):
        transcribed_sequence = self.sequence.replace("T", "U")
        return RNASequence(transcribed_sequence)

    def complement(self):
        complement_table = {
            "A": "T", "T": "A", "C": "G", "G": "C"
        }
        complement_sequence = ""
        for nucleotide in self.sequence:
            complement = complement_table.get(nucleotide, "-")
            complement_sequence += complement
        return DNASequence(complement_sequence)

    def reverse_complement(self):
        reverse_complement_sequence = self.complement().sequence[::-1]
        return DNASequence(reverse_complement_sequence)

class RNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.type = 'RNA'

    def complement(self):
        complement_table = {
            "A": "U", "U": "A", "C": "G", "G": "C"
        }
        complement_sequence = ""
        for nucleotide in self.sequence:
            complement = complement_table.get(nucleotide, "-")
            complement_sequence += complement
        return RNASequence(complement_sequence)

    def reverse_complement(self):
        reverse_complement_sequence = self.complement().sequence[::-1]
        return RNASequence(reverse_complement_sequence)

class ProteinSequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.type = 'Protein'

    def __str__(self):
        return self.sequence

def process_sequence_operation(seq, operation):
  try:
    match (seq.type, operation):
        case ('DNA', 'transcribe'):
            transcr = seq.transcribe()
            print("Transcribed RNA Sequence:", transcr.sequence)
        case ('DNA', 'complement'):
            compl = seq.complement()
            print("Complement Sequence:", compl.sequence)
        case ('DNA', 'reverse_complement'):
            rev_compl = seq.reverse_complement()
            print("Reverse Complement Sequence:", rev_compl.sequence)
        case ('RNA', 'complement'):
            compl =  seq.complement()
            print("Complement Sequence:", compl.sequence)
        case ('RNA', 'reverse_complement'):
            rev_compl = seq.reverse_complement()
            print("Reverse Complement Sequence:", rev_compl.sequence)
        case (_, _):
            print("Error: Invalid operation for the given sequence type.")
  except AttributeError:
    print("Error: Invalid sequence type.")

# Example usage
dna_sequence = DNASequence("ATCG")
rna_sequence = RNASequence("AUCG")
protein_sequence = ProteinSequence("MRS*-")
invalid_sequence = "im_invalid_seq"

process_sequence_operation(dna_sequence, 'transcribe')
process_sequence_operation(dna_sequence, 'complement')
process_sequence_operation(dna_sequence, 'reverse_complement')
process_sequence_operation(rna_sequence, 'complement')
process_sequence_operation(rna_sequence, 'reverse_complement')
process_sequence_operation(protein_sequence, 'transcribe')
process_sequence_operation(dna_sequence, 'smth')
process_sequence_operation(invalid_sequence, 'complement')
