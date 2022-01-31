class Publication(object):
    def __init__(self, doi, publicationYear, title, publicationVenue):
        self.doi = doi
        self.publicationYear = publicationYear
        self.title = title
        self.publicationVenue = publicationVenue
    
    def getDOI(self):
        return self.doi
    
    def getPublicationYear(self):
        return self.publicationYear
    
    def getTitle(self):
        return self.title
    
    def getPublicationVenue(self):
        return self.publicationVenue

    
class Venue(object):
    def __init__(self, identifiers, name):
        self.id = set()
        for identifier in identifiers:
            self.id.add(identifier)
            
        self.name = name
    
    def getIds(self):
        result = []
        for identifier in self.id:
            result.append(identifier)
        result.sort()
        return result
    
    def getName(self):
        return self.name
    
    def addId(self, identifier):
        result = True
        if identifier not in self.id:
            self.id.add(identifier)
        else:
            result = False
        return result
    
    def removeId(self, identifier):
        result = True
        if identifier in self.id:
            self.id.remove(identifier)
        else:
            result = False
        return result
    

class JournalArticle(Publication):
    def __init__(self, doi, publicationYear, title, publicationVenue, issue, volume):
        self.issue = issue
        self.volume = volume
        
        # Here is where the constructor of the superclass is explicitly recalled, so as
        # to handle the input parameters as done in the superclass
        super().__init__(doi, publicationYear, title, publicationVenue)
    
    def getIssue(self):
        return self.issue
    
    def getVolume(self):
        return self.volume


class BookChapter(Publication):
    pass


class Journal(Venue):
    pass


class Book(Venue):
    pass