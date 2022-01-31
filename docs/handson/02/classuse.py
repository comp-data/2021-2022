from myclasses import JournalArticle, Journal

journal_1 = Journal(["1531-6912"], "Comparative and Functional Genomics")

journal_article_1 = JournalArticle("10.1002/cfg.304", 
                                   2003, 
                                   "Development of Computational Tools for the Inference of Protein Interaction Specificity Rules and Functional Annotation Using Structural Information", 
                                   journal_1, 
                                   "4", 
                                   "4")

print("-- Journal article metadata")
print(" | title:", journal_article_1.getTitle())
print(" | venue name:", journal_article_1.getPublicationVenue().getName())
print(" | issue:", journal_article_1.getIssue())
print(" | volume:", journal_article_1.getVolume())
