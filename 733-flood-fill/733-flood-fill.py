class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # sr => row
        # sc => col
        seen = set()
        def filler(image, sr, sc, newColor, curColor):
            if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]!=curColor:
                return image
            image[sr][sc] = newColor
            # UP
            if (sr-1, sc) not in seen:
                seen.add((sr-1, sc))
                filler(image, sr-1, sc, newColor, curColor)
            # DOWN
            if (sr+1, sc) not in seen:
                seen.add((sr+1, sc))
                filler(image, sr+1, sc, newColor, curColor)
            # LEFT
            if (sr, sc-1) not in seen:
                seen.add((sr, sc-1))
                filler(image, sr, sc-1, newColor, curColor)
            # RIGHT
            if (sr, sc+1) not in seen:
                seen.add((sr, sc+1))
                filler(image, sr, sc+1, newColor, curColor)
            
            return image
        
        return filler(image, sr, sc, newColor, image[sr][sc])