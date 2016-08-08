#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths, percent_outliers=10):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = [abs(n-p)**2 for n, p in zip(net_worths, predictions)]
    num_outliers = round(len(ages)*percent_outliers/100)

    cleaned_data = zip(ages, net_worths, errors)
    cleaned_data = sorted(cleaned_data, key=lambda x:x[2])
    cleaned_data = cleaned_data[:-num_outliers:]
    
    return cleaned_data

