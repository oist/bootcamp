import random

def format_fasta(title, sequence):
    """
    This formats a fasta sequence
    Input: 
      title - String - Title of the sequence
      sequence - String - Actual sequence
    Output: 
      String - Fully formatted fasta sequence
    """
    fasta_width = 70 # Number of characters in one line

    n_lines = 1 + len(sequence) // fasta_width # Number of lines

    lines = [ sequence[i*fasta_width: (i+1)*fasta_width] for i in range(n_lines)]
    lines = "\n".join(lines)
    
    formatted = f"> {title}\n{lines}\n\n"
    return formatted 

bases = "actg" # Bases for our randon protein

# Writing random sequences in a file
with open("random_sequences.fa", "w") as f:
    for length in range(1, 25): # Sequences of different lengths
        for run in range(10): # Trying several times
            
            title = f"length_{length} run_{run}"
            sequence = "".join(random.choices(bases, k=length))

            f.write(format_fasta(title, sequence))
