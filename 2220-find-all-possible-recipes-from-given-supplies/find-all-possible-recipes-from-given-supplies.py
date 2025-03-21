# from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supp = set(supplies)  # Use a set for quick lookup
        answer = []
        made_something = True  # Flag to check if we are still making progress

        while made_something:  # Keep checking until no new recipes can be made
            made_something = False
            for i in range(len(ingredients)):
                if recipes[i] not in supp:  # Only check recipes that haven't been made yet
                    count = 0
                    for j in range(len(ingredients[i])):
                        if ingredients[i][j] in supp:
                            count += 1
                    
                    if count == len(ingredients[i]):  # All ingredients are available
                        supp.add(recipes[i])  # Add recipe to supplies
                        answer.append(recipes[i])  # Add to answer
                        made_something = True  # Mark that we made progress

        return answer
