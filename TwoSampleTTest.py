# Patients with high blood pressure would be randomly assigned into two groups,
# a placebo group and a treatment group. The placebo group would receive conventional
# treatment while the treatment group would receive a new drug that is expected to
# lower blood pressure.  After treatment for a couple of months,
# the two-sample t test is used to compare the average blood pressure of the two groups.

# Source: https://services.ncl.ac.uk/itservice/research/dataanalysis/simpletests/ttests/independentsamplesttesttwo-samplesttest/#:~:text=Independent%2Dsamples%20t%20test%20(two%2Dsample%20t%20test)&text=As%20an%20example%2C%20a%20practical,group%20and%20a%20treatment%20group.

import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ttest_ind

class TTest:
    def __init__(self, groupOne, groupTwo):
        self.groupOne = groupOne
        self.groupTwo = groupTwo

    # Function to calculate means of both groups
    def calculate_mean(self):
        print("Mean of group one: ", self.groupOne.mean())
        print("Mean of group two: ", self.groupTwo.mean())

    # Function to check distributions of both samples using Anderson-Darling test from SciPy
    def check_distribution(self):
        result1 = stats.anderson(self.groupOne)
        result2 = stats.anderson(self.groupTwo)
        results = [result1, result2]
        n = 0
        for result in results:
            print('\n')
            n += 1
            for sigLevel, critVal in zip(result.significance_level, result.critical_values):
                print(f'Distribution for Group {n}: ')
                if result.statistic < critVal:
                    print(f'At a {sigLevel}% significance level, data is normal')
                else:
                    print(f'At a {sigLevel}% significance level, data is not normal')

    # Function to check that all samples are from a population of equal variance using Levene test from SciPy
    def check_variance(self):
        stat, pVal = stats.levene(self.groupOne, self.groupTwo)
        if pVal > 0.05:
            print("\nAssume equal variance")
        else:
            print("\nVariances differ")

    # Perform Two-Sided T-Test using Statsmodels to include Degrees of Freedom
    def perform_test(self):
        tStat, pVal, degreesFreedom = ttest_ind(self.groupOne, self.groupTwo, usevar="pooled")
        if pVal > 0.05:
            print("Failed to reject the null hypothesis. Both groups have equal means.")
        else:
            print("Reject the null hypothesis. Both groups have different means. ")

class main:
    def __init__(self):
        # Assumption: Both groups are independent of each other
        # Group 1 = placebo
        groupOne = np.array([90, 95, 67, 120, 89, 92, 100, 82, 79, 85])
        # Group 2 = new drug
        groupTwo = np.array([71, 79, 69, 98, 91, 85, 89, 75, 78, 80])

        testCase = TTest(groupOne, groupTwo)
        testCase.calculate_mean()
        testCase.check_distribution()
        testCase.check_variance()
        testCase.perform_test()

main()