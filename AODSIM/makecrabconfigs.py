template = 'crab_AODSIM_StopToMuB_M_XXX_YYYmm.py'

mass_points = [100,500,1000,1500]
ctau_points = [1,10,100,1000,10000,100000]

inputdatasets = {'100_1':       '/StopToMuB_M_100_1mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '100_10':      '/StopToMuB_M_100_10mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '100_100':     '/StopToMuB_M_100_100mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '100_1000':    '/StopToMuB_M_100_1000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '100_10000':   '/StopToMuB_M_100_10000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '100_100000':  '/StopToMuB_M_100_100000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_100000':  '/StopToMuB_M_500_100000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_10000':   '/StopToMuB_M_500_10000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_1000':    '/StopToMuB_M_500_1000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_100':     '/StopToMuB_M_500_100mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_10':      '/StopToMuB_M_500_10mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '500_1':       '/StopToMuB_M_500_1mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_1000000':'/StopToMuB_M_1000_1000000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_100000': '/StopToMuB_M_1000_100000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_10000':  '/StopToMuB_M_1000_10000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_1000':   '/StopToMuB_M_1000_1000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_100':    '/StopToMuB_M_1000_100mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_10':     '/StopToMuB_M_1000_10mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1000_1':      '/StopToMuB_M_1000_1mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_1000000':'/StopToMuB_M_1500_1000000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_100000': '/StopToMuB_M_1500_100000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_10000':  '/StopToMuB_M_1500_10000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_1000':   '/StopToMuB_M_1500_1000mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_100':    '/StopToMuB_M_1500_100mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_10':     '/StopToMuB_M_1500_10mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                 '1500_1':      '/StopToMuB_M_1500_1mm_13p6TeV_2022MC/rlopezru-DigiRawHlt-87e245638d0e8549d13398f07ce44cec/USER',
                }

with open(template, 'r') as f_in:
    text = f_in.read()

for M in mass_points:
    for ct in ctau_points:
        textout = text.replace('###MASS###', str(M))
        textout = textout.replace('###CTAU###', str(ct))
        textout = textout.replace('###INPUTDATASET###', inputdatasets[f'{M}_{ct}'])
        with open(f'crab/crab_AODSIM_StopToMuB_M_{M}_ctau_{ct}mm.py', 'w') as f_out:
            f_out.write(textout)
