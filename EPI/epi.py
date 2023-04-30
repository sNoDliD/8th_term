from math import prod

COCOMO_1_coeffs = [[2.4, 1.05, 2.5, 0.38],
                   [3.0, 1.12, 2.5, 0.35],
                   [3.6, 1.20, 2.5, 0.32]]

def COCOMO_1(SIZE, proj_type):
    a, b, c, d = COCOMO_1_coeffs[proj_type]
    PM = a * SIZE**b
    TM = c * PM**d
    SS = PM / TM
    P = SIZE / PM
    return PM, TM, SS, P


SIZE = 72

print("COCOMO_1:")
print(COCOMO_1(SIZE, 0))
print(COCOMO_1(SIZE, 1))
print(COCOMO_1(SIZE, 2))
print()

# 1 = n/a
# 1.00 != n/a
COCOMO_inter_CDs = {
    "RELY": [0.75, 0.88, 1.00, 1.15, 1.40,    1],
    "DATA": [   1, 0.94, 1.00, 1.08, 1.16,    1],
    "CPLX": [0.70, 0.85, 1.00, 1.15, 1.30, 1.65],
    "TIME": [   1,    1, 1.00, 1.11, 1.30, 1.66],
    "STOR": [   1,    1, 1.00, 1.06, 1.21, 1.56],
    "VIRT": [   1, 0.87, 1.00, 1.15, 1.30,    1],
    "TURN": [   1, 0.87, 1.00, 1.07, 1.15,    1],
    "ACAP": [1.46, 1.19, 1.00, 0.86, 0.71,    1],
    "AEXP": [1.29, 1.13, 1.00, 0.91, 0.82,    1],
    "PCAP": [1.42, 1.17, 1.00, 0.86, 0.70,    1],
    "VEXP": [1.21, 1.10, 1.00, 0.90,    1,    1],
    "LEXP": [1.14, 1.07, 1.00, 0.95,    1,    1],
    "MODP": [1.24, 1.10, 1.00, 0.91, 0.82,    1],
    "TOOL": [1.24, 1.10, 1.00, 0.91, 0.83,    1],
    "SCED": [1.23, 1.08, 1.00, 1.04, 1.10,    1],
  }

COCOMO_inter_coeffs = [[3.2, 1.05],
                       [3.0, 1.12],
                       [2.8, 1.20]]

VL, L, N, H, VH, C = range(6)

def COCOMO_inter(SIZE, CDs_config, proj_type):
    a, b = COCOMO_inter_coeffs[proj_type]
    CDs = [vals[CDs_config.get(CD, N)] for CD, vals in COCOMO_inter_CDs.items()]
    EAF = prod(CDs)
    PM = EAF * a * SIZE**b
    return PM

CDs_configs_1 = [{
    "TIME": i,
    "LEXP": i,
    "CPLX": i,
  } for i in range(N, VH + 1)]

print("COCOMO_inter_1:")
for i in range(3):
    print([COCOMO_inter(SIZE, CDs, i) for CDs in CDs_configs_1])
print()

CDs_config_2 = {
    "RELY": L,
    "DATA": VH,
    "CPLX": H,
    "TIME": H,
    "STOR": VH,
    "VIRT": L,
    "TURN": H,
    "ACAP": H,
    "AEXP": VH,
    "PCAP": H,
    "VEXP": H,
    "LEXP": VH,
    "MODP": H,
    "TOOL": H,
    "SCED": H
  }

print(f"COCOMO_inter_2:")
for i in range(3):
  print(COCOMO_inter(SIZE, CDs_config_2, i))

print("CDs:")
for CD, vals in COCOMO_inter_CDs.items():
    print(f"{CD} = {vals[CDs_config_2.get(CD, N)]}")