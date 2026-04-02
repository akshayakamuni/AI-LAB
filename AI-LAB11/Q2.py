def solve_csp():
    """
    CSP backtracking with constraint propagation.
    Variables: S, E, N, D, M, O, R, Y
    Constraints:
      - All digits unique (0-9)
      - S != 0, M != 0
      - SEND + MORE = MONEY
    """
    # We solve column by column (right to left) with carry propagation
    # D + E = Y + 10*c1
    # N + R + c1 = E + 10*c2
    # E + O + c2 = N + 10*c3
    # S + M + c3 = O + 10*c4  (c4 must be 1 since MONEY has 5 digits)
    # M = c4 => M = 1

    results = []

    for S in range(1, 10):
      for M in range(1, 10):
        if M != S:
         for E in range(0, 10):
          if len({S,M,E}) < 3: continue
          for N in range(0, 10):
           if len({S,M,E,N}) < 4: continue
           for D in range(0, 10):
            if len({S,M,E,N,D}) < 5: continue
            for O in range(0, 10):
             if len({S,M,E,N,D,O}) < 6: continue
             for R in range(0, 10):
              if len({S,M,E,N,D,O,R}) < 7: continue
              for Y in range(0, 10):
               if len({S,M,E,N,D,O,R,Y}) < 8: continue

               SEND  = S*1000 + E*100 + N*10 + D
               MORE  = M*1000 + O*100 + R*10 + E
               MONEY = M*10000 + O*1000 + N*100 + E*10 + Y

               if SEND + MORE == MONEY:
                results.append((S,E,N,D,M,O,R,Y))

    for S,E,N,D,M,O,R,Y in results:
        SEND  = S*1000 + E*100 + N*10 + D
        MORE  = M*1000 + O*100 + R*10 + E
        MONEY = M*10000 + O*1000 + N*100 + E*10 + Y
        print(f"S={S} E={E} N={N} D={D} M={M} O={O} R={R} Y={Y}")
        print(f"  {SEND}")
        print(f"+ {MORE}")
        print(f"------")
        print(f"  {MONEY}")

solve_csp()
