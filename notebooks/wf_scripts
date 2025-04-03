#!/usr/bin/env python

import argparse
import numpy as np
import random

class Population:
    import numpy as np
    def __init__(self, N=10, f=0.2, outfile=None, with_np=False):
        self.N = N
        self.f = f
        self.with_np = with_np
        self.steps = 0
        self.state = "segregating"
        self.outfile = outfile

        derived_count = round(N*f)
        self.pop = [0] * (N - derived_count) + [1] * derived_count

        if with_np:
            self.pop = np.array(self.pop)

    def __repr__(self):
        return f"Population(N={self.N}, f={self.f})"

    def step(self, ngens=1):
        if self.outfile:
            out = open(self.outfile, 'a')
        for i in range(ngens):
            # Test fixation/loss
            derived = sum(self.pop)
            if derived == 0:
                self.state = "extinct"
                break
            elif derived == len(self.pop):
                self.state = "fixed"
                break

            if self.with_np:
                self.pop = np.random.choice(self.pop, size=self.N)
            else:
                self.pop = random.choices(self.pop, k=self.N)
            if self.outfile:
                out.write("".join([str(x) for x in self.pop]) + "\n")
            self.steps += 1
        if self.outfile:
            out.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", help="Size if population in individuals", 
                        type=int, default=1000)
    parser.add_argument("--ngens", help="Number of generations to run", 
                        type=int, default=1000)
    parser.add_argument("-f", help="Initial derived allele frequency", 
                        type=float, default=0.2)
    parser.add_argument("-o", help="Outfile", dest="outfile")
    parser.add_argument("--withnp",
                         help="Use numpy rather than lists",
                         action="store_true")
    parser.add_argument("-v", "--verbose",
                         help="increase output verbosity",
                         action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print(args)

    p = Population(N=args.N, f=args.f, outfile=args.outfile, with_np=args.withnp)
    p.step(ngens=args.ngens)
    print(f"{p.state} after generations: {p.steps}; freq(a): {sum(p.pop)/p.N}")