COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2A3bbbar = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     5.00000000E+00   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.54000000E+03   # At
        12     1.54000000E+03   # Ab
        13     1.54000000E+03   # Atau
        23     2.00000000E+02   # MUE
        25     5.00000000E+00   # TB
        26     6.00000000E+02   # MA0
        27     6.05362568E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.96147383E+02   # MSf(1,1,1)
   1000011     5.02124333E+02   # MSf(1,2,1)
   2000011     5.01706018E+02   # MSf(2,2,1)
   1000002     1.49910023E+03   # MSf(1,3,1)
   2000002     1.49962019E+03   # MSf(2,3,1)
   1000001     1.50108899E+03   # MSf(1,4,1)
   2000001     1.50018986E+03   # MSf(2,4,1)
   1000014     4.96147383E+02   # MSf(1,1,2)
   1000013     5.02149324E+02   # MSf(1,2,2)
   2000013     5.01681028E+02   # MSf(2,2,2)
   1000004     1.49910022E+03   # MSf(1,3,2)
   2000004     1.49962131E+03   # MSf(2,3,2)
   1000003     1.50109009E+03   # MSf(1,4,2)
   2000003     1.50018877E+03   # MSf(2,4,2)
   1000016     9.98079268E+02   # MSf(1,1,3)
   1000015     1.00046976E+03   # MSf(1,2,3)
   2000015     1.00145112E+03   # MSf(2,2,3)
   1000006     8.76514793E+02   # MSf(1,3,3)
   2000006     1.13484824E+03   # MSf(2,3,3)
   1000005     9.99672858E+02   # MSf(1,4,3)
   2000005     1.00226018E+03   # MSf(2,4,3)
        25     1.20053351E+02   # Mh0
        35     6.01278963E+02   # MHH
        36     6.00000000E+02   # MA0
        37     6.05498986E+02   # MHp
   1000022     8.32246583E+01   # MNeu(1)
   1000023     1.46162492E+02   # MNeu(2)
   1000025    -2.07032524E+02   # MNeu(3)
   1000035     2.73117025E+02   # MNeu(4)
   1000024     1.38016688E+02   # MCha(1)
   1000037     2.71807047E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     8.78442979E-01   # Delta Mh0
        35     2.59529186E-02   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     3.66877468E-02   # Delta MHp
BLOCK NMIX
     1   1     9.02741035E-01   # ZNeu(1,1)
     1   2    -1.76906456E-01   # ZNeu(1,2)
     1   3     3.40847919E-01   # ZNeu(1,3)
     1   4    -1.93869609E-01   # ZNeu(1,4)
     2   1    -3.94247799E-01   # ZNeu(2,1)
     2   2    -6.93610991E-01   # ZNeu(2,2)
     2   3     4.67997695E-01   # ZNeu(2,3)
     2   4    -3.80066603E-01   # ZNeu(2,4)
     3   1     8.11445475E-02   # ZNeu(3,1)
     3   2    -1.12684390E-01   # ZNeu(3,2)
     3   3    -6.81879284E-01   # ZNeu(3,3)
     3   4    -7.18163235E-01   # ZNeu(3,4)
     4   1    -1.51798743E-01   # ZNeu(4,1)
     4   2     6.89137234E-01   # ZNeu(4,2)
     4   3     4.47036346E-01   # ZNeu(4,3)
     4   4    -5.49732225E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.25444296E-01   # UCha(1,1)
     1   2     7.80268821E-01   # UCha(1,2)
     2   1     7.80268821E-01   # UCha(2,1)
     2   2     6.25444296E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.80268821E-01   # VCha(1,1)
     1   2     6.25444296E-01   # VCha(1,2)
     2   1     6.25444296E-01   # VCha(2,1)
     2   2     7.80268821E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1    -6.27000005E-01   # USf(1,1)
     1   2     7.79019251E-01   # USf(1,2)
     2   1     7.79019251E-01   # USf(2,1)
     2   2     6.27000005E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08166916E-01   # USf(1,1)
     1   2    -7.06045055E-01   # USf(1,2)
     2   1     7.06045055E-01   # USf(2,1)
     2   2     7.08166916E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1    -4.89397966E-01   # USf(1,1)
     1   2     8.72060566E-01   # USf(1,2)
     2   1     8.72060566E-01   # USf(2,1)
     2   2     4.89397966E-01   # USf(2,2)
BLOCK ALPHA
              -2.10429880E-01   # Alpha
BLOCK DALPHA
               2.65900939E-04   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     5.00000000E+00   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.54000000E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.54000000E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.54000000E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     1.49657094E-05   # Yf(1,1)
     2   2     3.09443379E-03   # Yf(2,2)
     3   3     5.20441717E-02   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.75722993E-05   # Yf(1,1)
     2   2     7.53265896E-03   # Yf(2,2)
     3   3     1.01450741E+00   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     1.74829084E-04   # Yf(1,1)
     2   2     2.76809607E-03   # Yf(2,2)
     3   3     1.19892640E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     8.01480244E+01   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.56234141E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.84634666E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99999260E-01   # UASf(1,1)
     1   4    -1.21690415E-03   # UASf(1,4)
     2   2     9.72951221E-01   # UASf(2,2)
     2   5    -2.31010653E-01   # UASf(2,5)
     3   3    -6.27000005E-01   # UASf(3,3)
     3   6     7.79019251E-01   # UASf(3,6)
     4   1     1.21690415E-03   # UASf(4,1)
     4   4     9.99999260E-01   # UASf(4,4)
     5   2     2.31010653E-01   # UASf(5,2)
     5   5     9.72951221E-01   # UASf(5,5)
     6   3     7.79019251E-01   # UASf(6,3)
     6   6     6.27000005E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     9.99999997E-01   # UASf(1,1)
     1   4     7.69624283E-05   # UASf(1,4)
     2   2     9.99457413E-01   # UASf(2,2)
     2   5     3.29375163E-02   # UASf(2,5)
     3   3     7.08166916E-01   # UASf(3,3)
     3   6    -7.06045055E-01   # UASf(3,6)
     4   1    -7.69624283E-05   # UASf(4,1)
     4   4     9.99999997E-01   # UASf(4,4)
     5   2    -3.29375163E-02   # UASf(5,2)
     5   5     9.99457413E-01   # UASf(5,5)
     6   3     7.06045055E-01   # UASf(6,3)
     6   6     7.08166916E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99997553E-01   # UASf(1,1)
     1   4    -2.21213987E-03   # UASf(1,4)
     2   2     9.99388672E-01   # UASf(2,2)
     2   5    -3.49611623E-02   # UASf(2,5)
     3   3    -4.89397966E-01   # UASf(3,3)
     3   6     8.72060566E-01   # UASf(3,6)
     4   1     2.21213987E-03   # UASf(4,1)
     4   4     9.99997553E-01   # UASf(4,4)
     5   2     3.49611623E-02   # UASf(5,2)
     5   5     9.99388672E-01   # UASf(5,5)
     6   3     8.72060566E-01   # UASf(6,3)
     6   6     4.89397966E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99988959E-01   # UH(1,1)
     1   2     4.69912525E-03   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.69912525E-03   # UH(2,1)
     2   2     9.99988959E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     3.59906436E-03   # Gamma(h0)
     2.28024406E-03   2        22        22   # BR(h0 -> photon photon)
     1.05917882E-03   2        22        23   # BR(h0 -> photon Z)
     1.55935294E-02   2        23        23   # BR(h0 -> Z Z)
     1.42284897E-01   2       -24        24   # BR(h0 -> W W)
     6.92225766E-02   2        21        21   # BR(h0 -> gluon gluon)
     6.00777279E-09   2       -11        11   # BR(h0 -> Electron electron)
     2.67233169E-04   2       -13        13   # BR(h0 -> Muon muon)
     7.69668075E-02   2       -15        15   # BR(h0 -> Tau tau)
     2.15484148E-07   2        -2         2   # BR(h0 -> Up up)
     2.98439348E-02   2        -4         4   # BR(h0 -> Charm charm)
     9.95298633E-07   2        -1         1   # BR(h0 -> Down down)
     2.49954343E-04   2        -3         3   # BR(h0 -> Strange strange)
     6.62230428E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     6.28706881E+00   # Gamma(HH)
     3.55066326E-06   2        22        22   # BR(HH -> photon photon)
     5.21764635E-06   2        22        23   # BR(HH -> photon Z)
     9.25444149E-04   2        23        23   # BR(HH -> Z Z)
     1.85497105E-03   2       -24        24   # BR(HH -> W W)
     2.38363997E-04   2        21        21   # BR(HH -> gluon gluon)
     3.68971994E-10   2       -11        11   # BR(HH -> Electron electron)
     1.64202926E-05   2       -13        13   # BR(HH -> Muon muon)
     4.70563184E-03   2       -15        15   # BR(HH -> Tau tau)
     2.00235648E-11   2        -2         2   # BR(HH -> Up up)
     2.77130080E-06   2        -4         4   # BR(HH -> Charm charm)
     1.25295001E-01   2        -6         6   # BR(HH -> Top top)
     4.64264064E-08   2        -1         1   # BR(HH -> Down down)
     1.16597021E-05   2        -3         3   # BR(HH -> Strange strange)
     3.02064277E-02   2        -5         5   # BR(HH -> Bottom bottom)
     1.44985242E-01   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)
     1.78250750E-01   2  -1000037   1000024   # BR(HH -> Chargino2 chargino1)
     1.78250750E-01   2  -1000024   1000037   # BR(HH -> Chargino1 chargino2)
     3.98825328E-03   2  -1000037   1000037   # BR(HH -> Chargino2 chargino2)
     2.59749127E-02   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
     4.70548514E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)
     7.82906643E-02   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)
     3.19917318E-05   2   1000022   1000035   # BR(HH -> neutralino1 neutralino4)
     1.74299739E-02   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)
     3.50765517E-02   2   1000023   1000025   # BR(HH -> neutralino2 neutralino3)
     2.60286000E-03   2   1000023   1000035   # BR(HH -> neutralino2 neutralino4)
     4.85811470E-03   2   1000025   1000025   # BR(HH -> neutralino3 neutralino3)
     1.06961923E-01   2   1000025   1000035   # BR(HH -> neutralino3 neutralino4)
     3.52903628E-03   2   1000035   1000035   # BR(HH -> neutralino4 neutralino4)
     5.96327199E-13   2        23        36   # BR(HH -> Z A0)
     9.44862080E-03   2        25        25   # BR(HH -> h0 h0)
DECAY        36     6.25373024E+00   # Gamma(A0)
    -5.82344669E-06   2        22        22   # BR(A0 -> photon photon)
    -1.11712447E-05   2        22        23   # BR(A0 -> photon Z)
    -3.63511249E-04   2        21        21   # BR(A0 -> gluon gluon)
    -3.67967066E-10   2       -11        11   # BR(A0 -> Electron electron)
     1.63755594E-05   2       -13        13   # BR(A0 -> Muon muon)
    -4.69251342E-03   2       -15        15   # BR(A0 -> Tau tau)
    -1.76216648E-11   2        -2         2   # BR(A0 -> Up up)
    -2.43915396E-06   2        -4         4   # BR(A0 -> Charm charm)
    -1.65762129E-01   2        -6         6   # BR(A0 -> Top top)
    -4.63106653E-08   2        -1         1   # BR(A0 -> Down down)
    -1.16306414E-05   2        -3         3   # BR(A0 -> Strange strange)
    -3.01465120E-02   2        -5         5   # BR(A0 -> Bottom bottom)
    -3.16819888E-01   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)
    -4.37612516E-02   2  -1000037   1000024   # BR(A0 -> Chargino2 chargino1)
    -4.37612516E-02   2  -1000024   1000037   # BR(A0 -> Chargino1 chargino2)
    -8.41751663E-02   2  -1000037   1000037   # BR(A0 -> Chargino2 chargino2)
    -4.55946414E-02   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
    -1.01009708E-01   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)
    -2.17214223E-02   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)
    -1.46683527E-03   2   1000022   1000035   # BR(A0 -> neutralino1 neutralino4)
    -4.55039531E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)
    -6.07200713E-03   2   1000023   1000025   # BR(A0 -> neutralino2 neutralino3)
    -5.70060022E-03   2   1000023   1000035   # BR(A0 -> neutralino2 neutralino4)
    -3.86244282E-03   2   1000025   1000025   # BR(A0 -> neutralino3 neutralino3)
    -2.03817931E-02   2   1000025   1000035   # BR(A0 -> neutralino3 neutralino4)
    -5.75835187E-02   2   1000035   1000035   # BR(A0 -> neutralino4 neutralino4)
    -1.57336881E-03   2        23        25   # BR(A0 -> Z h0)
    -4.08258193E-36   2        25        25   # BR(A0 -> h0 h0)
DECAY        37     6.27947463E+00   # Gamma(Hp)
     3.98970076E-10   2       -11        12   # BR(Hp -> Electron nu_e)
     1.70572129E-05   2       -13        14   # BR(Hp -> Muon nu_mu)
     4.82483458E-03   2       -15        16   # BR(Hp -> Tau nu_tau)
     4.42772337E-08   2        -1         2   # BR(Hp -> Down up)
     5.07650844E-07   2        -3         2   # BR(Hp -> Strange up)
     3.16587760E-07   2        -5         2   # BR(Hp -> Bottom up)
     1.13297397E-07   2        -1         4   # BR(Hp -> Down charm)
     1.35073364E-05   2        -3         4   # BR(Hp -> Strange charm)
     4.43368973E-05   2        -5         4   # BR(Hp -> Bottom charm)
     1.03217725E-05   2        -1         6   # BR(Hp -> Down top)
     2.25062100E-04   2        -3         6   # BR(Hp -> Strange top)
     1.87451699E-01   2        -5         6   # BR(Hp -> Bottom top)
     9.96420563E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     7.62906862E-03   2   1000022   1000037   # BR(Hp -> neutralino1 chargino2)
     2.63110633E-02   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)
     2.67999524E-01   2   1000023   1000037   # BR(Hp -> neutralino2 chargino2)
     1.26616662E-01   2   1000024   1000025   # BR(Hp -> chargino1 neutralino3)
     9.60908750E-02   2   1000025   1000037   # BR(Hp -> neutralino3 chargino2)
     1.80180838E-01   2   1000024   1000035   # BR(Hp -> chargino1 neutralino4)
     1.29686195E-03   2   1000035   1000037   # BR(Hp -> neutralino4 chargino2)
     1.64524937E-03   2        24        25   # BR(Hp -> W h0)
     2.87528265E-10   2        24        35   # BR(Hp -> W HH)
     1.07817321E-09   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
