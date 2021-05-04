from sympy import *
from numpy import *
import numpy as np


class Diagonalisation:

    def __init__(self, file_U_exp):

        number_atoms_experiment = self._get_number_atoms(file_U_exp)
        #print(number_atoms_experiment)

        self.result_dicts = []

        for iatom in range(0, number_atoms_experiment):
            atomname = self._get_atom_name(filename=file_U_exp, atomnumber=iatom)
            matr_ex = self._get_Umatrix_from_file(filename=file_U_exp, atomnumber=iatom)
            lambdas = self._get_eigenvalues(matrix=self.matrix, atom=self.atom)

            # save result for printing or other use
            self.result_dicts.append({"atomname": atomname, "eigenvalues": self.lambdas_list})

    def _get_number_atoms(self, file_U_exp):
        return sum(1 for line in open(file_U_exp) if line != '\n')

    def _get_Umatrix_from_file(self, filename, atomnumber):
        with open(filename, 'r') as f:
            for iline, line in enumerate(f):
                if iline == atomnumber:
                    splitline = line.split()
                    newarray = splitline[1:]
                    self.matrix = np.array(
                        [[float(newarray[0]), float(newarray[3]), float(newarray[4])],
                         [float(newarray[3]), float(newarray[1]), float(newarray[5])],
                         [float(newarray[4]), float(newarray[5]), float(newarray[2])]])
        print(self.matrix)
        return self.matrix

    def _get_atom_name(self, filename, atomnumber):
        with open(filename, 'r') as f:
            for iline, line in enumerate(f):
                if iline == atomnumber:
                    #print(atomnumber)
                    splitline = line.split()
                    self.atom = splitline[0]
        #print(self.atom)
        return self.atom


    def _get_eigenvalues(self, matrix, atom):
        M = Matrix(matrix)

        #print('Matrix for {} is {} '.format(atom, M))

        P, D = M.diagonalize()

        print('Diagonal of a matrix : {}'.format(D))
        print('Eigenvalues for {} are: lambda1= {}, lambda2= {}, lambda3= {}'.format(atom, "{:.5f}".format(D[0, 0]),
                                                                      "{:.5f}".format(D[1, 1]),
                                                                      "{:.5f}".format(D[2, 2])))
        self.lambdas_list = ['{}'.format("{:.5f}".format(D[0, 0])), '{}'.format("{:.5f}".format(D[1, 1])),
                        '{}'.format("{:.5f}".format(D[2, 2]))]
        #print(self.lambdas_list)
        return self.lambdas_list

    def print_outputfile(self, filename="ADPs_40_out.txt"):

        with open(filename, 'w') as f:
            for dictionary in self.result_dicts:
                print(dictionary["atomname"], dictionary["eigenvalues"][0], dictionary["eigenvalues"][1],
                      dictionary["eigenvalues"][2], file=f)


file_U_exp = 'ADPs_40.txt'

s = Diagonalisation(file_U_exp)
s.print_outputfile()


