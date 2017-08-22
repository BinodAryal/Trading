"""
A simple wrapper for linear regression.  (c) 2015 Tucker Balch
"""
"""
http://quantsoftware.gatech.edu/MC3-Project-1
"""
"""
@author Binod Aryal

"""
import numpy as np

class KNNLearner(object):

    def __init__(self, k = 3, verbose = False):
        self.verbose = verbose
        self.knn = k
        if self.verbose :
            print "Created " + str(k) + " nearest neighbour learner"


    def addEvidence(self,dataX,dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        if not hasattr(self,'xEvidence'):
            self.xEvidence = dataX
        else:
            self.xEvidence = np.append(self.xEvidence, dataX, 0)

        if not hasattr(self,'yEvidence'):
            self.yEvidence = dataY
        else:
            self.yEvidence = np.append(self.yEvidence, dataY, 0)


    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        ## normalize the data, so that larger scales don't have prevalence
        normalised_xEvidence = (self.xEvidence - self.xEvidence.min(axis=0))/ (self.xEvidence.max(axis=0) - self.xEvidence.min(axis=0))
        normalised_points = (points - self.xEvidence.min(axis=0))/ (self.xEvidence.max(axis=0) - self.xEvidence.min(axis=0))

        number_of_points = np.shape(points)[0]

        if self.verbose :
            print "KNN Learner:Querying:" + str(points)

        output = np.zeros(number_of_points)

        for i in range(0, number_of_points):
            point = normalised_points[i]

            ## To query, calculate the distance between the query points and each value
            distance = np.sqrt(np.sum(np.square(normalised_xEvidence - point), axis = 1))
            nearestNeighbourIndex = distance.argsort()[:self.knn]
            nearestNeighbourY = self.yEvidence[nearestNeighbourIndex]

            ## Now we need to take the mean of the k Y values
            output[i] = nearestNeighbourY.mean()


        if self.verbose :
            print "KNN Learner:Query output:" + str(output)

        return output

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
