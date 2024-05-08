template = 'crab_PREMIXRAW_StopToMuB_M_XXX_YYYmm.py'

mass_points = [500]
ctau_points = [1,10,100,1000,10000,100000]

inputdatasets = {'500_100000': '/StopToMuB_M_500_100000mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-4788604166596253c1aa09f33ee6493a/USER',
                 '500_10000': '/StopToMuB_M_500_10000mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-6dbeb08e115b3fc4389dd814af612b70/USER',
                 '500_1000': '/StopToMuB_M_500_1000mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-e35e8810903e828bb9aec41239033696/USER',
                 '500_100': '/StopToMuB_M_500_100mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-d0d102b0a94b5299ed17272f1e60e3a5/USER',
                 '500_10': '/StopToMuB_M_500_10mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-7a148e75414ff8f3b36f5658ed1983fc/USER',
                 '500_1': '/StopToMuB_M_500_1mm_13p6TeV_2022MC_CMSSW_12_4_20_v0/rlopezru-GENSIM-b4390a366bdb9a745205550928109d9b/USER',
                 '1000_1000000': '/StopToMuB_M_1000_1000000mm_13p6TeV_2022MC/rlopezru-GenSim-03e045847b4e569bac756f9b1a62661e/USER',
                 '1000_100000': '/StopToMuB_M_1000_100000mm_13p6TeV_2022MC/rlopezru-GenSim-55303ffbcd2b28618a30191c7098dd0d/USER',
                 '1000_10000': '/StopToMuB_M_1000_10000mm_13p6TeV_2022MC/rlopezru-GenSim-3a1e5fb1e0e46fc8f2658a616d915873/USER',
                 '1000_1000': '/StopToMuB_M_1000_1000mm_13p6TeV_2022MC/rlopezru-GenSim-1537a1d3b68ced11113912ec74c5211c/USER',
                 '1000_100': '/StopToMuB_M_1000_100mm_13p6TeV_2022MC/rlopezru-GenSim-8e497901ea55fb97eec05827b80a04be/USER',
                 '1000_10': '/StopToMuB_M_1000_10mm_13p6TeV_2022MC/rlopezru-GenSim-8d4973a8a46817e6227e5ddc1543ab8b/USER',
                 '1000_1': '/StopToMuB_M_1000_1mm_13p6TeV_2022MC/rlopezru-GenSim-a17028e9f82f4a74b6877712146b34c5/USER',
                 '1250_1000000': '/StopToMuB_M_1250_1000000mm_13p6TeV_2022MC/rlopezru-GenSim-0d4d6b305198134a520fefe5c4a1745d/USER',
                 '1250_100000': '/StopToMuB_M_1250_100000mm_13p6TeV_2022MC/rlopezru-GenSim-64e244d1f1e5ca656f03a5953b31adad/USER',
                 '1250_10000': '/StopToMuB_M_1250_10000mm_13p6TeV_2022MC/rlopezru-GenSim-56e58d42d2f5d7fbf6c49fd4d59fa0d1/USER',
                 '1250_1000': '/StopToMuB_M_1250_1000mm_13p6TeV_2022MC/rlopezru-GenSim-2a40ff2472d122461b19b1d6159a02df/USER',
                 '1250_100': '/StopToMuB_M_1250_100mm_13p6TeV_2022MC/rlopezru-GenSim-71701052fc673adaa148715b4c4dfb47/USER',
                 '1250_10': '/StopToMuB_M_1250_10mm_13p6TeV_2022MC/rlopezru-GenSim-f56a5cc01e47e70ef8e93a3aa37fda32/USER',
                 '1250_1': '/StopToMuB_M_1250_1mm_13p6TeV_2022MC/rlopezru-GenSim-8282e5fbbfa881aa57eecdffd99aa4e7/USER',
                 '1500_1000000': '/StopToMuB_M_1500_1000000mm_13p6TeV_2022MC/rlopezru-GenSim-e6a1f74a6ac1aa42a27a11db33d1d38e/USER',
                 '1500_100000': '/StopToMuB_M_1500_100000mm_13p6TeV_2022MC/rlopezru-GenSim-8e1026b39616ace4416c1c83e25df3c4/USER',
                 '1500_10000': '/StopToMuB_M_1500_10000mm_13p6TeV_2022MC/rlopezru-GenSim-da69b124196d88ee688dcb2b3482c4fc/USER',
                 '1500_1000': '/StopToMuB_M_1500_1000mm_13p6TeV_2022MC/rlopezru-GenSim-dd90bdd859a950b22b203e935cd2a563/USER',
                 '1500_100': '/StopToMuB_M_1500_100mm_13p6TeV_2022MC/rlopezru-GenSim-4c24d2275e4e360146e69723b71069d9/USER',
                 '1500_10': '/StopToMuB_M_1500_10mm_13p6TeV_2022MC/rlopezru-GenSim-f9a0c6907292c4ca5330c5fa873a1531/USER',
                 '1500_1': '/StopToMuB_M_1500_1mm_13p6TeV_2022MC/rlopezru-GenSim-5b2cc7373d5cae2c7314cf7c1631b199/USER'}

with open(template, 'r') as f_in:
    text = f_in.read()

for M in mass_points:
    for ct in ctau_points:
        textout = text.replace('###MASS###', str(M))
        textout = textout.replace('###CTAU###', str(ct))
        textout = textout.replace('###INPUTDATASET###', inputdatasets[f'{M}_{ct}'])
        with open(f'crab/crab_PREMIXRAW_StopToMuB_M_{M}_ctau_{ct}mm.py', 'w') as f_out:
            f_out.write(textout)
