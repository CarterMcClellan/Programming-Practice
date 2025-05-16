l1 = [
   {
      "quantity": 1,
      "description": "I need to return this recipient..."
   },
   {
      "quantity": 1,
      "description": "I need to return this popular type of street food..."
   },
   {
      "quantity": 1,
      "description": "I need to return this type of remark..."
   },
   {
      "quantity": 1,
      "description": "I need to return this suddenly canceled (agreement)..."
   },
   {
      "quantity": 1,
      "description": "I need to return this classical dance..."
   },
   {
      "quantity": 1,
      "description": "I need to return this graduate-to-be..."
   },
   {
      "quantity": 2,
      "description": "I need to return this soft touch..."
   },
   {
      "quantity": 1,
      "description": "I need to return this type of heron..."
   },
   {
      "quantity": 2,
      "description": "I need to return this soft but unruly drummer..."
   },
   {
      "quantity": 2,
      "description": "I need to return this group of criminals..."
   },
   {
      "quantity": 10,
      "description": "I need to return this type of understanding..."
   },
   {
      "quantity": 9,
      "description": "I need to return this BBB-..."
   },
   {
      "quantity": 1,
      "description": "I need to return this person who wants to quit..."
   },
   {
      "quantity": 7,
      "description": "I need to return this ugly facial expression..."
   },
   {
      "quantity": 6,
      "description": "I need to return this warm breakfast dish..."
   },
   {
      "quantity": 10,
      "description": "I need to return this brown-coloured ale..."
   },
   {
      "quantity": 4,
      "description": "I need to return this plant that grows underground..."
   },
   {
      "quantity": 6,
      "description": "I need to return this common solvent..."
   },
   {
      "quantity": 2,
      "description": "I need to return this type of symmetry..."
   },
   {
      "quantity": 7,
      "description": "I need to return this partner dance..."
   },
   {
      "quantity": None,
      "description": "I need to return these good luck charms..."
   }
]

l2 = [
   {
      "description": "...said an important C++ component",
      "price": "$4.09"
   },
   {
      "description": "...said le supermarché, il ristorante and el dinosaurio",
      "price": "$5.08"
   },
   {
      "description": "...said the counterargument",
      "price": "$5.08"
   },
   {
      "description": "...said the laundry room staple",
      "price": "$5.09"
   },
   {
      "description": "...said the heavy machine useful in forestry",
      "price": "$5.10"
   },
   {
      "description": "...said the remnants of an explosion",
      "price": "$5.11"
   },
   {
      "description": "...said the (story) that was worth repeating",
      "price": "$6.08"
   },
   {
      "description": "...said Captain Marvel & Black Widow",
      "price": "$6.08"
   },
   {
      "description": "...said this type of inexpensive flooring",
      "price": "$6.08"
   },
   {
      "description": "...said the (fuse) that seemed ready to go off",
      "price": "$6.09"
   },
   {
      "description": "...said the 4-dimensional solid",
      "price": "$6.09"
   },
   {
      "description": "...said the distinguished ambassador",
      "price": "$6.09"
   },
   {
      "description": "...said Duel (or High School Musical)",
      "price": "$6.09"
   },
   {
      "description": "...said one of the major scenes in West Side Story",
      "price": "$6.11"
   },
   {
      "description": "...said the narrow bike trail",
      "price": "$6.11"
   },
   {
      "description": "...said the cozy wine shop",
      "price": "$7.07"
   },
   {
      "description": "...said the total reprobate",
      "price": "$7.10"
   },
   {
      "description": "...said the often-wet piece of equipment",
      "price": "$7.10"
   },
   {
      "description": "...said the person who was here before me",
      "price": "$7.11"
   },
   {
      "description": "...said the person hovering a foot off the ground",
      "price": "$8.09"
   }
]

print("Len l1", len(l1))
print("Len l2", len(l2))

N, M = len(l1), len(l2)

for idx in range(min(N, M)):
    sent_1 = l1[idx]["description"].replace("...", "")
    sent_2 = l2[idx]["description"].replace("...", "")

    print(f"{sent_1} {sent_2}")

# def format_options(ele):
#     return ele.replace("...said", "")

# options = [e['description'] for e in l2]
# options_as_str = "\n".join([f"{idx+1}. {format_options(e)}" for idx, e in enumerate(options)])
# for v in l1:
#     desc_formatted = v['description'].replace("I need to return this", "")
#     prompt = """
# Select the option which best completes this sentence:
#     {sentence}

# {options}
# """.format(sentence=desc_formatted, options=options_as_str)
#     print(prompt)

#     input("continue...")