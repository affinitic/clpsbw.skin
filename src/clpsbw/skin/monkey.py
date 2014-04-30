import csv
from StringIO import StringIO


def getSavedFormInputForEdit(self, **kwargs):
    """ returns saved as CSV text """
    delimiter = self.csvDelimiter()
    sbuf = StringIO()
    writer = csv.writer(sbuf, delimiter=delimiter)
    for row in self.getSavedFormInput():
        nonbreaking_row = [col.replace("\r\n", " ") for col in row]
        writer.writerow(nonbreaking_row)
    res = sbuf.getvalue()
    sbuf.close()

    return res
