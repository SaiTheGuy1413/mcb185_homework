import sys
import mcb185

kd = {
    'A':  1.8,
    'C':  2.5,
    'D': -3.5,
    'E': -3.5,
    'F':  2.8,
    'G': -0.4,
    'H': -3.2,
    'I':  4.5,
    'K': -3.9,
    'L':  3.8,
    'M':  1.9,
    'N': -3.5,
    'P': -1.6,
    'Q': -3.5,
    'R': -4.5,
    'S': -0.8,
    'T': -0.7,
    'V':  4.2,
    'W': -0.9,
    'Y': -1.3
}

count = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    ds = defline + seq
    seqi = seq
    move_on = False
    if len(seqi) < 41:
        continue
    
    sig_pep = 0
    for i in range(0, 8):
        sig_pep += kd[seqi[i]]
    if sig_pep >= 20 and 'P' not in seqi[0:8]:
        move_on = True
        
    sp1 = 0
    sp2 = 7
    if not move_on:
        while sp2 < 29:
            sp2 += 1
            sig_pep += kd[seqi[sp2]]
            sig_pep -= kd[seqi[sp1]]
            sp1 += 1

            if sig_pep >= 20 and 'P' not in seqi[sp1:sp2+1]:
                move_on = True
                break 
    
    if move_on == True:
        trans_pep = 0
        for i in range(30, 41):
            trans_pep += kd[seqi[i]]
        if trans_pep >= 22 and 'P' not in seqi[30:41]:
            print(defline)
            continue
        
        tp1 = 30
        tp2 = 40

        while tp2 < len(seqi) - 1:
            tp2 += 1
            trans_pep += kd[seqi[tp2]]
            trans_pep -= kd[seqi[tp1]]
            tp1 += 1

            if trans_pep >= 22 and 'P' not in seqi[tp1:tp2 +1]:
                    count += 1
                    print(defline)
                    break

        
print(count)
        
