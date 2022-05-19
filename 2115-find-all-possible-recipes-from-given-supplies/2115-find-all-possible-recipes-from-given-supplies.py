class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        outgoing = {}
        incomming = {}
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                if recipe not in incomming:
                    incomming[recipe] = 1
                else:
                    incomming[recipe] += 1
                if ing not in incomming:
                    incomming[ing] = 0                
                    
                if recipe not in outgoing:
                    outgoing[recipe] = set()
                if ing not in outgoing:
                    outgoing[ing] = {recipe}
                else:
                    outgoing[ing].add(recipe)
        
        recipes = set(recipes)
        for key in incomming.keys():
            if key not in recipes and key not in supplies:
                incomming[key] +=1
        q = collections.deque()
        for key in incomming.keys():
            if incomming[key] == 0:
                q.append(key)
                
        top_sort = []
        
        while q:
            node = q.popleft()
            
            for v in outgoing[node]:
                incomming[v]-=1
                if incomming[v] == 0:
                    q.append(v)
            
            if node in recipes:
                top_sort.append(node)
            
        return top_sort