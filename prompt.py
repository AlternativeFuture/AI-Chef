import json

SYSTEM_JSON = "You are a helpful assistant designed to response JSON object."
SYSTEM_CHEF = """You are a useful helper that can supply the name of the meal, the ingredient 
          measurements in SI units, and cooking instructions for three different dishes that can be made with the 
          components that are provided."""
USER = "ingredients: {}."
# Current data is{}.   Also, don't count ingredients you can't identify

# chicken, tomatoes, cheese, flour, pepperoni

# TODO: implement json loads
RESPONSE_EXAMPLE = json.dumps({
  "dishes": [
    {
      "name": "Bacon and Cheese Omelette",
      "ingredients": {
        "cheese": "100 grams",
        "bacon": "100 grams"
      },
      "instructions": "1. Whisk 2 eggs in a bowl. \n2. Cook the bacon in a pan until crispy, then remove and set aside. \n3. Pour the whisked eggs into the pan and cook until the edges start to set. \n4. Sprinkle the cheese and bacon over one half of the omelette. \n5. Fold the other half over the filling and cook for another minute. \n6. Slide the omelette onto a plate and serve hot."
    },
    {
      "name": "Bacon and Cheese Stuffed Chicken Breast",
      "ingredients": {
        "cheese": "150 grams",
        "bacon": "150 grams"
      },
      "instructions": "1. Preheat the oven to 375°F (190°C). \n2. Pound the chicken breasts to an even thickness. \n3. Season the chicken with salt and pepper. \n4. Lay the bacon slices on a cutting board, then place the chicken breast on top. \n5. Sprinkle cheese over the chicken breast. \n6. Roll up the chicken breast and secure with toothpicks. \n7. Place the chicken in a baking dish and bake for 25-30 minutes."
    },
    {
      "name": "Cheesy Bacon Pasta",
      "ingredients": {
        "cheese": "200 grams",
        "bacon": "200 grams"
      },
      "instructions": "1. Cook the pasta according to package instructions. \n2. In a separate pan, cook the bacon until crispy, then remove and set aside. \n3. In the same pan, add the cooked pasta and stir in the cheese until melted. \n4. Crumble the bacon and stir into the cheesy pasta. \n5. Serve hot with a sprinkle of black pepper."
    }
  ]
})
