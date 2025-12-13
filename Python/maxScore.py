# A library runs a summer reading program where each book belongs to a category and earns a certain number of points. 
# A student may select up to 3 books, but each must be from a different category.
# Given a list of books the student has read, represented as (category, points), 
# determine the maximum total points the student can earn by choosing the optimal subset of books under these constraints.

# Examples
# [("Adventure",5),("Adventure",2),("History",3)] → 8
# [("Adventure",4),("History",3),("Reference",1),("Fiction",2)] → 9
# [("Biography",2),("Biography",4),("Science",3),("Science",1)] → 7

def get_max_score(books):
    best = {}
    for cat, pts in books:
        best[cat] = max(best.get(cat, 0), pts)
    return sum(sorted(best.values(), reverse=True)[:3])
