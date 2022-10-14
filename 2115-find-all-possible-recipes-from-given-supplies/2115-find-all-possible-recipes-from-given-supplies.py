class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        def check(i):
            for a in ingredients[i]:
                if a not in supplies:
                    return False
                
            return True
        
        for _ in range(len(recipes)):
            for i in range(len(recipes)):
                if recipes[i]not in supplies and check(i):
                    supplies.add(recipes[i])
                    
        return [a for a in recipes if a in supplies]
    
    