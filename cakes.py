"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.


// must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); 
// must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}); 

"""




def cakes(recipe, available):
    recipe = recipe
    available = available
    amount = []

    for item in recipe: # Loop para verificar se está faltando ingrediente
        if item not in available: 
            print(f'Missing item detected: {item}')
            return 0
        
        else:
            if (recipe[item] <= available[item]): # Condicional para verificar se há ingredientes suficientes para a receita
                print(f'ingredient {item} enough')

            else:
                print(f'Amount of ingredient missing: {item} {available[item]}')
                return 0
        
        # divide cada ingrediente disponivel pela receita e adiciona em um vetor para retornar o menor número que será a quantidade de receitas possiveis a ser feita
        calc = available[item] / recipe[item]
        amount.append(calc)

    return int(min(amount))



recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
available = {'flour': 1500, 'sugar': 1200, 'eggs': 12, 'milk': 200}

#recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100};
#available = {'sugar': 500, 'flour': 2000, 'milk': 2000};
print(cakes(recipe, available))

