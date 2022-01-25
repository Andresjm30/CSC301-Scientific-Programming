import time;
import math; 

def naiveAlgo(n):

    print("N= 10^" + str(math.log10(n)));
    startTime = time.time();

    partialSum=0;
    for i in range(0,n):
        partialSum = math.sqrt(19.0) + partialSum;
    endTime = time.time();

    exactSum = (n*math.sqrt(19.0));
    absError = abs(exactSum - partialSum);
    relError = absError/exactSum;
    elapsedTime =  endTime-startTime;
    print("Exact Sum: " + str(exactSum));
    print("Calculated Sum: "+ str(partialSum));
    print("Absolute Error: " + str(absError));
    print("Relative Error: " + str(relError));
    print("Elapsed time for summations: " + str(elapsedTime));
    print("__________________________________________");


def compSumAlgo(n):

    print("N= 10^" + str(math.log10(n)));
    sum = 0;
    carry = 0;
    startTime = time.time();
    for i in range(0,n):
        #Addition of square root of 19
        comp = math.sqrt(19.0) - carry;
        tmpSum = sum + comp;
        carry = (tmpSum - sum) - comp;

        sum=tmpSum;
    endTime = time.time();

    exactSum = (n * math.sqrt(19.0));
    absError = abs(exactSum - sum);
    relError = absError / exactSum;
    elapsedTime = endTime - startTime;
    print("Exact Sum: " + str(exactSum));
    print("Calculated Sum: " +str(sum))
    print("Absolute Error: " + str(absError));
    print("Relative Error: " + str(relError));
    print("Elapsed time for summations: " + str(elapsedTime));
    print("__________________________________________");

def runAlgos():

    size = [10**3,10**4,10**5,10**6,10**7,10**8,];
    for x in size:
        print("NAIVE ALGO: ");
        naiveAlgo(x);
        print("COMPENSATED ALGO:  ");
        compSumAlgo(x);

runAlgos();