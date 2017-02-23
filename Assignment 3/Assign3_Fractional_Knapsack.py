# From Wikipedia: Solved by a greedy algorithm that considers
# the materials in sorted order by their values per unit weight.
# If sum of the choices made so far equals capacity W, then algor. sets X_i = 0
# If difference d between sum of choices made so far and W is smaller than W_i, then alg. sets x_i = d
# In remaining case, alg. chooses x_i = w_i

#weight = [2.0, 3.4, 1.5, 2.3, 8.8, 2.5, 7.8]
#value = [25.0, 67.2, 33.4, 24.6, 53.5, 1.6, 10.5]
#item = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]


def greedy_fractional_knapsack(item_list):
    #sort_by_value_per_unit_weight = sorted(((name, weight, value/weight)
    #                                        for name, weight, value in item_list),
    #                                        reverse = True)
    sort_by_value_per_unit_weight = sorted(((value/weight, weight, name)
                                            for name, weight, value in item_list),
                                            reverse = True)

    #print sort_by_value_per_unit_weight
    # Total
    weight_in_bag = 0.0
    total_value = 0.0

    in_bag = []

    print "Bag Contents:"
    for value, weight, name in sort_by_value_per_unit_weight:
        #print name, weight, value
        #piece = min(15-0, 1.3)
        #piece_weight = min(maximum_weight - weight_in_bag, weight)
        if weight_in_bag < maximum_weight:
            piece_weight = min(maximum_weight - weight_in_bag, weight)
            # Adding the item's weight to the bag
            weight_in_bag += piece_weight
            # Adding the item's pieces value to the bag
            value_to_bag = piece_weight * value
            # Storing total value of things in the bag
            total_value += value_to_bag
            print name, piece_weight, value_to_bag
            in_bag += [name, weight_in_bag, value_to_bag]


    print "\ntotal weight in bag:  total value in bag:"
    return weight_in_bag, total_value


maximum_weight = 20.0

item = [("item1", 2.0, 35.0),
        ("item2", 3.4, 67.2),
        ("item3", 1.5, 33.4),
        ("item4", 2.3, 24.6),
        ("item5", 8.3, 53.5),
        ("item6", 2.5, 1.6),
        ("item7", 7.8, 10.5),
        ("item8", 3.5, 20.3),
        ("item9", 1.3, 10.2),
        ("item10", 8.9, 78.0)]


print greedy_fractional_knapsack(item)