template = 'crab_GEN_StopToMuB_M_XXX_YYYmm.py'

mass_points = [100, 500, 1000, 1250, 1500]
ctau_points = [1,10,100,1000,10000,100000,1000000]

with open(template, 'r') as f_in:
    text = f_in.read()

for M in mass_points:
    for ct in ctau_points:
        textout = text.replace('###MASS###', str(M))
        textout = textout.replace('###CTAU###', str(ct))
        with open(f'crab/crab_GEN_StopToMuB_M_{M}_ctau_{ct}mm.py', 'w') as f_out:
            f_out.write(textout)
