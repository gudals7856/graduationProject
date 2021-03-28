# run_muscle.py

from Bio.Align.Applications import MuscleCommandline

muscle_exe = "C:\Users\조형민\graduationProject\analysis"

cmd_line = MuscleCommandline(muscle_exe, \
                             input="covid.all.fasta", \
                             out="covid.all.aln", \
                            clw=" ")

print(cmd_line)
stdout, stderr = cmd_line()

