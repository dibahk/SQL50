class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books = sorted(books, key= lambda x:(x[1], x[0]), reverse= True)
        height = 0
        while not books == []:
            s = shelfWidth
            shelf_height = 0
            s -= books[0][0] #remaining shelf space
            shelf_height = max(books[0][1], shelf_height)
            books.pop(0)
            while s > 0 and len(books) >= 1: #indicator of shelf finish
                data = [book for book in books if book[0]<=s]
                s -= data[0][0] #remaining shelf space
                books.remove(data[0])
            height += shelf_height
        return height
